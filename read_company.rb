
# usage:
#   ruby read_company.rb google

require_relative 'scripts/questions'

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


raise "missing the argument - company_name" if ARGV.empty?
print_keys = %w[front_id difficulty encounters paid_only likes dislikes title]
list = Questions.new.read_company_list(ARGV[0]){|item| [item['encounters'], item['likes']] }
           .map{|item| print_keys.map{|key| item[key]}.join("\t") }

puts print_keys.join("\t")
puts list
