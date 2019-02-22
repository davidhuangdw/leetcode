require 'fileutils'
require_relative 'constants'

class ProblemsFileWriter
  class <<self
    def mkdir_if_absent(dir)
      FileUtils.mkpath(dir) unless File.exist?(dir)
    end

    def save(text, path)
      mkdir_if_absent File.dirname(path)
      File.write(path, text)
      puts "----saved: #{path}"
    end
  end

  attr_accessor :parser, :root_dir, :question_subdir, :solution_subdir, :company_subdir,
                :problem_list_filename, :overwrite_existing_question
  def initialize(parser: nil,
                 root_dir: DEFAULTS_CONFIG[:root_dir],
                 question_subdir: DEFAULTS_CONFIG[:question_subdir],
                 solution_subdir: DEFAULTS_CONFIG[:solution_subdir],
                 company_subdir: DEFAULTS_CONFIG[:company_subdir],
                 problem_list_filename: DEFAULTS_CONFIG[:problem_list_filename],
                 overwrite_existing_question: DEFAULTS_CONFIG[:overwrite_existing_question]
                 )
    @parser = parser
    @root_dir = root_dir
    @question_subdir = question_subdir
    @solution_subdir = solution_subdir
    @company_subdir = company_subdir
    @problem_list_filename = problem_list_filename
    @overwrite_existing_question = overwrite_existing_question
  end

  def read_problems_list_file
    File.read(problem_list_file_path)
  end

  def read_company_file(company)
    File.read(company_file_path(company)) if File.exist?(company_file_path(company))
  end

  def search_question_file(slug_title)
    Dir[File.join(root_dir, question_subdir, "*.#{slug_title}")]
  end

  def save_problems_list_file(text)
    klass.save(text, problem_list_file_path) # always overwrite here
  end

  def save_company_file(text, company:)
    klass.save(text, company_file_path(company)) # always overwrite company info
  end

  def save_question_file(text)
    save(text, question_file_path)
  end

  def save_solution_file(text)
    save(text, solution_file_path)
  end

  def problem_list_file_path
    File.join(root_dir, problem_list_filename)
  end

  def question_file_path
    File.join(root_dir, question_subdir, question_file_name)
  end

  def solution_file_path
    File.join(root_dir, solution_subdir, solution_file_name)
  end

  def company_file_path(company)
    File.join(root_dir, company_subdir, company)
  end

  def question_file_name
    [parser.front_id, parser.id, parser.title].join('.')
  end

  def solution_file_name
    question_file_name + '.solution'
  end

  def question_dir
    File.join(root_dir, question_subdir)
  end

  def company_dir
    File.join(root_dir, company_subdir)
  end

  private

  def save(text, file_path)
    if File.exist?(file_path) && !overwrite_existing_question
      puts "----skipping: #{file_path}"
    else
      klass.save(text, file_path)
    end
  end

  def klass
    self.class
  end

end
