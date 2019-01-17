import org.junit.Assert.assertEquals
import org.junit.Test
//https://leetcode.com/problems/reconstruct-itinerary/
import java.util.*


class ReconstructItinerary{
  fun findItinerary(tickets: Array<Array<String>>): List<String> {
    tickets.sortWith(compareByDescending{it[1]})
    val nexts = HashMap<String, Stack<String>>()
    for((fr, to) in tickets){
      if(nexts[fr] == null)
        nexts[fr] = Stack()
      nexts[fr]!!.add(to)
    }

    val ret = mutableListOf<String>()
    fun dfs(node: String){
      while(nexts.getOrDefault(node, Stack()).isNotEmpty())
        dfs(nexts[node]!!.pop())          // smaller first
      ret.add(node)     //reverse order
    }
    dfs("JFK")
    return ret.reversed()
  }

  @Test
  fun test1(){
    assertEquals(listOf("JFK", "MUC", "LHR", "SFO", "SJC"), findItinerary(arrayOf(
        arrayOf("MUC", "LHR"),
        arrayOf("JFK", "MUC"),
        arrayOf("SFO", "SJC"),
        arrayOf("LHR", "SFO")
    )))
  }

  @Test
  fun test2(){
    assertEquals(listOf("JFK","NRT","JFK","KUL"), findItinerary(arrayOf(
        arrayOf("JFK", "KUL"),
        arrayOf("JFK", "NRT"),
        arrayOf("NRT", "JFK")
    )))
  }

}