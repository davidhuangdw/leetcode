import org.junit.Assert.assertEquals
import org.junit.Test
import java.util.*

//https://leetcode.com/problems/redundant-connection-ii/


class RedundantConnectionII{
  fun findRedundantDirectedConnection(edges: Array<IntArray>): IntArray {
    val n = edges.size
    val ch = Array<MutableList<Int>>(n+1){ mutableListOf() }
    val parents = mutableMapOf<Int, MutableList<Int>>()
    var node = -1

    for(e in edges){
      val (fr, to) = e
      ch[fr].add(to)
      if(to in parents) {
        parents[to]!!.add(fr)
        node = to
      }else
        parents[to] = mutableListOf(fr)
    }

    val path = Stack<Int>()
    var cycle = setOf<Int>()
    val visited = mutableListOf<Int>()
    fun dfs(cur: Int){
      if(cycle.isNotEmpty()) return
      if(cur in visited) {
        val i = path.indexOf(cur)
        if(i >= 0)
          cycle = path.slice(i until path.size).toSet()
        return
      }
      visited.add(cur)
      path.add(cur)
      for(to in ch[cur])
        dfs(to)
      path.pop()
    }
    for(i in 1..n){
      if(i in visited) continue
      dfs(i)
    }

    if(node > 0){
      val ps = parents[node]!!
      for(p in ps)
        if(p in cycle)
          return intArrayOf(p, node)
      return intArrayOf(ps.last(), node)
    }

    var res = edges[0]
    for(e in edges){
      if(e[0] in cycle && e[1] in cycle)
        res = e
    }
    return res
  }

  @Test
  fun test1(){
    assertEquals(listOf(2,3), findRedundantDirectedConnection(arrayOf(
        intArrayOf(1,2),
        intArrayOf(1,3),
        intArrayOf(2,3)
    )).toList())
  }

  @Test
  fun test2(){
    assertEquals(listOf(4,1), findRedundantDirectedConnection(arrayOf(
        intArrayOf(1,2),
        intArrayOf(2,3),
        intArrayOf(3,4),
        intArrayOf(4,1),
        intArrayOf(1,5)
        )).toList())
  }

}