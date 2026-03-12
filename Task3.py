
from fastapi import FastAPI,HTTPException
 
app=FastAPI()

# a) sum of two numbers
 
@app.post("/sum")
def calculate_sum(num1, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail="Both inputs must be numbers"
        )

    return {"sum": num1 + num2}

# b) lower case to upper case string transformation

@app.get("/uppercase")

def lower_to_uppercase(text: str):

    if not text.islower():
        raise HTTPException(
            status_code=400,
            detail="Input needs to be in lowercase"
        )

    return {"uppercase": text.upper()}


# to run api use command uvicorn Task3:app --reload

