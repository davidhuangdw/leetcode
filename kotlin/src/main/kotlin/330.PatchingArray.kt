import org.junit.Assert.assertEquals
import org.junit.Test
//https://leetcode.com/problems/patching-array/


class PatchingArray{
  fun minPatches(nums: IntArray, n: Int): Int {
    var ret = 0
    var cur = 0L
    var i = 0
    while(cur < n){
      if(i < nums.size && nums[i] <= cur+1)
        cur += nums[i++]
      else{
        ret ++
        cur += cur+1
      }
    }
    return ret
  }

  @Test
  fun test1(){
    assertEquals(1, minPatches(intArrayOf(1, 3), 6))
  }

  @Test
  fun test2(){
    assertEquals(2, minPatches(intArrayOf(1, 5, 10), 20))
  }

  @Test
  fun test3(){
    assertEquals(0, minPatches(intArrayOf(1, 2, 2), 5))
  }
}