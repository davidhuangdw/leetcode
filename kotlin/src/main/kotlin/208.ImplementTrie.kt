import org.junit.Assert.assertEquals
import org.junit.Test
//https://leetcode.com/problems/implement-trie-prefix-tree/

class ImplementTrie{
  class Node{
    var end = false
    val next = HashMap<Char, Node>()
  }
  /** Initialize your data structure here. */
  val root = Node()

  /** Inserts a word into the trie. */
  fun insert(word: String) {
    var node = root
    for(ch in word){
      if(!node.next.containsKey(ch))
        node.next[ch] = Node()
      node = node.next[ch]!!
    }
    node.end = true
  }

  private fun walk(word: String): Node?{
    var node = root
    for(ch in word){
      if(node.next.containsKey(ch))
        node = node.next[ch]!!
      else
        return null
    }
    return node
  }

  /** Returns if the word is in the trie. */
  fun search(word: String): Boolean {
    val node = walk(word)
    return node != null && node.end
  }

  /** Returns if there is any word in the trie that starts with the given prefix. */
  fun startsWith(prefix: String) = walk(prefix) != null

  @Test
  fun test1(){
    insert("apple")
    assert(search("apple"))
    assert(!search("app"))
    assert(startsWith("app"))
    insert("app")
    assert(search("app"))
  }
}