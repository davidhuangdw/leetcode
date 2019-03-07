import org.junit.Assert.assertEquals
import org.junit.Test
import java.util.*

// https://leetcode.com/problems/my-calendar-i


class MyCalendar() {
  val all = TreeSet<Pair<Int, Int>>(compareBy({it.first}, {it.second}))

  fun book(start: Int, end: Int): Boolean {
    val cur = start to end
    val l = all.floor(cur)
    if(l != null && l.second > start) return false
    val r = all.ceiling(cur)
    if(r != null && r.first < end) return false
    all.add(cur)
    return true
  }

}

class MyCalendarTests(){
  @Test
  fun test1(){
    val c = MyCalendar()
    assertEquals(true, c.book(10, 20))
    assertEquals(false, c.book(15, 25))
    assertEquals(true, c.book(20, 30))
  }
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * var obj = MyCalendar()
 * var param_1 = obj.book(start,end)
 */

