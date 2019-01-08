import org.junit.Assert.assertEquals
import org.junit.Test
//https://leetcode.com/problems/word-search-ii/

class WordSearchII{
  class Trie{
    class Node{
      val next = HashMap<Char, Node>()
      var end = false
    }
    val root = Node()

    fun insert(word: String){
      var node = root
      for(ch in word){
        if(!node.next.containsKey(ch))
          node.next[ch] = Node()
        node = node.next[ch]!!
      }
      node.end = true
    }
  }

  fun findWords(board: Array<CharArray>, words: Array<String>): List<String> {
    val trie = Trie()
    for(w in words)
      trie.insert(w)

    val result = HashSet<String>()
    val visited = HashSet<Pair<Int, Int>>()

    fun search(node: Trie.Node, i: Int, j: Int, pre: String){
      if(!(0<=i && i<board.size && 0<=j && j<board[i].size) || visited.contains(i to j))
        return
      val ch = board[i][j]
      val cur = pre+ch
      val nd =  node.next.get(ch)
      if(nd == null) return
      if(nd.end)
        result.add(cur)

      visited.add(i to j)
      for((ni, nj) in listOf(i to j+1, i+1 to j, i to j-1, i-1 to j))
        search(nd, ni, nj, cur)
      visited.remove(i to j)
    }

    for(i in 0 until board.size)
      for(j in 0 until board[i].size)
        search(trie.root, i, j, "")

    return result.toList()
  }

  @Test
  fun test1(){
    assertEquals(setOf("eat", "oath"), findWords(
        arrayOf(
            "oaan",
            "etae",
            "ihkr",
            "iflv"
        ).map{it.toCharArray()}.toTypedArray(),
        arrayOf("oath", "pea", "eat", "rain")
    ).toSet())
  }

  @Test
  fun test2(){
    assertEquals(listOf("a"), findWords(
        arrayOf(
            "a"
        ).map{it.toCharArray()}.toTypedArray(),
        arrayOf("a")
    ))
  }

  @Test
  fun test3(){
    assertEquals(listOf<String>(), findWords(
        arrayOf(
            "aa"
        ).map{it.toCharArray()}.toTypedArray(),
        arrayOf("aaa")
    ))
  }
}