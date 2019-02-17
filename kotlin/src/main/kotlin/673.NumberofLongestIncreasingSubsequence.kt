import org.junit.Assert.assertEquals
import org.junit.Test
//https://leetcode.com/problems/number-of-longest-increasing-subsequence/


class NumberofLongestIncreasingSubsequence{
  class Node(val begin: Int, val end: Int){
    val md = begin + (end - begin)/2
    val left by lazy { Node(begin, md) }
    val right by lazy { Node(md+1, end) }
    var cur = 0 to 1

    fun merge(lenCount1: Pair<Int, Int>, lenCount2: Pair<Int, Int>): Pair<Int, Int>{
      val (l1, c1) = lenCount1
      val (l2, c2) = lenCount2
      if(l1 == l2) return l1 to (if(l1==0) 1 else c1+c2)
      return if(l1 < l2) lenCount2 else lenCount1
    }

    fun insert(num: Int, lenCount: Pair<Int, Int>){
      if(num < begin || end < num) return
      cur = if(begin == end)
        merge(cur, lenCount)
      else{
        if(num <= md) left.insert(num, lenCount)
        else right.insert(num, lenCount)
        merge(left.cur, right.cur)
      }
    }

    fun query(num: Int): Pair<Int, Int>{
      if(end <= num || begin == end) return cur
      if(num <= md) return left.query(num)
      return merge(left.cur, right.query(num))
    }
  }

  fun findNumberOfLIS(nums: IntArray): Int {
    val n = nums.size
    if(n == 0) return 0
    val min = nums.min()!!
    val root = Node(min, nums.max()!!)
    for(num in nums){
      val (len, count) = if(num == min) 0 to 1 else root.query(num-1)
      root.insert(num,len+1 to count)
    }
    return root.cur.second
  }

  @Test
  fun test0(){
    assertEquals(4, findNumberOfLIS(intArrayOf(4,3,2,1)))
  }

  @Test
  fun test1(){
    assertEquals(2, findNumberOfLIS(intArrayOf(1,3,5,4,7)))
  }

  @Test
  fun test2(){
    assertEquals(5, findNumberOfLIS(intArrayOf(2,2,2,2,2)))
  }
}