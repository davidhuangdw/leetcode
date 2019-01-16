import org.junit.Assert.assertEquals
import org.junit.Test
//https://leetcode.com/problems/count-of-range-sum/


class CountofRangeSum{
  fun countRangeSum(nums: IntArray, lower: Int, upper: Int): Int {
    val sums = mutableListOf(0L)
    for(v in nums) sums.add(v + sums.last())

    var count = 0
    fun sort(sub: List<Long>): List<Long>{
      if(sub.size <= 1) return sub
      val hf = sub.size/2
      val l = sort(sub.subList(0, hf))
      val r = sort(sub.subList(hf, sub.size))
      val m = r.size

      var j = 0
      var k = 0
      var t = 0
      val sorted = mutableListOf<Long>()
      for(v in l){
        while(j < m && r[j] - v < lower) j ++
        while(k < m && r[k] - v <= upper) k ++
        while(t < m && r[t] <= v) sorted.add(r[t++])
        sorted.add(v)
        count += maxOf(0, k-j)
      }
      return sorted + r.subList(t, m)
    }

    sort(sums)
    return count
  }

  @Test
  fun test1(){
    assertEquals(3, countRangeSum(intArrayOf(-2,5,-1), -2, 2))
  }

  @Test
  fun test2(){
    assertEquals(7, countRangeSum(intArrayOf(-3,1,2,-2,2,-1), -3, -1))
  }

  @Test
  fun test3(){
    assertEquals(0, countRangeSum(intArrayOf(), 0, 0))
  }
}