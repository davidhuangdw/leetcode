import org.junit.Assert.assertEquals
import org.junit.Test

//https://leetcode.com/problems/next-permutation/

class NextPermutation{
  fun nextPermutation(nums: IntArray): Unit {
    val lower = (nums.size-2 downTo 0).find{ nums[it] < nums[it+1] }

    if(lower != null){
      val k = (nums.size-1 downTo lower+1).find{ nums[it] > nums[lower] }!!
      swap(nums, lower, k)
    }
    var l=(lower ?: -1)+1
    var r=nums.size-1
    while(l < r)
      swap(nums, l++, r--)
  }

  private fun swap(nums: IntArray, i: Int, j: Int){
    val tmp = nums[i]
    nums[i] = nums[j]
    nums[j] = tmp
  }

  @Test
  fun test1(){
    val nums = intArrayOf(1,2,3)
    nextPermutation(nums)
    assertEquals(listOf(1,3,2), nums.toList())
  }

  @Test
  fun test2(){
    val nums = intArrayOf(3,2,1)
    nextPermutation(nums)
    assertEquals(listOf(1,2,3), nums.toList())
  }

  @Test
  fun test3(){
    val nums = intArrayOf(1,1,5)
    nextPermutation(nums)
    assertEquals(listOf(1,5,1), nums.toList())
  }

}

