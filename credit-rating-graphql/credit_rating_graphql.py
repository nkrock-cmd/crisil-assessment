import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from typing import List


@strawberry.input
class MortgageInput:
    credit_score: int
    loan_amount: float
    property_value: float
    annual_income: float
    debt_amount: float
    loan_type: str
    property_type: str

@strawberry.type
class CreditRating:
    rating: str
    total_risk_score: int

# Function to Calculate Risk Score
def calculate_risk_score(mortgage: MortgageInput) -> int:
    risk_score = 0

    # Loan-to-Value (LTV) Calculation
    ltv = mortgage.loan_amount / mortgage.property_value
    if ltv > 0.9:
        risk_score += 2
    elif ltv > 0.8:
        risk_score += 1

    # Debt-to-Income (DTI) Calculation
    dti = mortgage.debt_amount / mortgage.annual_income
    if dti > 0.5:
        risk_score += 2
    elif dti > 0.4:
        risk_score += 1

    # Credit Score Impact
    if mortgage.credit_score >= 700:
        risk_score -= 1
    elif mortgage.credit_score < 650:
        risk_score += 1

    # Loan Type Impact
    if mortgage.loan_type == "fixed":
        risk_score -= 1
    elif mortgage.loan_type == "adjustable":
        risk_score += 1

    # Property Type Impact
    if mortgage.property_type == "condo":
        risk_score += 1

    return risk_score

# Function to Determine RMBS Rating
def determine_rmbs_rating(mortgages: List[MortgageInput]) -> CreditRating:
    total_risk_score = sum(calculate_risk_score(m) for m in mortgages)
    avg_credit_score = sum(m.credit_score for m in mortgages) / len(mortgages)

    # Adjust risk score based on avg credit score
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

    return CreditRating(rating=rating, total_risk_score=total_risk_score)

@strawberry.type
class Query:
    @strawberry.field
    def get_credit_rating(self, mortgages: List[MortgageInput]) -> CreditRating:
        return determine_rmbs_rating(mortgages)

# Setup FastAPI and GraphQL Router
schema = strawberry.Schema(query=Query)
graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")

