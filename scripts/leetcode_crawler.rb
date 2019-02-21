require 'json'
require 'faraday'

class LeetcodeCrawler
  def initialize(cookie=nil)
    puts "Warning: cookie value is empty, so it won't get premium data" unless cookie
    @cookie = cookie
    @client = Faraday.new
  end

  def fetch_problems
    url = 'https://leetcode.com/api/problems/algorithms/'
    @client.get(url).tap do |resp|
      puts resp.body
      raise "\nLeetcode API get_problems failed: #{resp.status}\n#{resp.body}" if error_resp?(resp)
    end
  end

  def fetch_question(title_slug)
    body = {
        operationName: 'questionData',
        variables: {titleSlug: title_slug},
        query: "query questionData($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    questionId\n    questionFrontendId\n    boundTopicId\n    title\n    titleSlug\n    content\n    translatedTitle\n    translatedContent\n    isPaidOnly\n    difficulty\n    likes\n    dislikes\n    isLiked\n    similarQuestions\n    contributors {\n      username\n      profileUrl\n      avatarUrl\n      __typename\n    }\n    langToValidPlayground\n    topicTags {\n      name\n      slug\n      translatedName\n      __typename\n    }\n    companyTagStats\n    codeSnippets {\n      lang\n      langSlug\n      code\n      __typename\n    }\n    stats\n    hints\n    solution {\n      id\n      canSeeDetail\n      __typename\n    }\n    status\n    sampleTestCase\n    metaData\n    judgerAvailable\n    judgeType\n    mysqlSchemas\n    enableRunCode\n    enableTestMode\n    envInfo\n    __typename\n  }\n}\n"
    }
    post_graphql(body)
  end

  def fetch_solution(title_slug)
    body = {
        operationName: 'QuestionNote',
        variables: {titleSlug: title_slug},
        query: "query QuestionNote($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    questionId\n    article\n    solution {\n      id\n      url\n      content\n      contentTypeId\n      canSeeDetail\n      rating {\n        id\n        count\n        average\n        userRating {\n          score\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"
    }
    post_graphql(body)
  end

  private

  def post_graphql(body)
    body = body.to_json unless body.is_a? String
    url = 'https://leetcode.com/graphql'
    headers = {
        'Content-Type' => 'application/json',
        'cookie' => @cookie
    }
    @client.post(url, body, headers).tap do |resp|
      raise "\nLeetcode API graphql failed: #{resp.status}\n#{resp.body}" if error_resp?(resp)
    end
  end

  def error_resp?(resp)
    resp.status != 200 || !resp.body['errors'].nil?
  end
end
