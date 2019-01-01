import org.junit.Assert.assertEquals
import org.junit.Test

//https://leetcode.com/problems/insert-interval/

class InsertInterva{
  fun insert(intervals: List<Interval>, newInterval: Interval): List<Interval> {
    val n = intervals.size
    val l = (0 until n).find{ intervals[it].end >= newInterval.start } ?: n
    val r = (n-1 downTo 0).find{ newInterval.end >= intervals[it].start } ?: -1

    if(l <= r) {
      newInterval.start = minOf(newInterval.start, intervals[l].start)
      newInterval.end = maxOf(newInterval.end, intervals[r].end)
    }

    val result = mutableListOf<Interval>()
    if(0<l) result.addAll(intervals.subList(0, l))
    result.add(newInterval)
    if(r+1<n) result.addAll(intervals.subList(r+1, n))
    return result
  }

  @Test
  fun test1(){
    assertEquals(listOf(1 to 5, 6 to 9), insert(listOf(
        Interval(1, 3),
        Interval(6, 9)
    ), Interval(2, 5)).map{ it.asPair() })
  }

  @Test
  fun test2(){
    assertEquals(listOf(1 to 2, 3 to 10, 12 to 16), insert(listOf(
        Interval(1, 2),
        Interval(3, 5),
        Interval(6, 7),
        Interval(8, 10),
        Interval(12, 16)
    ), Interval(4, 8)).map{ it.asPair() })
  }

}