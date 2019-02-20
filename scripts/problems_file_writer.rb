require 'fileutils'

class ProblemsFileWriter
  class <<self
    def mkdir_if_absent(dir)
      FileUtils.mkpath(dir) unless File.exist?(dir)
    end

    def save(text, path)
      mkdir_if_absent File.dirname(path)
      File.write(path, text)
    end
  end

  DEFAULT_ROOT_DIR = 'crawled'
  DEFAULT_QUESTION_SUBDIR = 'question_data'
  DEFAULT_SOLUTION_SUBDIR = 'solution_data'
  DEFAULT_PROBLEMS_FILE = 'problem_list'

  attr_accessor :root_dir, :question_subdir, :solution_subdir, :parser
  def initialize(parser,
                 root_dir: DEFAULT_ROOT_DIR,
                 question_subdir: DEFAULT_QUESTION_SUBDIR,
                 solution_subdir: DEFAULT_SOLUTION_SUBDIR)
    @parser = parser
    @root_dir = root_dir
    @question_subdir = question_subdir
    @solution_subdir = solution_subdir
  end

  def read_problems_list_file(fname = DEFAULT_PROBLEMS_FILE)
    File.read(File.join(root_dir, fname))
  end

  def save_problems_list_file(text, fname = DEFAULT_PROBLEMS_FILE)
    klass.save(text, File.join(root_dir, fname))
  end

  def save_question_file(text)
    klass.save(text, question_file_path)
  end

  def save_solution_file(text)
    klass.save(text, solution_file_path)
  end

  def question_file_path
    File.join(root_dir, question_subdir, question_file_name)
  end

  def solution_file_path
    File.join(root_dir, solution_subdir, solution_file_name)
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

  private

  def klass
    self.class
  end

end
