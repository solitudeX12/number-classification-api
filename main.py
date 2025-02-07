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
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_fibonacci(n: int) -> bool:
    """Check if a number is in the Fibonacci sequence."""
    x1 = 5 * (n ** 2) + 4
    x2 = 5 * (n ** 2) - 4
    return math.isqrt(x1) ** 2 == x1 or math.isqrt(x2) ** 2 == x2

async def get_fun_fact(n: int) -> str:
    """Fetches a fun fact from an external API."""
    url = f"http://numbersapi.com/{n}/math"  # External API for math facts
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            if response.status_code == 200:
                return response.text  # Returns the fun fact
            else:
                return f"No fun fact found for {n}."
    except Exception:
        return f"Could not retrieve a fun fact for {n}."

@app.get("/classify/{number}")
async def classify_number(number: str):
    """
    Classifies a given number and returns its mathematical properties in JSON format.
    """
    # Validate input: Accept only integers
    if not number.isdigit() and not (number.startswith('-') and number[1:].isdigit()):
        raise HTTPException(status_code=400, detail={"number": number, "error": True})

    num = int(number)

    # Fetch fun fact asynchronously
    fun_fact = await get_fun_fact(num)

    # Construct response
    response = {
        "number": num,
        "error": False,
        "is_even": num % 2 == 0,
        "is_prime": is_prime(num),
        "is_fibonacci": is_fibonacci(num),
        "fun_fact": fun_fact,
    }
    
    return response

# Create a Mangum handler for Lambda
handler = Mangum(app)