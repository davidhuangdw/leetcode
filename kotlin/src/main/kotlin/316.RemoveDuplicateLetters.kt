import org.junit.Assert.assertEquals
import org.junit.Test
//https://leetcode.com/problems/remove-duplicate-letters/

import java.util.*
import kotlin.collections.HashMap

class RemoveDuplicateLetters{
  fun removeDuplicateLetters(s: String): String {
    val done = mutableSetOf<Char>()
    val count = HashMap<Char, Int>()
    for(c in s)
      count[c] = count.getOrDefault(c, 0) + 1

    val st = Stack<Char>()
    for(c in s){
      count[c] = count[c]!! - 1
      if(c in done)
        continue
      while(st.isNotEmpty() && count[st.peek()]!! > 0 && st.peek() > c)
        done.remove(st.pop())
      st.push(c)
      done.add(c)
    }
    return st.joinToString("")
  }

  fun removeDuplicateLetters1(s: String): String {
    fun bit(ch: Char) = 1 shl (ch.toInt() - 'a'.toInt())
    val n = s.length
    if(n == 0) return ""

    val combs = IntArray(n)
    val remain = mutableSetOf<Char>()
    for(i in n-1 downTo 0){
      val ch = s[i]
      remain.add(ch)
      combs[i] = (if(i==n-1) 0 else combs[i+1]) or bit(ch)
    }
    var least = combs[0]
    var (l,r) = 0 to 0

    return buildString {
      while(least > 0){
        while(r+1 < n && (least and combs[r+1]) == least)
          r++

        val mini = (l..r).filter { s[it] in remain }.minBy { s[it] }!!    // maybe use slide-window to achieve O(1)
        val ch = s[mini]

        append(ch)
        remain.remove(ch)
        least = least xor bit(ch)
        l = mini+1
      }
    }
  }

  @Test
  fun test1(){
    assertEquals("abc", removeDuplicateLetters("bcabc"))
  }

  @Test
  fun test2(){
    assertEquals("acdb", removeDuplicateLetters("cbacdcbc"))
  }

  @Test
  fun test3(){
    assertEquals("bac", removeDuplicateLetters("cbac"))
  }


}