from lib.includes_todo import *

def test_returns_false_if_empty_string():
    actual = includes_todo("")
    expected = False
    assert actual == expected

def test_returns_true_if_todo_present():
    actual = includes_todo("#todo test")
    expected = True
    assert actual == expected 

def test_returns_false_if_todo_not_present():
    actual = includes_todo("test")
    expected = False
    assert actual == expected 

def test_returns_true_if_todo_present_at_end():
    actual = includes_todo("test #todo")
    expected = True
    assert actual == expected 

