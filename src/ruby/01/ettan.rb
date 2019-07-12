# This comment was intentianlly left blank
class EulerOne
  def divisible_by_tree_and_five(number)
    (number % 3).zero? || (number % 5).zero?
  end

  def sum_divisible_one_and_fives(max)
    1.upto(max).map { |i| i if divisible_by_tree_and_five(i) }
     .compact
     .reduce { |sum, i| sum + i }
  end
end
