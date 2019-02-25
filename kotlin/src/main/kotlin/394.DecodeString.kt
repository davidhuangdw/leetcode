import org.junit.Assert.assertEquals
import org.junit.Test
import java.lang.StringBuilder
import java.util.*

// https://leetcode.com/problems/decode-string


class DecodeString {
  fun decodeString(s: String): String {
    var cur = StringBuilder()
    var num = StringBuilder()
    val digits = "0123456789".toSet()
    val stack = Stack<Pair<StringBuilder, StringBuilder>>()
    for(ch in s)
      when(ch){
        '[' -> {
          stack.push(cur to num)
          cur = StringBuilder()
          num = StringBuilder()
        }
        ']' -> {
          val sub = cur
          val last = stack.pop()
          cur = last.first
          cur.append(sub.repeat(last.second.toString().toInt()))
          num.setLength(0)
        }
        in digits -> num.append(ch)
        else -> cur.append(ch)
      }
    return cur.toString()
  }

  @Test
  fun test1(){
    assertEquals("aaabcbc", decodeString("3[a]2[bc]"))
  }

  @Test
  fun test2(){
    assertEquals("accaccacc", decodeString( "3[a2[c]]"))
  }

  @Test
  fun test3(){
    assertEquals("abcabccdcdcdef", decodeString("2[abc]3[cd]ef"))
  }


}

