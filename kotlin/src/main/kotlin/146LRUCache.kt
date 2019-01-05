import org.junit.Assert.assertEquals
import org.junit.Test

//https://leetcode.com/problems/lru-cache/

class Node(
    var key: Int = 0,
    var value: Int = 0,
    var prev: Node? = null,
    var next: Node? = null
){
  fun remove(): Node{
    prev?.next = next
    next?.prev = prev
    next = null
    prev = null
    return this
  }

  fun insert(node: Node): Node{
    node.next = next
    node.prev = this
    next?.prev = node
    next = node
    return node
  }
}

class LRUCache(val capacity: Int){
  var count = 0
  val hash: HashMap<Int, Node> = HashMap()
  val head = Node()
  val tail = head.insert(Node())

  fun get(key: Int): Int {
    if(!hash.containsKey(key)) return -1

    val node = hash[key]!!
    shiftUp(node)
    return node.value
  }

  fun put(key: Int, value: Int): Int{
    if(hash.containsKey(key))
      hash[key]!!.value = value
    else{
      val node = Node(key, value)
      if(count == capacity) pop()
      head.insert(node)
      hash[key] = node
      count ++
    }

    return get(key)
  }

  private fun pop(): Node?{
    if(count == 0) return null

    val node = tail.prev!!.remove()
    hash.remove(node.key)
    count --
    return node
  }

  private fun shiftUp(node: Node): Node{
    if(head.next != node){
      node.remove()
      head.insert(node)
    }
    return node
  }
}

class Tests{
  fun toList(cache: LRUCache): List<Int>{
    val list = mutableListOf<Int>()
    var node = cache.head.next
    while(node != null){
      list.add(node.value)
      node = node.next
    }
    return list.subList(0, list.lastIndex)
  }

  @Test
  fun test(){
    val cache = LRUCache(2)
    cache.put(1, 100)
    cache.put(2, 200)
    assertEquals(listOf(200, 100), toList(cache))
    assertEquals(100, cache.get(1))
    assertEquals(listOf(100, 200), toList(cache))

    assertEquals(100, cache.get(1))
    cache.put(3, 333)
    assertEquals(listOf(333, 100), toList(cache))
    cache.put(3, 300)
    assertEquals(listOf(300, 100), toList(cache))
    cache.put(4, 400)
    assertEquals(-1, cache.get(1))
    assertEquals(400, cache.get(4))
    assertEquals(300, cache.get(3))
  }
}