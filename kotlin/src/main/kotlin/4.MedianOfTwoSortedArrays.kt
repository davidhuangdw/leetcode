import org.junit.Assert.assertEquals
import org.junit.Test
// https://leetcode.com/problems/median-of-two-sorted-arrays


class MedianOfTwoSortedArrays {
  fun findMedianSortedArrays(a: IntArray, b: IntArray): Double {
    val (n, m) = a.size to b.size
    var k = (n+m+1)/2
    var (i, j) = 0 to 0
    while(k > 1) {
      val l = k/2
      val r = k - l
      val (pi, pj) = i+l-1 to j+r-1
      if(pj >= m || (pi<n && a[pi] <= b[pj])){
        k -= l
        i += l
      }else{
        k -= r
        j += r
      }
    }

    val v4 = (a.slice(i until minOf(n, i+2)) + b.slice(j until minOf(m, j+2))).sorted()
    return (v4[0]+v4[(n+m+1)%2])/2.0
  }


  @Test
  fun test1(){
    assertEquals(2.0, findMedianSortedArrays(intArrayOf(1,3), intArrayOf(2)), 1e-7)
  }

  @Test
  fun test2(){
    assertEquals(2.5, findMedianSortedArrays(intArrayOf(1,2), intArrayOf(3,4)), 1e-7)
  }

  @Test
  fun test3(){
    assertEquals(3.5, findMedianSortedArrays(intArrayOf(2,3,4,5), intArrayOf()), 1e-7)
  }


}

