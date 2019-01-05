import org.junit.Assert.assertEquals
import org.junit.Test
import java.util.*

//https://leetcode.com/problems/min-stack/


class MinStack{
  private val mins = Stack<Int>()
  private val values = Stack<Int>()

  fun push(x: Int) {
    if(mins.empty() || x <= mins.peek())
      mins.push(x)
    values.push(x)
  }

  fun pop(): Int {
    val v = values.pop()
    if(mins.peek() == v) mins.pop()
    return v
  }

  fun top(): Int = values.peek()

  fun getMin() = mins.peek()

  @Test
  fun test1(){
    push(-2)
    push(0)
    push(-3)
    assertEquals(-3, getMin())
    pop()
    assertEquals(0, top())
    assertEquals(-2, getMin())
  }
}