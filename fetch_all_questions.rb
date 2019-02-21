
# usage:
#   ruby fetch_questions.rb
#   ruby fetch_questions.rb 900 1000

require_relative 'scripts/fetch_all_questions_job'
require_relative 'scripts/constants'


front_id_range = ARGV.empty? ? 0..FLOAT::INFINITY : ARGV[0].to_i..ARGV[1].to_i
cookie = DEFAULTS_CONFIG[:cookie]
FetchAllQuestionsJob.new(front_id_range: front_id_range, cookie: cookie).run

