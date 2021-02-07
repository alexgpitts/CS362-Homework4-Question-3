import unittest
import full_name

class TestCase(unittest.TestCase):
    
    #check if it will return exact first string and second string separated by a space
    def test_my_name(self):
        self.assertEqual(full_name.get_full_name("Alex", "Pitts"), "Alex Pitts")

    #check if it will uppercase names
    def test_my_name_lower_case(self):
        self.assertEqual(full_name.get_full_name("alex", "pitts"), "Alex Pitts")

    #check if it will return space if you give it empty strings
    def test_empty(self):
        self.assertEqual(full_name.get_full_name("", ""), " ")



if __name__ == '__main__':
    unittest.main(verbosity=2)