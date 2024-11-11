import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)
       
    # Add your additional test cases here.
    def test_invalid_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(-5), "Invalid")

    def test_invalid_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), "Invalid")

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(0), 50)

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(6), 50)

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(12), 50)

    def test_teenager_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(13), 100)

    def test_teenager_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(18), 100)
    
    def test_teenager_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(20), 100)

    def test_middleage_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(21), 150)

    def test_middleage_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(48), 150)

    def test_middleage_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(60), 150)
    
    def test_senior_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(61), 100)

    def test_senior_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(65), 100)

if __name__ == '__main__':
    unittest.main()