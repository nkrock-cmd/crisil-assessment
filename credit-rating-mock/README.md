Credit Rating

-> Project Overview
This project calculates credit ratings for a list of mortgages based on various risk factors such as Loan-to-Value (LTV), Debt-to-Income (DTI), credit score, loan type, and property type.

-> Features
- Calculates individual mortgage risk scores.
- Aggregates risk scores to determine an overall credit rating.
- Handles large datasets with parallel processing.
- Validates input data to ensure correctness.
- Provides comprehensive error handling and logging.


-> Risk Score Calculation
Each mortgage undergoes a series of calculations to determine its risk score:
1.	LTV Ratio Calculation: Higher LTV values increase risk.
2.	DTI Ratio Calculation: Higher DTI values increase risk.
3.	Credit Score Evaluation: Lower credit scores increase risk.
4.	Loan Type Adjustment: Adjustable-rate loans are riskier than fixed-rate loans.
5.	Property Type Adjustment: Condos are riskier than single-family homes.


-> Credit Rating Assignment
The final risk score for the RMBS determines the assigned credit rating:
- AAA: Total risk score ≤ 2 (Highly secure)
- BBB: 3 ≤ Total risk score ≤ 5 (Medium risk)
- C: Total risk score > 5 (High risk)


-> Installation Steps

1. Clone the repository:
   git clone https://github.com/nkrock-cmd/crisil-assessment.git
   
2. Navigate to the project directory:
   cd credit-rating-mock

3. Install dependencies (Need only Python to Use this Project, if already have ignore this):
   pip install -r requirements.txt
   Python >= 3.8

-> Usage
Run the `credit_rating.py` script to calculate credit ratings:
python credit_rating.py

Expected output:
Credit Rating: BBB

-> Testing
Run the unit tests using `unittest`:
python -m unittest test_credit_rating.py


-> Technical Decisions
1. Static Methods: Used for utility-like methods that do not depend on instance-specific data.
2. Error Handling: Input validation and logging ensure robustness.
3. Scalability Considerations: The solution can efficiently handle multiple mortgages. 
4.	Testing Approach: Unit tests implemented using Python’s unittest framework. Edge cases such as missing or invalid input data covered.

-> Data Validation
The validate_mortgage() method ensures that each mortgage in the input JSON contains all required fields and that their values are of appropriate types.


-> Future Enhancements
- Add support for external data sources (e.g., databases, APIs).
- Optimize further using vectorized operations with libraries like NumPy or Pandas.
- Implement parallel processing to distribute the workload across multiple CPU cores.
- Add more detailed logging and reporting.


-> Summary
- The code is optimized for readability, correctness, and scalability.
- The solution is robust, scalable, and well-documented.