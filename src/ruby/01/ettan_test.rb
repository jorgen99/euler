$LOAD_PATH.unshift(File.dirname(__FILE__))
require 'test/unit'
require('ettan')

class FrameTest < Test::Unit::TestCase

  def setup
    @one = EulerOne.new
  end

  def teardown; end

  def test_sum_up_to_ten
    assert_equal 23, @one.sum_divisible_one_and_fives(9)
  end

  def test_euler_one
    assert_equal 233168, @one.sum_divisible_one_and_fives(999)
  end

end
