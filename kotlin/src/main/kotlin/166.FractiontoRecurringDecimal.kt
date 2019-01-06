import org.junit.Assert.assertEquals
import org.junit.Test

//https://leetcode.com/problems/fraction-to-recurring-decimal/

class FractiontoRecurringDecimal{
  fun fractionToDecimal(numerator: Int, denominator: Int): String {
    if(numerator == 0) return "0"

    var flag = 1
    var num = numerator.toLong()
    var den = denominator.toLong()
    if(num < 0) {
      flag *= -1
      num *= -1
    }
    if(den < 0) {
      flag *= -1
      den *= -1
    }

    val neg = if(flag == -1) "-" else ""
    val int = num/den
    var remain = num - int*den
    if(remain == 0L) return "${neg}${int}"

    val occur = HashMap<Long, Int>()
    val decimals = buildString {
      while(remain != 0L && !occur.containsKey(remain)){
        occur[remain] = length
        remain *= 10
        val mul = remain/den
        append(mul)
        remain -= mul*den
      }
    }

    return if(remain == 0L)
      "${neg}${int}.${decimals}"
    else
      "${neg}${int}.${decimals.substring(0, occur[remain]!!)}(${decimals.substring(occur[remain]!!)})"
  }

  @Test
  fun test1(){
    assertEquals("0.5", fractionToDecimal(1, 2))
  }

  @Test
  fun test2(){
    assertEquals("2", fractionToDecimal(2, 1))
  }

  @Test
  fun test3(){
    assertEquals("0.(6)", fractionToDecimal(2, 3))
  }

  @Test
  fun test4(){
    assertEquals("0.(012)", fractionToDecimal(4, 333))
  }

  @Test
  fun test5(){
    assertEquals("-2147483648", fractionToDecimal(-2147483648, 1))
  }
}