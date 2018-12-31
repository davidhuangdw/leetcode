import org.junit.Assert.assertEquals
import org.junit.Test
import java.util.*

// https://leetcode.com/problems/valid-parentheses/

val TO_LEFT = mapOf(
    '}' to '{',
    ']' to '[',
    ')' to '('
)

class ValidParentheses {
  fun isValid(s: String): Boolean {
    if(s.length % 2 != 0) return false

    val lefts = Stack<Char>()
    for(ch in s)
      if(TO_LEFT.containsKey(ch)){
        if(lefts.empty() || lefts.pop() != TO_LEFT[ch])
          return false
      } else
        lefts.push(ch)

    return lefts.isEmpty()
  }


  @Test
  fun test1(){
    assertEquals(true, isValid("()"))
  }

  @Test
  fun test2(){
    assertEquals(true, isValid("()[]{}"))
  }

  @Test
  fun test3(){
    assertEquals(false, isValid("([)]"))
  }

  @Test
  fun test4(){
    assertEquals(true, isValid("{[()]}[]"))
  }
}