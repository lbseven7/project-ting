from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()

    # ENQUEUE
    priority_queue.enqueue({"qtd_linhas": 6})
    priority_queue.enqueue({"qtd_linhas": 4})
    assert len(priority_queue) == 2

    # DEQUEUE
    assert priority_queue.dequeue() == {"qtd_linhas": 4}
    assert priority_queue.dequeue() == {"qtd_linhas": 6}
    priority_queue.enqueue({"qtd_linhas": 4})
    priority_queue.enqueue({"qtd_linhas": 6})

    # SEARCH
    assert priority_queue.search(0) == {"qtd_linhas": 4}
    assert priority_queue.search(1) == {"qtd_linhas": 6}

    # ERROR
    with pytest.raises(IndexError):
        priority_queue.search(2)
