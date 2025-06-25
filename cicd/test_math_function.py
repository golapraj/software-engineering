from math_functions import add, sub

def test_add_numbers():
    assert add(2,2) == 4
    assert add(1,3) == 4
    assert add(1000,1000) == 2000
    assert add(-2,-2) == -4
    assert add(0.5,0.5) == 1.0
    assert add(-0.5,-0.5) == -1.0
    assert add(0.55, 0.55) == 1.1
    assert add(-0.55, 0.55) == 0.0
    assert add(1000000.5, 1000000.5) == 2000001.0
    for x in range(0,1000):
        for y in range(0,1000):
            assert add(x,y) == x + y
    # assert add(25.5, 45.0) == 70.5, f"result == {add(25.5, 45.0)}"

def test_sub_numbers():
    assert sub(2,2) == 0
    assert sub(7,3) == 4
    assert sub(2000,1000) == 1000
    assert sub(-2,2) == -4
    assert sub(1.0,0.5) == 0.5
    # assert sub(-0.5,-0.5) == -1.0
    # assert sub(0.55, 0.55) == 1.1
    # assert sub(-0.55, 0.55) == 0.0
    # assert sub(1000000.5, 1000000.5) == 2000001.0
    # for x in range(0,1000):
    #     for y in range(0,1000):
    #         assert sub(x,y) == x + y
    # assert sub(25.5, 45.0) == 70.5, f"result == {add(25.5, 45.0)}"
