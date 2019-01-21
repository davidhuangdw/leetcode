import org.junit.Assert.assertEquals
import org.junit.Test
import java.util.*

//https://leetcode.com/problems/insert-delete-getrandom-o1/


class InsertDeleteGetRandom{
  class RandomizedSet() {
    /** Initialize your data structure here. */
    val indexMap = HashMap<Int, Int>()
    val values = Stack<Int>()
    val rand = Random()

    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    fun insert(v: Int): Boolean {
      if(indexMap.containsKey(v))
        return false
      values.add(v)
      indexMap[v] = values.size-1
      return true
    }

    /** Removes a value from the set. Returns true if the set contained the specified element. */
    fun remove(v: Int): Boolean {
      if(!indexMap.containsKey(v))
        return false
      val i = indexMap.remove(v)!!
      val last = values.pop()
      if(v != last){
        values[i] = last
        indexMap[last] = i
      }
      return true
    }

    /** Get a random element from the set. */
    fun getRandom(): Int {
      return values.get(rand.nextInt(values.size))
    }
  }

  private val randomSet = RandomizedSet()

  @Test
  fun test1(){
    assertEquals(true, randomSet.insert(1))
    assertEquals(false, randomSet.remove(2))
    assertEquals(true, randomSet.insert(2))
    assertEquals(true, randomSet.getRandom() in listOf(1,2))
    assertEquals(true, randomSet.remove(1))
    assertEquals(false, randomSet.insert(2))
    assertEquals(true, randomSet.getRandom() in listOf(2))
  }

}