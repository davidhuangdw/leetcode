
# usage:
#   ruby fetch_questions.rb
#   ruby fetch_questions.rb 900 1000

require_relative 'scripts/leetcode_crawler'
require_relative 'scripts/problem_metadata_parser'
require_relative 'scripts/problems_file_writer'


@problem_list_file_exist = true
@front_id_range = 0..10000
unless ARGV.empty?
  @front_id_range = ARGV[0].to_i..ARGV[1].to_i
end

@cookie = ENV['LEETCODE_COOKIE']
@crawler = LeetcodeCrawler.new(@cookie)
@parser = ProblemMetadataParser.new(nil)
@filer = ProblemsFileWriter.new(@parser)

def problem_list_body
  @problem_body ||= @problem_list_file_exist ? @filer.read_problems_list_file : @crawler.fetch_problems.body
end

def problem_list
  ProblemMetadataParser.decode_problem_metadata_list(problem_list_body)
      .select {|problem| @front_id_range.include? ProblemMetadataParser.new(problem).front_id.to_i }
end


# main:
puts "RANGE: #{@front_id_range}"
puts "fetch problem list..."
@filer.save_problems_list_file(problem_list_body) unless @problem_list_file_exist

puts problem_list.size
problem_list.each do |problem_metadata|
  @parser.metadata = problem_metadata
  puts @filer.question_file_name

  begin
    @filer.save_question_file @crawler.fetch_question(@parser.title).body
    @filer.save_solution_file @crawler.fetch_solution(@parser.title).body
  rescue => e
    puts "fetch question failed: #{e.inspect}"
  end
end

