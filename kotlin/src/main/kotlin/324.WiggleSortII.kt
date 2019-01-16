import org.junit.Assert.assertEquals
import org.junit.Test
//https://leetcode.com/problems/wiggle-sort-ii/


class WiggleSortII{
  fun wiggleSort(nums: IntArray): Unit {
    nums.sort()
    val n = nums.size
    val m = (n+1)/2
    val l = nums.slice(0 until m)
    val r = nums.slice(m until n)
    for((i,v) in l.reversed().withIndex())
      nums[i*2] = v
    for((i,v) in r.reversed().withIndex())
      nums[i*2+1] = v
  }

  fun wiggled(nums: IntArray) = !(0 until nums.size-1 step 2).any{ nums[it] >= nums[it+1] }

  @Test
  fun test1(){
    val nums = intArrayOf(1,2,3,4,5)
    wiggleSort(nums)
    assert(wiggled(nums))
  }

  @Test
  fun test2(){
    val nums = intArrayOf(4,5,5,6)
    wiggleSort(nums)
    assert(wiggled(nums))
  }

}