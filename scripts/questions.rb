require_relative 'leetcode_crawler'
require_relative 'question_json_parser'
require_relative 'problems_file_writer'
require_relative 'problem_metadata_parser'
require_relative 'constants'

class Questions
  LATEST_DURATION = DEFAULTS_CONFIG[:problem_list_keep_duration]

  attr_reader :cookie, :enforce_fetch_list, :crawler, :parser, :filer

  def initialize(cookie: DEFAULTS_CONFIG[:cookie], enforce_fetch_list: false)
    @cookie = cookie
    @enforce_fetch_list = enforce_fetch_list
    @crawler = LeetcodeCrawler.new(cookie)
    @filer = ProblemsFileWriter.new
  end

  def get_question(slug_title)
    QuestionJsonParser.new(get_question_body(slug_title))
  end

  def read_question(slug_title)
    body = read_question_body(slug_title)
    body && QuestionJsonParser.new(body)
  end

  def fetch_question(slug_title)
    QuestionJsonParser.new(fetch_question_body(slug_title))
  end

  def get_list(list_body = nil)
    ProblemMetadataParser.decode_problem_metadata_list(list_body || get_list_body)
  end

  def fetch_list
    ProblemMetadataParser.decode_problem_metadata_list(fetch_list_body)
  end

  def read_company_list(company, &order)
    JSON.parse(filer.read_company_file(company) || '{}').values
        .sort_by(&order).to_a.reverse
  end

  def get_question_body(slug_title, &after_fetch)
    read_question_body(slug_title) || fetch_question_body(slug_title, &after_fetch)
  end

  def read_question_body(slug_title)
    paths = filer.search_question_file(slug_title)
    puts "-----Ambiguous: multiple files for question #{slug_title} is found: #{paths.join(', ')}" if paths.size > 1
    puts "-----Not found: the question file for #{slug_title} is no found.." if paths.empty?
    paths[0] && File.read(paths[0])
  end

  def fetch_question_body(slug_title, &after_fetch)
    crawler.fetch_question(slug_title).body
        .tap{|body|  after_fetch.call(body) if after_fetch}
  end

  def get_list_body(&after_fetch)
    !enforce_fetch_list && already_latest_problem_list? ? read_list_body : fetch_list_body(&after_fetch)
  end

  def read_list_body
    filer.read_problems_list_file
  end

  def fetch_list_body(&after_fetch)
    puts "fetch problem list..."
    crawler.fetch_problems.body
        .tap{|body|  after_fetch.call(body) if after_fetch}
  end

  private

  def already_latest_problem_list?
    problem_list_file = Dir[filer.problem_list_file_path][0]
    problem_list_file && File.open(problem_list_file).stat.mtime + LATEST_DURATION >= Time.now
  end
end
