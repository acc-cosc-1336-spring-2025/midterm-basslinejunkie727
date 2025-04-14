#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import test_config
from src.question_a.main import get_sum_of_evens
from src.question_b.main import get_person_category
from src.question_c.main import get_bonus_pay_amount
from src.question_d.main import get_assessment_value
from src.question_d.main import get_tax_assessed
class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())
    def test_get_sum_of_evens(self):
        self.assertEqual(get_sum_of_evens(11),30)
        self.assertEqual(get_sum_of_evens(10),30)
        self.assertEqual(get_sum_of_evens(8),20)

    def test_get_person_category(self);
        self.assertEqual(get_person_category(1),'infant')
        self.assertEqual(get_person_category(2),'child')
        self.assertEqual(get_person_category(14),'teenager')
        self.assertEqual(get_person_category(20),'adult')

    def test_get_bonus_pay_amount(self):
        self.assertEqual(get_bonus_pay_amount(-1),'invalid arguments')
        self.assertEqual(get_bonus_pay_amount(200),10)
        self.assertEqual(get_bonus_pay_amount(600),36)
        self.assertEqual(get_bonus_pay_amount(1000),70)
        self.assertEqual(get_bonus_pay_amount(1500),120)
        self.assertEqual(get_bonus_pay_amount(2000),'invalid arguments')

    def test_get_assessment_value(self):
        self.assertEqual(get_assessment_value(10000),6000)
        self.assertEqual(get_assessment_value(20000),12000)

    def test_get_tax_assessed(self):
        self.assertEqual(get_tax_assessed(6000),43.20)
        self.assertEqual(get_tax_assessed(10000),72)



