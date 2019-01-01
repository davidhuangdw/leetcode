import org.junit.Assert.assertEquals
import org.junit.Test

//https://leetcode.com/problems/merge-intervals/

class MergeInterval{
  fun merge(intervals: List<Interval>): List<Interval> {
    val result = mutableListOf<Interval>()
    if(intervals.isEmpty()) return result

    val sorted =  intervals.sortedWith(compareBy({it.start}, {it.end}))
    var join = sorted.first()
    for(cur in sorted){
      if(cur.start <= join.end)
        join.end = maxOf(join.end, cur.end)
      else{
        result.add(join)
        join = cur
      }
    }
    result.add(join)
    return result
  }

  @Test
  fun test1(){
    assertEquals(listOf(1 to 6, 8 to 10, 15 to 18), merge(listOf(
        Interval(1, 3),
        Interval(2, 6),
        Interval(8, 10),
        Interval(15, 18)
    )).map{it.asPair()})
  }

  @Test
  fun test2(){
    assertEquals(listOf(1 to 5), merge(listOf(
        Interval(1, 4),
        Interval(4, 5)
    )).map{it.asPair()})
  }
}