
# usage:
# ruby fetch_code_snippet.rb some-slug-title
# ruby fetch_code_snippet.rb some-slug-title kotlin

require 'set'
require_relative 'scripts/question_json_parser'
require_relative 'scripts/problems_file_writer'
require_relative 'scripts/code_snippet_builder'
require_relative 'scripts/questions'
require_relative 'scripts/constants'


class FetchCodeSnippetJob
  SEARCH_ORDERS = DEFAULTS_CONFIG[:code_snippets][:langs_search_order]
  PROBLEMS_URL = DEFAULTS_CONFIG[:problems_url_prefix]

  attr_reader :slug_title, :parser, :filer, :questions, :limit_langs

  def initialize(slug_title, cookie: nil, limit_langs: nil)
    @slug_title = slug_title
    @parser = QuestionJsonParser.new(nil)
    @filer = ProblemsFileWriter.new(parser: parser)
    @questions = Questions.new(cookie: cookie)
    @limit_langs = limit_langs || []
  end

  def run
    parser.source = question_body
    done = Set.new

    SEARCH_ORDERS.each do |lang, config|
      next unless limit_langs.empty? || limit_langs.include?(lang.to_s)
      snippet = parser.code_snippet(lang)
      next unless snippet

      file_path = File.join(config[:src_dir], parser.source_file_name(config))
      next if done.include?(file_path)
      done.add(file_path)
      if File.exist?(file_path)
        puts "--------- skip: #{file_path} -----------"
      else
        url = File.join(PROBLEMS_URL, slug_title)
        text = CodeSnippetBuilder.build(snippet, class_name: parser.camelized_title, comment: url, **config)
        File.write(file_path, text)

        puts "--------- Success: #{file_path} -----------"
        puts text
      end
    end
  end

  private

  def question_body
    @question_body ||= questions.get_question_body(slug_title){|body| filer.save_question_file(body) }
  end

end


# main:
raise "missing the argument" if ARGV.empty?
FetchCodeSnippetJob.new(ARGV[0], cookie: DEFAULTS_CONFIG[:cookie], limit_langs: ARGV[1..-1]).run

