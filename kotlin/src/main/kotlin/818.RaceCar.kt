import org.junit.Assert.assertEquals
import org.junit.Test
//https://leetcode.com/problems/race-car/


class RaceCar{
  val cache = HashMap<Int, Int>()
  private fun cal(k: Int) = (1 shl k)-1
  fun racecar(target: Int): Int {
    if(target !in cache){
      var k = 1
      while(cal(k) < target) k++
      if(cal(k) == target) cache[target] = k
      else{
        var res = racecar(cal(k)-target)
        for(j in 0 until k-1)
          res = minOf(res, j+racecar(target-cal(k-1)+cal(j)))
        cache[target] = k+1+res
      }
    }
    return cache[target]!!
  }

  @Test
  fun test1(){
    assertEquals(2, racecar(3))
  }

  @Test
  fun test2(){
    assertEquals(5, racecar(6))
  }
}