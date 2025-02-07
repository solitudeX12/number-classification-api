from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import math
import httpx  # Import httpx for making API calls
from mangum import Mangum  # Adapter for AWS Lambda

# Initialize FastAPI app
app = FastAPI(title="Number Classification API")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n: int) -> bool:
    return n > 0 and sum(i for i in range(1, n) if n % i == 0) == n

def get_digit_sum(n: int) -> int:
    return sum(int(digit) for digit in str(abs(n)))

def get_properties(n: int) -> list:
    properties = []
    if n % 2 == 0:
        properties.append("Even")
    else:
        properties.append("Odd")
    if n > 0:
        properties.append("Positive")
    elif n < 0:
        properties.append("Negative")
    return properties

def get_fun_fact(n: int) -> str:
    try:
        response = requests.get(f"http://numbersapi.com/{n}", timeout=5)
        if response.status_code == 200:
            return response.text
    except requests.exceptions.RequestException:
        return "No fun fact available at the moment."
    return "No fun fact available."

@app.get("/classify/{number}")
async def classify_number(number: int, response: Response) -> Dict:
    result = {
        "number": number,
        "prime": is_prime(number),
        "perfect": is_perfect(number),
        "properties": get_properties(number),
        "digit_sum": get_digit_sum(number),
        "fun_fact": get_fun_fact(number)
    }
    
    # Set JSON response headers explicitly
    response.headers["Content-Type"] = "application/json"
    return result


# Create a Mangum handler for Lambda
handler = Mangum(app)