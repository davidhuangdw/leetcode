
# usage:
# ruby fetch_code_snippet.rb some-slug-title

require_relative 'scripts/leetcode_crawler'
require_relative 'scripts/question_json_parser'
require_relative 'scripts/problems_file_writer'
require_relative 'scripts/code_snippet_builder'

SEARCH_ORDERS = {
    kotlin: {
        src_dir: 'kotlin/src/main/kotlin/',
        suffix: '.kt',
        comment_prefix: '//',
        front_lines: "import org.junit.Assert\nimport org.junit.Test"
    },
    python3: {
        src_dir: 'python/',
        suffix: '.py',
        separator: '_',
        comment_prefix: '#',
        front_lines: 'from unittest import TestCase',
    },
    python: {
        src_dir: 'python/',
        suffix: '.py',
        separator: '_',
        comment_prefix: '#',
        front_lines: 'from unittest import TestCase',
    },
}
PROBLEMS_URL = 'https://leetcode.com/problems/'


# main:
raise "missing the argument" if ARGV.empty?
slug_title = ARGV[0]
cookie = ENV['LEETCODE_COOKIE']
crawler = LeetcodeCrawler.new(cookie)
parser = QuestionJsonParser.new(nil)
filer = ProblemsFileWriter.new(parser)

question_file = Dir[File.join(filer.question_dir, "*#{slug_title}")][0]
question_body = if question_file
                  File.read(question_file)
                else
                  puts 'fetching question...'
                  crawler.fetch_question(slug_title).body
                end

parser.question_body = question_body  # setup parser for filer
unless question_file
  filer.save_question_file(question_body)
  puts filer.question_file_path
end

for lang,config in SEARCH_ORDERS
  snippet = parser.code_snippet(lang)
  next unless snippet
  file_path = File.join(config[:src_dir], parser.source_file_name(config))
  url = File.join(PROBLEMS_URL, slug_title)
  unless File.exist?(file_path)
    text = CodeSnippetBuilder.build(snippet, class_name: parser.camelized_title, comment: url, **config)
    File.write(file_path, text)

    puts snippet
    puts "Success: #{file_path} -----------"
    puts text
  end
end
