Credit Rating GraphQL API

Project Overview: 

This is a GraphQL API built with FastAPI and Strawberry. GraphQL is a query language and runtime for APIs that allows clients to request exactly the data they need, reducing over-fetching and under-fetching issues. It calculates the credit rating for Residential Mortgage-Backed Securities (RMBS) based on mortgage details like credit score, loan amount, property value, income, and debt.

- Provides a GraphQL API for credit rating calculation
- Takes multiple mortgages as input and calculates their risk score
- Returns a credit rating (AAA, BBB, C) based on predefined logic
- Uses FastAPI and Strawberry GraphQL

Key Concepts of GraphQL

1. Schema:
A GraphQL schema defines the structure of data that clients can query. It includes:
-Types (objects with fields)
-Queries (to fetch data)
-Mutations (to modify data)
2. Queries:
GraphQL allows clients to request specific fields instead of getting the whole dataset.
3. Mutations (Updating or Adding Data):
GraphQL mutations modify data (create, update, delete records).

Installation Steps:

1. Clone the project
First, download this project by running:

git clone https://github.com/nkrock-cmd/crisil-assessment.git
cd credit-rating-graphql

2. Create a virtual environment

python -m venv venv
venv\Scripts\activate

3. Install required libraries
Run this to install all necessary packages:

pip install -r requirements.txt

Once everything is set up, start the API server, 
Run this Command:

uvicorn credit_rating_graphql:app --reload

After successful run, Go to:
http://127.0.0.1:8000/graphql

Here, you can run queries and test the API!
Send a GraphQL query like this:

query {
  getCreditRating(mortgages: [
    {
      creditScore: 750,
      loanAmount: 200000,
      propertyValue: 2500000,
      annualIncome: 40000,
      debtAmount: 80000,
      loanType: "fixed",
      propertyType: "single_family"
    },
    {
      creditScore: 680,
      loanAmount: 150000,
      propertyValue: 17500000,
      annualIncome: 450000,
      debtAmount: 10000,
      loanType: "adjustable",
      propertyType: "condo"
    }
  ]) {
    rating
    totalRiskScore
  }
}

Expected Output:

{
  "data": {
    "getCreditRating": {
      "rating": "AAA",
      "totalRiskScore": 1
    }
  }
}

Built With
FastAPI - For handling API requests
Strawberry GraphQL - For GraphQL schema
Uvicorn - For running the server
