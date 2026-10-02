from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "AI Voice Lead Agent backend is running!"
    }


@app.post("/check-lead")
async def check_lead(request: Request):
    body = await request.json()

    # Check if this is a Vapi tool call
    tool_calls = body.get("message", {}).get("toolCalls", [])

    if tool_calls:
        tool_call = tool_calls[0]

        arguments = tool_call.get("function", {}).get("arguments", {})

        monthly_income = arguments.get("monthly_income", 0)
        loan_amount = arguments.get("loan_amount", 0)

        if monthly_income >= 50000 and loan_amount <= 1000000:
            status = "qualified_for_next_step"
        else:
            status = "needs_review"

        return {
            "results": [
                {
                    "toolCallId": tool_call.get("id"),
                    "result": {
                        "status": status,
                        "monthly_income": monthly_income,
                        "loan_amount": loan_amount
                    }
                }
            ]
        }

    # Manual/direct test
    monthly_income = body.get("monthly_income", 0)
    loan_amount = body.get("loan_amount", 0)

    if monthly_income >= 50000 and loan_amount <= 1000000:
        status = "qualified_for_next_step"
    else:
        status = "needs_review"

    return {
        "status": status,
        "monthly_income": monthly_income,
        "loan_amount": loan_amount
    }