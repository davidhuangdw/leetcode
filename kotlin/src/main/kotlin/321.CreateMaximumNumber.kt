import org.junit.Assert.assertEquals
import org.junit.Test
//https://leetcode.com/problems/create-maximum-number/


import java.util.*
class CreateMaximumNumber{
  fun maxNumber(nums1: IntArray, nums2: IntArray, k: Int): IntArray {

    fun largestSub(nums: IntArray, maxSize: Int): List<Int>{
      val cur = Stack<Int>()
      var ndrops = nums.size - maxSize
      for(v in nums){
        while(ndrops > 0 && cur.isNotEmpty() && cur.peek() < v) {
          cur.pop()
          ndrops --
        }
        cur.push(v)
      }
      return cur.slice(0 until maxSize)
    }

    fun compare(a: List<Int>, b: List<Int>): Int{
      val i = (0 until minOf(a.size, b.size)).find{ a[it] != b[it]}
      return if(i == null) a.size - b.size else a[i] - b[i]
    }

    fun merge(nums1: List<Int>, nums2: List<Int>): List<Int>{     // is there O(n) solution?
      val (n, m) = nums1.size to nums2.size
      var (i, j) = 0 to 0
      val ret = mutableListOf<Int>()
      while(i < n && j < m){
        if(compare(nums1.subList(i, n), nums2.subList(j, m)) >= 0)
          ret.add(nums1[i++])
        else
          ret.add(nums2[j++])
      }
      return ret + nums1.subList(i, n) + nums2.subList(j, m)
    }

    val (n, m) =  nums1.size to nums2.size
    var ret = listOf<Int>()
    for(i in maxOf(k-m,0)..minOf(k,n)){
      val mg = merge(largestSub(nums1, i), largestSub(nums2, k-i))
      if(compare(mg, ret) > 0)
        ret = mg
    }
    return ret.toIntArray()
  }

  @Test
  fun test1(){
    assertEquals(listOf(9, 8, 6, 5, 3), maxNumber(
        intArrayOf(3, 4, 6, 5), intArrayOf(9, 1, 2, 5, 8, 3), 5
    ).toList())
  }

  @Test
  fun test2(){
    assertEquals(listOf(6, 7, 6, 0, 4), maxNumber(
        intArrayOf(6, 7), intArrayOf(6, 0, 4), 5
    ).toList())
  }

  @Test
  fun test3(){
    assertEquals(listOf(9, 8, 9), maxNumber(
        intArrayOf(3, 9), intArrayOf(8, 9), 3
    ).toList())
  }

  @Test
  fun test4(){
    assertEquals(listOf<Int>(9,9,9,9,9,9,9,7,8,7,6,1,7,2,7,5,5,1,5,2,5,7,1,0,4,3,8,7,3,8,5,3,8,3,4,0,2,3,8,2,7,1,2,3,8,7,6,7,1,1,3,9,0,5,2,8,2,8,7,5,0,8,0,7,2,8,5,6,5,9,5,1,5,2,6,2,4,9,9,7,6,5,7,9,2,8,8,3,5,9,5,1,8,8,4,6,6,3,8,4,6,6,1,3,4,1,6,7,0,8,0,3,3,1,8,2,2,4,5,7,3,7,7,4,3,7,3,0,7,3,0,9,7,6,0,3,0,3,1,5,1,4,5,2,7,6,2,4,2,9,5,5,9,8,4,2,3,6,1,9),
        maxNumber(
        intArrayOf(3,3,3,2,3,7,3,8,6,0,5,0,7,8,9,2,9,6,6,9,9,7,9,7,6,1,7,2,7,5,5,1),
        intArrayOf(5,6,4,9,6,9,2,2,7,5,4,3,0,0,1,7,1,8,1,5,2,5,7,0,4,3,8,7,3,8,5,3,8,3,4,0,2,3,8,2,7,1,2,3,8,7,6,7,1,1,3,9,0,5,2,8,2,8,7,5,0,8,0,7,2,8,5,6,5,9,5,1,5,2,6,2,4,9,9,7,6,5,7,9,2,8,8,3,5,9,5,1,8,8,4,6,6,3,8,4,6,6,1,3,4,1,6,7,0,8,0,3,3,1,8,2,2,4,5,7,3,7,7,4,3,7,3,0,7,3,0,9,7,6,0,3,0,3,1,5,1,4,5,2,7,6,2,4,2,9,5,5,9,8,4,2,3,6,1,9),
        160
    ).toList())
  }

}