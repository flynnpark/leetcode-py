from . import MyHashMap


def test_solution():
    my_hash_map = MyHashMap()
    assert my_hash_map.put(1, 1) is None
    # 3 The map is now [[1,1]]
    assert my_hash_map.put(2, 2) is None
    # The map is now [[1,1], [2,2]]
    assert my_hash_map.get(1) is 1
    # return 1, The map is now [[1,1], [2,2]]
    assert my_hash_map.get(3) is -1
    # return -1 (i.e., not found), The map is now [[1,1], [2,2]]
    assert my_hash_map.put(2, 1) is None
    # The map is now [[1,1], [2,1]] (i.e., update the existing value)
    assert my_hash_map.get(2) is 1
    # return 1, The map is now [[1,1], [2,1]]
    assert my_hash_map.remove(2) is None
    # remove the mapping for 2, The map is now [[1,1]]
    assert my_hash_map.get(2) is -1
    # return -1 (i.e., not found), The map is now [[1,1]]
