import logging

logging.basicConfig(level=logging.ERROR)

class CreditRating():
    
    @staticmethod
    def validate_mortgage(mortgage):
        required_fields = ["credit_score", "loan_amount", "property_value", "annual_income", "debt_amount", "loan_type", "property_type"]
        
        for field in required_fields:
            if field not in mortgage:
                raise ValueError(f"Missing field: {field}")
        
        if not isinstance(mortgage["credit_score"], (int, float)) or not 300 <= mortgage["credit_score"] <= 850:
            raise ValueError(f"Invalid credit_score: {mortgage['credit_score']}. Must be between 300 and 850.")
        
        if mortgage["loan_type"] not in ["fixed", "adjustable"]:
            raise ValueError(f"Invalid loan_type: {mortgage['loan_type']}. Must be 'fixed' or 'adjustable'.")
    
        if mortgage["property_type"] not in ["single_family", "condo"]:
            raise ValueError(f"Invalid property_type: {mortgage['property_type']}. Must be 'single_family' or 'condo'.")
     
        for field in ["credit_score", "loan_amount", "property_value", "annual_income", "debt_amount"]:
            if not isinstance(mortgage[field], (int, float))or mortgage[field] < 0:
                raise ValueError(f"Invalid {field}: {mortgage[field]}. Must be a non-negative number.")

            
    @staticmethod
    def calculate_ltv(loan_amount, property_value):
        if property_value == 0:
            raise ValueError("property_value cannot be zero.")
        ltv_ratio= loan_amount / property_value
        return ltv_ratio

    @staticmethod
    def calculate_dti(debt_amount, annual_income):
        if annual_income == 0:
            raise ValueError("annual_income cannot be zero.")
        dti_ratio = debt_amount / annual_income
        return dti_ratio

    @staticmethod
    def calculate_mortgage_risk(mortgage):
        
        try:
            CreditRating.validate_mortgage(mortgage)
            
            risk_score = 0
        
            credit_score = mortgage.get("credit_score", 0)
            loan_amount = mortgage.get("loan_amount", 0)
            property_value = mortgage.get("property_value", 1)
            annual_income = mortgage.get("annual_income", 1)
            debt_amount = mortgage.get("debt_amount", 0)
            loan_type = mortgage.get("loan_type", "").lower()
            property_type = mortgage.get("property_type", "").lower()

            # Loan-to-Value (LTV) Risk
            ltv = CreditRating.calculate_ltv(loan_amount, property_value)
            if ltv > 0.9:
                risk_score += 2
            elif ltv > 0.8:
                risk_score += 1

            # Debt-to-Income (DTI) Risk
            dti = CreditRating.calculate_dti(debt_amount, annual_income)
            if dti > 0.5:
                risk_score += 2
            elif dti > 0.4:
                risk_score += 1

            # Credit Score Risk
            if credit_score >= 700:
                risk_score -= 1
            elif credit_score < 650:
                risk_score += 1

            # Loan Type Risk
            if loan_type == "fixed":
                risk_score -= 1
            elif loan_type == "adjustable":
                risk_score += 1

            # Property Type Risk
            if property_type == "condo":
                risk_score += 1

            return risk_score
        
        except ValueError as e:
            logging.error(f"Error calculating mortgage risk: {e}")
            raise  
        except Exception as e:
            logging.error(f"Unexpected error calculating mortgage risk: {e}")
            raise

    
    @staticmethod
    def calculate_credit_rating(mortgages):
        if not isinstance(mortgages, list):
            raise ValueError("Input must be a list of mortgages.")
        if not mortgages:
            raise ValueError("Mortgages list cannot be empty.")
        
        total_risk_score = 0
        total_credit_score = 0
        num_mortgages = len(mortgages)
    
        for mortgage in mortgages:
            total_risk_score += CreditRating.calculate_mortgage_risk(mortgage)
            total_credit_score += mortgage.get("credit_score", 0)

        avg_credit_score = total_credit_score / num_mortgages if num_mortgages else 0
        if avg_credit_score >= 700:
            total_risk_score -= 1
        elif avg_credit_score < 650:
            total_risk_score += 1

        # Assign Ratings
        if total_risk_score <= 2:
            rating = "AAA"
        elif 3 <= total_risk_score <= 5:
            rating = "BBB"
        else:
            rating = "C"
        
        return rating

def main():
    sample_input = {
        "mortgages": [
            {
                "credit_score": 620,
                "loan_amount": 200000,
                "property_value": 250000,
                "annual_income": 60000,
                "debt_amount": 20000,
                "loan_type": "fixed",
                "property_type": "single_family"
            },
            {
                "credit_score": 650,
                "loan_amount": 150000,
                "property_value": 175000,
                "annual_income": 45000,
                "debt_amount": 10000,
                "loan_type": "adjustable",
                "property_type": "condo"
            }
        ]
    }

    rating = CreditRating.calculate_credit_rating(sample_input["mortgages"])
    print("Credit Rating:", rating)

if __name__ == "__main__":
    main()