import unittest
from credit_rating import CreditRating
import logging

logging.basicConfig(level=logging.ERROR)

class TestCreditRating(unittest.TestCase):
    def setUp(self):
        logging.disable(logging.CRITICAL)

    def tearDown(self):
        logging.disable(logging.NOTSET)


# CHECK FOR VALID VALUE AND BOUNDARIES TEST CASES
    def test_valid_mortgages(self):
        mortgage1 = {"credit_score": 750,"loan_amount": 200000,"property_value": 250000,"annual_income": 80000,"debt_amount": 20000,"loan_type": "fixed","property_type": "single_family"}
        mortgage2 = {"credit_score": 680,"loan_amount": 150000,"property_value": 175000,"annual_income": 45000,"debt_amount": 10000,"loan_type": "adjustable","property_type": "condo"}
        
        self.assertEqual(CreditRating.calculate_mortgage_risk(mortgage1), -2)
        self.assertEqual(CreditRating.calculate_mortgage_risk(mortgage2), 3)
    

    def test_edge_cases(self):
        high_ltv_mortgage = {"credit_score": 700,"loan_amount": 180000,"property_value": 200000,"annual_income": 60000,"debt_amount": 25000,"loan_type": "fixed","property_type": "single_family"}
        high_dti_mortgage = {"credit_score": 690,"loan_amount": 100000,"property_value": 150000,"annual_income": 40000,"debt_amount": 25000,"loan_type": "adjustable","property_type": "condo"}
        
        self.assertEqual(CreditRating.calculate_mortgage_risk(high_ltv_mortgage), 0)
        self.assertEqual(CreditRating.calculate_mortgage_risk(high_dti_mortgage), 4)


    def test_credit_score_boundaries(self):
        mortgage1={"credit_score":300,"loan_amount":100000,"property_value":200000,"annual_income":50000,"debt_amount":10000,"loan_type":"fixed","property_type":"single_family"}
        mortgage2={"credit_score":850,"loan_amount":100000,"property_value":200000,"annual_income":50000,"debt_amount":10000,"loan_type":"fixed","property_type":"single_family"}
        
        self.assertEqual(CreditRating.calculate_mortgage_risk(mortgage1), 0)
        self.assertEqual(CreditRating.calculate_mortgage_risk(mortgage2), -2)


    def test_exact_ltv_thresholds(self):
        mortgage1={"credit_score":700,"loan_amount":80000,"property_value":100000,"annual_income":50000,"debt_amount":10000,"loan_type":"fixed","property_type":"single_family"}
        mortgage2={"credit_score":700,"loan_amount":90000,"property_value":100000,"annual_income":50000,"debt_amount":10000,"loan_type":"fixed","property_type":"single_family"}
        
        self.assertEqual(CreditRating.calculate_mortgage_risk(mortgage1), -2)
        self.assertEqual(CreditRating.calculate_mortgage_risk(mortgage2), -1)


    def test_exact_dti_thresholds(self):
        mortgage1={"credit_score":700,"loan_amount":100000,"property_value":200000,"annual_income":50000,"debt_amount":20000,"loan_type":"fixed","property_type":"single_family"}
        mortgage2={"credit_score":700,"loan_amount":100000,"property_value":200000,"annual_income":50000,"debt_amount":25000,"loan_type":"fixed","property_type":"single_family"}
        
        self.assertEqual(CreditRating.calculate_mortgage_risk(mortgage1), -2)
        self.assertEqual(CreditRating.calculate_mortgage_risk(mortgage2), -1)

    def test_rating_boundaries(self):
            mortgage1=[{"credit_score":700,"loan_amount":80000,"property_value":100000,"annual_income":50000,"debt_amount":10000,"loan_type":"fixed","property_type":"single_family"}]
            mortgage2=[{"credit_score":650,"loan_amount":90000,"property_value":100000,"annual_income":50000,"debt_amount":25000,"loan_type":"adjustable","property_type":"condo"}]
            
            self.assertEqual(CreditRating.calculate_credit_rating(mortgage1), "AAA")
            self.assertEqual(CreditRating.calculate_credit_rating(mortgage2), "BBB")


# CHECK FOR MISSING OR INVALID VALUE TEST CASES
    def test_invalid_mortgages(self):
        mortgages = {"credit_score": "sevenhundread","loan_amount": 200000,"property_value": 250000,"annual_income": 60000,"debt_amount": 20000,"loan_type": "fixed","property_type": "single_family"}
        
        with self.assertRaises(ValueError):
            CreditRating.validate_mortgage(mortgages)

        mortgages = {"credit_score": 720,"loan_amount": 150000,"property_value": 175000}
        
        with self.assertRaises(ValueError):
            CreditRating.validate_mortgage(mortgages)
    
    def test_empty_mortgages(self):
        mortgages = []
        with self.assertRaises(ValueError):
            CreditRating.validate_mortgage([])
    
    def test_negative_mortgages(self):
        mortgages = [{"credit_score": 600, "loan_amount": 200000, "property_value": 210000, "annual_income": -40000, "debt_amount": 25000, "loan_type": "adjustable", "property_type": "condo"}]
        with self.assertRaises(ValueError):
            CreditRating.validate_mortgage(mortgages)


# CHECK FOR CREDIT RATING TEST CASES
    def test_credit_rating(self):
        mortgages = [
            {"credit_score": 750, "loan_amount": 200000, "property_value": 250000, "annual_income": 80000, "debt_amount": 20000, "loan_type": "fixed", "property_type": "single_family"},
            {"credit_score": 680, "loan_amount": 150000, "property_value": 175000, "annual_income": 45000, "debt_amount": 10000, "loan_type": "adjustable", "property_type": "condo"}
        ]
        rating= CreditRating.calculate_credit_rating(mortgages)
        self.assertEqual(rating, "AAA")

    def test_high_credit_score_low_risk(self):
        mortgages = [
            {"credit_score": 750, "loan_amount": 100000, "property_value": 200000, "annual_income": 80000, "debt_amount": 10000, "loan_type": "fixed", "property_type": "single_family"},
            {"credit_score": 720, "loan_amount": 150000, "property_value": 250000, "annual_income": 100000, "debt_amount": 20000, "loan_type": "fixed", "property_type": "single_family"}
        ]
        rating = CreditRating.calculate_credit_rating(mortgages)
        self.assertEqual(rating, "AAA")

    def test_medium_risk(self):
        mortgages = [
            {"credit_score": 680, "loan_amount": 180000, "property_value": 200000, "annual_income": 50000, "debt_amount": 25000, "loan_type": "adjustable", "property_type": "condo"},
            {"credit_score": 690, "loan_amount": 170000, "property_value": 210000, "annual_income": 60000, "debt_amount": 20000, "loan_type": "fixed", "property_type": "single_family"}
        ]
        rating = CreditRating.calculate_credit_rating(mortgages)
        self.assertEqual(rating, "BBB")

    def test_high_risk(self):
        mortgages = [
            {"credit_score": 600, "loan_amount": 200000, "property_value": 210000, "annual_income": 40000, "debt_amount": 25000, "loan_type": "adjustable", "property_type": "condo"},
            {"credit_score": 620, "loan_amount": 195000, "property_value": 200000, "annual_income": 35000, "debt_amount": 20000, "loan_type": "adjustable", "property_type": "condo"}
        ]
        rating = CreditRating.calculate_credit_rating(mortgages)
        self.assertEqual(rating, "C")


# CHECK FOR EXCEPTION HANDLING TEST CASES
    def test_division_by_zero(self):
        mortgage = {"credit_score": 700, "loan_amount": 100000, "property_value": 0, "annual_income": 50000, "debt_amount": 10000, "loan_type": "fixed", "property_type": "single_family"}
        with self.assertRaises(ValueError):
            CreditRating.calculate_mortgage_risk(mortgage)

    def test_division_by_zero_annual_income(self):
        mortgage = {"credit_score": 700, "loan_amount": 100000, "property_value": 100000, "annual_income": 0, "debt_amount": 10000, "loan_type": "fixed", "property_type": "single_family"}
        with self.assertRaises(ValueError):
            CreditRating.calculate_mortgage_risk(mortgage)      


    

if __name__ == "__main__":
    unittest.main()