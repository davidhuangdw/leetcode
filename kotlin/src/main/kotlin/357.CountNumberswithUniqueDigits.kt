import org.junit.Assert.assertEquals
import org.junit.Test
//https://leetcode.com/problems/count-numbers-with-unique-digits/


class CountNumberswithUniqueDigits{
  fun countNumbersWithUniqueDigits(n: Int): Int {
    val muls = listOf(9) + (9 downTo 1)
    var cnt = 1
    var mul = 1
    for(i in 0 until minOf(n, muls.size)){
      mul *= muls[i]
      cnt += mul
    }
    return cnt
  }

  @Test
  fun test1(){
    assertEquals(91, countNumbersWithUniqueDigits(2))
  }

  @Test
  fun test2(){
    assertEquals(10, countNumbersWithUniqueDigits(1))
  }
}