import org.junit.Assert.assertEquals
import org.junit.Test
import java.util.*

//https://leetcode.com/problems/find-median-from-data-stream/


class FindMedianfromDataStream{
  /** initialize your data structure here. */
  val lque = PriorityQueue<Int>(reverseOrder())
  val rque = PriorityQueue<Int>()

  fun addNum(num: Int) {
    if(lque.isEmpty() || num <= lque.peek()) {
      lque.add(num)
      if(lque.size - rque.size > 1)
        rque.add(lque.poll())
    }else{
      rque.add(num)
      if(rque.size > lque.size)
        lque.add(rque.poll())
    }
  }

  fun findMedian(): Double = if(lque.size == rque.size) (lque.peek()+rque.peek())/2.0 else lque.peek()*1.0


  // todo: for condensed case e.g. among 1-100, use count_hash & linkedlist

  companion object {
    const val PRECISION = 1e-9
  }

  @Test
  fun test1(){
    addNum(1)
    addNum(2)
    assertEquals(1.5, findMedian(), PRECISION)
    addNum(3)
    assertEquals(2.0, findMedian(), PRECISION)
  }
}