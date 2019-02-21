require_relative 'leetcode_crawler'
require_relative 'problem_metadata_parser'
require_relative 'problems_file_writer'
require_relative 'questions'
require_relative 'constants'


class FetchAllQuestionsJob

  attr_accessor :front_id_range, :cookie, :enforce_fetch_list
  attr_reader :crawler, :parser, :filer, :questions

  def initialize(front_id_range: 0..FLOAT::INFINITY, cookie:, enforce_fetch_list: false)
    @front_id_range = front_id_range
    @cookie = cookie
    @enforce_fetch_list = enforce_fetch_list
    @crawler = LeetcodeCrawler.new(cookie)
    @parser = ProblemMetadataParser.new(nil)
    @filer = ProblemsFileWriter.new(parser: parser)
    @questions = Questions.new(cookie: cookie, enforce_fetch_list: enforce_fetch_list)
  end

  def run
    puts "RANGE: #{@front_id_range}"
    puts problem_list.size
    filer

    problem_list.each do |problem_metadata|
      parser.source = problem_metadata
      puts filer.question_file_name

      begin
        filer.save_question_file crawler.fetch_question(parser.title).body
        filer.save_solution_file crawler.fetch_solution(parser.title).body
      rescue => e
        puts "fetch question failed: #{e.inspect}"
      end
    end
  end

  def problem_list_body
    @problem_body ||= questions.get_list_body do |body|
                        filer.save_problems_list_file(body)   # save after fetched
                      end
  end

  def problem_list
    @problem_list ||= questions.get_list(problem_list_body).select do |problem|
      front_id_range.include? ProblemMetadataParser.new(problem).front_id.to_i
    end
  end

  private


end
