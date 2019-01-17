import org.junit.Assert.assertEquals
import org.junit.Test
//https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/


class VerifyPreorderSerializationofaBinaryTree{
  fun isValidSerialization(preorder: String): Boolean {
    val str = preorder.split(",")
    val n = str.size
    var i = 0
    fun dfs(): Boolean{
      if(i >= n )return false

      return if(str[i++] == "#")
        true
      else
        dfs() && dfs()
    }
    return dfs() && i == n
  }

  @Test
  fun test1(){
    assertEquals(true, isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))
  }

  @Test
  fun test2(){
    assertEquals(false, isValidSerialization("1,#"))
  }

  @Test
  fun test3(){
    assertEquals(false, isValidSerialization("9,#,#,1"))
  }

  @Test
  fun test4(){
    assertEquals(false, isValidSerialization(""))
  }

  @Test
  fun test5(){
    assertEquals(true, isValidSerialization("#"))
  }
}