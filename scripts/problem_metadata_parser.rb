require 'json'

class ProblemMetadataParser
  PROBLEM_LIST_KEY = 'stat_status_pairs'
  STAT_KEY = 'stat'
  FRONT_QUESTION_ID_KEY = 'frontend_question_id'
  QUESTION_ID_KEY = 'question_id'
  QUESTION_TITLE_SLUG_KEY = 'question__title_slug'

  class <<self
    def decode_problem_metadata_list(problems_body)
      hashed = problems_body.is_a?(String) ? JSON.parse(problems_body) : problems_body.to_hash
      hashed[PROBLEM_LIST_KEY]
    end
  end

  attr_accessor :metadata

  def initialize(metadata)
    self.metadata = metadata
  end

  def front_id
    stat[FRONT_QUESTION_ID_KEY]
  end

  def title
    stat[QUESTION_TITLE_SLUG_KEY]
  end

  def id
    stat[QUESTION_ID_KEY]
  end

  def stat
    metadata[STAT_KEY]
  end

  alias source= metadata=

end
