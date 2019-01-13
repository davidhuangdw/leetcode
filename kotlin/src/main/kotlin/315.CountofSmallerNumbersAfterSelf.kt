import org.junit.Assert.assertEquals
import org.junit.Test
import java.util.*

//https://leetcode.com/problems/count-of-smaller-numbers-after-self/


class CountofSmallerNumbersAfterSelf{
  fun countSmaller(nums: IntArray): List<Int> {
    if(nums.isEmpty()) return emptyList()

    val n = nums.size
    val ret = (0 until n).map{0}.toMutableList()
    fun sort(inds: List<Int>): List<Int>{
      if(inds.size <= 1) return inds
      val m = inds.size/2
      val l = sort(inds.subList(0, m))
      val r = sort(inds.subList(m, inds.size))

      val res = mutableListOf<Int>()
      var (i, j) = 0 to 0
      while(i < l.size || j < r.size) {
        if(i < l.size && (j >= r.size || nums[r[j]] >= nums[l[i]])){
          ret[l[i]] += j
          res.add(l[i++])
        } else
          res.add(r[j++])
      }
      return res
    }
    sort((0 until n).toList())
    return ret
  }

  @Test
  fun test1(){
    assertEquals(listOf(2,1,1,0), countSmaller(intArrayOf(5,2,6,1)))
  }

  @Test
  fun test2(){
    assertEquals(listOf(2,0,0), countSmaller(intArrayOf(2,0,1)))
  }

}