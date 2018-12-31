import org.junit.Assert.assertEquals
import org.junit.Test
// https://leetcode.com/problems/generate-parentheses/

class GenerateParenthesis {
  fun generateParenthesis(n: Int): List<String> {
    val result = mutableListOf<String>()

    fun build(pre: String, nl: Int){
      if(pre.length == n+n)
        result.add(pre)
      else{
        if(nl < n)
          build(pre+'(', nl+1)
        if(nl > pre.length - nl)
          build(pre+')', nl)
      }
    }

    if(n > 0) build("", 0)
    return result
  }


  @Test
  fun test1(){
    assertEquals(listOf(
      "((()))",
      "(()())",
      "(())()",
      "()(())",
      "()()()"
    ), generateParenthesis(3))
  }
}