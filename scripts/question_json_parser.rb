require 'json'

class QuestionJsonParser
  DATA_KEY = 'data'
  QUESTION_KEY = 'question'
  FRONT_QUESTION_ID_KEY = 'questionFrontendId'
  QUESTION_ID_KEY = 'questionId'
  QUESTION_TITLE_SLUG_KEY = 'titleSlug'
  CODE_SNIPPETS_KEY = 'codeSnippets'
  LANG_SLUG_KEY = 'langSlug'
  CODE_KEY = 'code'
  LIKES_KEY = 'likes'
  DISLIKES_KEY = 'dislikes'
  DIFFICULTY_KEY = 'difficulty'
  PAID_ONLY_KEY = 'isPaidOnly'
  COMPANY_STATS_KEY = 'companyTagStats'

  attr_accessor :metadata

  def initialize(question_json_body)
    self.metadata = question_json_body
  end

  def general_info
    {}.tap do |h|
      %w[id front_id title difficulty likes dislikes paid_only]
          .each{|key| h[key] = send(key)}
    end
  end

  def front_id
    question[FRONT_QUESTION_ID_KEY]
  end

  def title
    question[QUESTION_TITLE_SLUG_KEY]
  end

  def id
    question[QUESTION_ID_KEY]
  end

  def code_snippets
    question[CODE_SNIPPETS_KEY]
  end

  def likes
    question[LIKES_KEY]
  end

  def dislikes
    question[DISLIKES_KEY]
  end

  def paid_only
    question[PAID_ONLY_KEY]
  end

  def difficulty
    question[DIFFICULTY_KEY]
  end

  def company_stats
    JSON.parse question[COMPANY_STATS_KEY] if question[COMPANY_STATS_KEY]
  end

  def code_snippet(lang_slug)
    snippet = code_snippets.find{|s| s[LANG_SLUG_KEY].to_s == lang_slug.to_s}
    snippet && snippet[CODE_KEY]
  end

  def source_file_name(separator: '.', suffix:, **opt)
    suffix = '.' + suffix unless suffix[0] == '.'
    [front_id, camelized_title].join(separator) + suffix
  end

  def camelized_title
    title.split('-').map{|s| s.capitalize}.join
  end

  def question
    metadata[DATA_KEY][QUESTION_KEY]
  end

  def metadata=(metadata)
    @metadata = metadata.is_a?(String) ? JSON.parse(metadata) : metadata.to_hash unless metadata.nil?
  end

  alias question_body metadata
  alias question_body= metadata=
  alias source= metadata=

end
