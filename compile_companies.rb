
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

end

CompileCompaniesJob.new(cookie: DEFAULTS_CONFIG[:cookie]).run