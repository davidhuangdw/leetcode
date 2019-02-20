
# usage:
#   ruby fetch_question_by_slug_title.rb some-slug-title

require_relative 'scripts/leetcode_crawler'
require_relative 'scripts/question_json_parser'
require_relative 'scripts/problems_file_writer'

raise "missing the argument" if ARGV.empty?
slug_title = ARGV[0]
cookie = ENV['LEETCODE_COOKIE']
crawler = LeetcodeCrawler.new(cookie)
parser = QuestionJsonParser.new(nil)
filer = ProblemsFileWriter.new(parser)

puts 'fetching question...'
question_body = crawler.fetch_question(slug_title).body
parser.question_body = question_body
filer.save_question_file(question_body)
puts filer.question_file_path

puts 'fetching solution...'
filer.save_solution_file crawler.fetch_solution(slug_title).body
puts filer.solution_file_path
