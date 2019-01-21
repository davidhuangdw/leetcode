import org.junit.Assert.assertEquals
import org.junit.Test
import java.util.*

//https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/


class InsertDeleteGetRandomDuplicatesallowed{
  class RandomizedCollection() {

    /** Initialize your data structure here. */
    val indexes = HashMap<Int, HashSet<Int>>()//.withDefault { HashSet() }
    val values = Stack<Int>()
    val rand = Random()

    /** Inserts a value to the collection. Returns true if the collection did not already contain the specified element. */
    fun insert(v: Int): Boolean {
      val set = indexes.getOrPut(v){ HashSet() }
      val notExist = set.isEmpty()
      set.add(values.size)
      values.add(v)
      return notExist
    }

    /** Removes a value from the collection. Returns true if the collection contained the specified element. */
    fun remove(v: Int): Boolean {
      val set = indexes.getOrPut(v){ HashSet() }
      if(set.isEmpty())
        return false

      val last = values.pop()
      val lastSet = indexes.getOrPut(last){ HashSet() }
      lastSet.remove(values.size)
      if(last != v){
        val i = set.first()
        set.remove(i)
        values[i] = last
        lastSet.add(i)
      }
      return true
    }

    /** Get a random element from the collection. */
    fun getRandom(): Int {
      return values[rand.nextInt(values.size)]
    }
  }


  private val collection = RandomizedCollection()
  @Test
  fun test1(){
    assertEquals(true, collection.insert(1))
    assertEquals(false, collection.insert(1))
    assertEquals(true, collection.insert(2))
    assertEquals(true, collection.getRandom() in listOf(1,2))
    assertEquals(false, collection.remove(9))
    assertEquals(true, collection.remove(1))
    assertEquals(true, collection.remove(2))
    assertEquals(true, collection.getRandom() in listOf(1))
  }


}