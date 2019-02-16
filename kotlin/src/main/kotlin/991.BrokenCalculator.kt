import org.junit.Assert.assertEquals
import org.junit.Test
//https://leetcode.com/problems/broken-calculator/


class BrokenCalculator{
  fun brokenCalc(X: Int, Y: Int): Int {
    var cnt = 0
    var y = Y
    while(y > X){
      if(y and 1 == 1){
        y += 1
        cnt ++
      }
      cnt ++
      y = y ushr 1
    }
    return cnt + X-y
  }

  @Test
  fun test1(){
    assertEquals(2, brokenCalc(2,3))
  }

  @Test
  fun test2(){
    assertEquals(2, brokenCalc(5,8))
  }

  @Test
  fun test3(){
    assertEquals(3, brokenCalc(3,10))
  }

  @Test
  fun test4(){
    assertEquals(1023, brokenCalc(1024,1))
  }
}