
# usage:
#   ruby compile_companies.rb

require_relative 'scripts/problems_file_writer'
require_relative 'scripts/code_snippet_builder'
require_relative 'scripts/problem_metadata_parser'
require_relative 'scripts/questions'
require_relative 'scripts/constants'

class CompileCompaniesJob
  ENCOUNTER_COUNT_KEY =  'timesEncountered'
  SLUG_NAME_KEY = 'slug'
  attr_reader :filer, :questions, :companies

  def initialize(cookie: nil)
    @filer = ProblemsFileWriter.new
    @questions = Questions.new(cookie: cookie)
    @companies = Hash.new do |hash, company_name|
      body = filer.read_company_file(company_name)
      hash[company_name] = body ? JSON.parse(body) : {}
    end
  end

  def run
    titles = questions.get_list.map{|problem| ProblemMetadataParser.new(problem).title }

    titles.each do |title|
      question = questions.read_question(title)  # read from file only
      stats = (question.company_stats || {}).values.flatten
      next if stats.empty?

      info = question.general_info
      stats.sort_by{|s| s[ENCOUNTER_COUNT_KEY]}.each do |stat|
        name = stat[SLUG_NAME_KEY]
        encounters = stat[ENCOUNTER_COUNT_KEY]
        companies[name][question.front_id] = info.merge(encounters: encounters)
      end
    end

    companies.each do |name, value|
      filer.save_company_file(value.to_json, company: name)
    end
  end

  def convert_to_texts
    # item example:
    # {
    #   "id"=>"965",
    #   "front_id"=>"929",
    #   "title"=>"unique-email-addresses",
    #   "difficulty"=>"Easy",
    #   "likes"=>321,
    #   "dislikes"=>86,
    #   "paid_only"=>false,
    #   "encounters"=>265
    # }
    #

    sort_keys = DEFAULTS_CONFIG[:company_data][:sort_keys]
    print_keys = DEFAULTS_CONFIG[:company_data][:print_keys]
    inline_separator = "\t"

    current_companies.each do |company|
      lines = questions.read_company_list(company){|item| sort_keys.map{|k| item[k]} }
                  .map{|item| print_keys.map{|k| item[k]}.join(inline_separator)}
      lines = [print_keys.join(inline_separator)] + lines
      filer.class.save(lines.join("\n"), company_text_file_path(company))
    end
  end

  private

  def company_text_file_path(company)
    dir = filer.company_dir + '_texts'
    File.join(dir, company)
  end

  def current_companies
    Dir::entries(ProblemsFileWriter.new.company_dir)
        .select{|name| name[0] != '.'}
  end

end


# main:
job = CompileCompaniesJob.new(cookie: DEFAULTS_CONFIG[:cookie])
job.run
job.convert_to_texts