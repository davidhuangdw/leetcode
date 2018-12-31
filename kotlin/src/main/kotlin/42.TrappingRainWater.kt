import org.junit.Assert.assertEquals
import org.junit.Test

//https://leetcode.com/problems/trapping-rain-water/

class TrappingRainWater {
  fun trap(height: IntArray): Int {
    if(height.isEmpty()) return 0

    var sum = 0
    val k = height.withIndex().maxBy{it.value}!!.index

    var max = height.first()
    for(i in 1 until k)
      if(height[i] > max)
        max = height[i]
      else
        sum += max-height[i]

    max = height.last()
    for(i in height.size-1 downTo k+1)
      if(height[i] > max)
        max = height[i]
      else
        sum += max - height[i]

    return sum
  }

  @Test
  fun test1(){
    assertEquals(6, trap(intArrayOf(0,1,0,2,1,0,1,3,2,1,2,1)))
  }

  @Test
  fun test2(){
    assertEquals(9, trap(intArrayOf(4,2,0,3,2,5)))
  }
}