import org.junit.Assert.assertEquals
import org.junit.Test
//https://leetcode.com/problems/bricks-falling-when-hit/


class BricksFallingWhenHit{
  fun hitBricks(grid: Array<IntArray>, hits: Array<IntArray>): IntArray {
    for(k in 0 until hits.size){
      val (i, j) = hits[k]
      if(grid[i][j] == 1)
        grid[i][j] = 0
      else
        hits[k] = intArrayOf(-1, -1)
    }

    // disjoint
    val root = hashMapOf<Pair<Int, Int>, Pair<Int, Boolean>>() //value: size to isTop
    val parent = hashMapOf<Pair<Int, Int>, Pair<Int, Int>>()
    fun find(pos: Pair<Int, Int>): Pair<Int, Int>{
      if(parent[pos] == pos) return pos
      parent[pos] = find(parent[pos]!!)
      return parent[pos]!!
    }
    fun union(a: Pair<Int, Int>, b: Pair<Int, Int>){
      val (ra, rb) = find(a) to find(b)
      val (sa, ta) = root[ra]!!
      val (sb, tb) = root[rb]!!
      parent[rb] = ra
      root[ra] = (sa+sb) to (ta || tb)
    }
    fun create(pos: Pair<Int, Int>){
      parent[pos] = pos
      root[pos] = 1 to (pos.first == 0)
    }

    val (n, m) = grid.size to grid[0].size
    for(i in 0 until n)
      for(j in 0 until m)
        if(grid[i][j] == 1) {
          create(i to j)
          if(i-1>=0 && grid[i-1][j] == 1)
            union(i-1 to j, i to j)
          if(j-1>=0 && grid[i][j-1] == 1)
            union(i to j-1, i to j)
        }

    // reverse
    val inc = mutableListOf<Int>()
    for((i, j) in hits.reversed()){
      if(i < 0){
        inc.add(0)
        continue
      }
      create(i to j)
      grid[i][j] = 1
      var nonTop = 0
      for((ni, nj) in listOf(listOf(i-1,j), listOf(i+1,j), listOf(i,j-1), listOf(i, j+1))){
        if(ni in 0 until n && nj in 0 until m && grid[ni][nj] == 1 && find(ni to nj) != find(i to j)){
          val (size, top) = root[find(ni to nj)]!!
          if(!top) nonTop += size
          union(ni to nj, i to j)
        }
      }
      inc.add(if(root[find(i to j)]!!.second) nonTop else 0)
    }
    return inc.reversed().toIntArray()
  }

  @Test
  fun test0(){
    assertEquals(listOf(1, 0, 1, 0, 0), hitBricks(
        arrayOf(intArrayOf(1), intArrayOf(1), intArrayOf(1), intArrayOf(1), intArrayOf(1)),
        arrayOf(intArrayOf(3,0), intArrayOf(4,0), intArrayOf(1,0), intArrayOf(2,0), intArrayOf(0,0))
    ).toList())
  }

  @Test
  fun test1(){
    assertEquals(listOf(2), hitBricks(
        arrayOf(intArrayOf(1,0,0,0), intArrayOf(1,1,1,0)),
        arrayOf(intArrayOf(1,0))
    ).toList())
  }

  @Test
  fun test2(){
    assertEquals(listOf(0,0), hitBricks(
        arrayOf(intArrayOf(1,0,0,0), intArrayOf(1,1,0,0)),
        arrayOf(intArrayOf(1,1), intArrayOf(1,0))
    ).toList())
  }
}