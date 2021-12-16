import unittest
from Activity_Employee import Employee



class Activity_Raise_Test(unittest.TestCase):
    def setUp(self):
        self.employee = Employee("Bob", "Candice", 50000)

    # test_give_default_raise()

    def test_give_default_raise(self):
        print("The default raise is 50000")
        self.employee.give_raise()
        self.assertEqual(55000, self.employee.salary)
    
    # test_give_custom_raise()

    def test_give_custome_raise(self):
        print("Here we test giving a custom raise")
        self.employee.give_raise(200)
        self.assertEqual(50200, self.employee.salary)
        # self.employee.give_raise(pay_raise = int("Input custome raise: "))
        # self.assertEqual()

unittest.main()