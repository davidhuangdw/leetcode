module CodeSnippetBuilder
  SOLUTION_CLASS_NAME = 'Solution'

  def self.build(snippet, class_name:, comment:, comment_prefix:,  front_lines:, **opt)
    front_lines + "\n" +
        comment.split("\n").map{|s| comment_prefix + ' ' + s}.join('\n') +
        "\n\n" +
        snippet.sub(SOLUTION_CLASS_NAME, class_name) +
        "\n"
  end
end
