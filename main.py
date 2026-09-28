from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import ast
import operator

app = FastAPI()


class ExpressionData(BaseModel):
    expression: str


OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
}


def evaluate(node):

    if isinstance(node, ast.Expression):
        return evaluate(node.body)

    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return node.value

    if isinstance(node, ast.BinOp):
        left = evaluate(node.left)
        right = evaluate(node.right)

        operation = OPERATORS.get(type(node.op))

        if operation is None:
            raise ValueError("Operator not supported")

        return operation(left, right)

    if isinstance(node, ast.UnaryOp):
        value = evaluate(node.operand)

        if isinstance(node.op, ast.USub):
            return -value

        if isinstance(node.op, ast.UAdd):
            return value

    raise ValueError("Invalid expression")


@app.get("/")
def home():
    return {
        "message": "Expression Evaluator API Running"
    }


@app.post("/calculate")
def calculate(data: ExpressionData):

    expression = data.expression.strip()

    if not expression:
        raise HTTPException(
            status_code=400,
            detail="Expression cannot be empty"
        )

    try:
        tree = ast.parse(expression, mode="eval")
        result = evaluate(tree)

        return {
            "expression": expression,
            "result": result
        }

    except ZeroDivisionError:
        raise HTTPException(
            status_code=400,
            detail="Cannot divide by zero"
        )

    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Invalid mathematical expression"
        )