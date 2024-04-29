import unittest
from oop1 import Queue

class TestQueue(unittest.TestCase):

    def test_insert_and_pop(self):
        q = Queue()
        q.insert("hi")
        self.assertEqual(q.pop(), "hi")  

    def test_isEmpty(self):
        q = Queue()
        self.assertTrue(q.isEmpty())  
        q.insert("item")
        self.assertFalse(q.isEmpty())  

    def test_pop_empty_queue(self):
        q = Queue()
        with self.assertRaises(IndexError): 
            q.pop()

if __name__ == '__main__':
    unittest.main()
