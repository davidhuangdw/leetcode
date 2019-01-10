import org.junit.Assert.assertEquals
import org.junit.Test
//https://leetcode.com/problems/expression-add-operators/


class ExpressionAddOperators{
  fun addOperators(num: String, target: Int): List<String> {
    val n = num.length
    val ret = mutableListOf<String>()

    fun dfs(i: Int, v: Long, last: Long, exp: String){
      if(i == n){
        if(v+last == target.toLong()) ret.add(exp)
        return
      }
      for(j in i+1..n){
        if(num[i] == '0' && j-i > 1) break

        val cur = num.substring(i, j)
        val curv = cur.toBigInteger().toLong()
        if(i == 0)
          dfs(j, v, curv, cur)
        else{
          dfs(j, v+last, curv, "$exp+$cur")
          dfs(j, v+last, -curv, "$exp-$cur")
          dfs(j, v, last*curv, "$exp*$cur")
        }
      }
    }
    dfs(0, 0, 0, "")
    return ret
  }

  @Test
  fun test1(){
    assertEquals(setOf("1+2+3", "1*2*3"), addOperators("123", 6).toSet())
  }

  @Test
  fun test2(){
    assertEquals(setOf("2*3+2", "2+3*2"), addOperators("232", 8).toSet())
  }

  @Test
  fun test3(){
    assertEquals(setOf("1*0+5", "10-5"), addOperators("105", 5).toSet())
  }

  @Test
  fun test4(){
    assertEquals(setOf("0+0", "0-0", "0*0"), addOperators("00", 0).toSet())
  }

  @Test
  fun test5(){
    assertEquals(setOf<String>(), addOperators("3456237490", 9191).toSet())
  }

}