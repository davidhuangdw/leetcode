
# usage:
#   ruby fetch_question.rb some-slug-title

require_relative 'scripts/leetcode_crawler'
require_relative 'scripts/question_json_parser'
require_relative 'scripts/problems_file_writer'
require_relative 'scripts/constants'

class FetchQuestionJob
  attr_reader :slug_title, :cookie, :crawler, :parser, :filer

  def initialize(slug_title, cookie: nil)
    @slug_title = slug_title
    @crawler = LeetcodeCrawler.new(cookie)
    @parser = QuestionJsonParser.new(nil)
    @filer = ProblemsFileWriter.new(parser: parser)
  end

  def run
    parser.source = question_body

    filer.save_question_file(question_body)

    puts 'fetching solution...'
    filer.save_solution_file crawler.fetch_solution(slug_title).body
  end

  def question_body
    return @question_body if @question_body
    puts 'fetching question...'
    @question_body = crawler.fetch_question(slug_title).body
  end

end

raise "missing the argument" if ARGV.empty?
FetchQuestionJob.new(ARGV[0], cookie: DEFAULTS_CONFIG[:cookie]).run

