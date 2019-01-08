import org.junit.Assert.assertEquals
import org.junit.Test
import java.util.*

//https://leetcode.com/problems/basic-calculator/submissions/

class BasicCalculator{
  fun calculate(s: String): Int {
    val stack = Stack<Pair<Int, Int>>()
    var sum = 0
    var num = 0
    var sign = 1
    for (ch in s) {
      when (ch) {
        in '0'..'9' -> num = num * 10 + ch.toInt() - '0'.toInt()
        in "+-" -> {
          sum += sign * num
          num = 0
          sign = if (ch == '+') 1 else -1
        }
        '(' -> {
          stack.push(sum to sign)
          sum = 0
          sign = 1
        }
        ')' -> {
          sum += sign * num
          val (lsum, lsign) = stack.pop()
          sum = lsum + sum * lsign
          num = 0
        }
      }
    }
    return sum + num * sign
  }

  @Test
  fun test1(){
    assertEquals(2, calculate("1+1"))
  }

  @Test
  fun test2(){
    assertEquals(3, calculate("2-1 + 2 "))
  }

  @Test
  fun test3(){
    assertEquals(23, calculate("(1+(4+5+2)-3)+(6+8)"))
  }

  @Test
  fun test4(){
    assertEquals(2, calculate("1 - (2-3)"))
  }
}