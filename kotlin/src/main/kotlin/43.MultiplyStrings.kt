import org.junit.Assert.assertEquals
import org.junit.Test
// https://leetcode.com/problems/multiply-strings


class MultiplyStrings {
  fun multiply(num1: String, num2: String): String {
    if("0" in listOf(num1, num2)) return "0"

    fun digits(num: String) = num.map{it - '0'}.reversed()
    val res = IntArray(num1.length + num2.length)
    for((i, v1) in digits(num1).withIndex()){
      for((j, v2) in digits(num2).withIndex()){
        val sum = res[i+j] + v1*v2
        res[i+j+1] += sum/10
        res[i+j] = sum%10
      }
    }
    val i = (res.size-1 downTo 0).first{res[it] != 0}
    return res.slice(0 until i+1).reversed().joinToString("")
  }

  @Test
  fun test1(){
    assertEquals("6", multiply("2", "3"))
  }

  @Test
  fun test2(){
    assertEquals("56088", multiply("123", "456"))
  }

  @Test
  fun test3(){
    assertEquals("0", multiply("0", "0"))
  }
}

