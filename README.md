# Expression Evaluator API

A FastAPI application that evaluates basic mathematical expressions safely.

## Features

- Mathematical Expression Evaluation
- Addition
- Subtraction
- Multiplication
- Division
- Power
- Parentheses
- Input Validation
- Error Handling

## Technologies

- Python
- FastAPI
- Pydantic
- Python AST

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
uvicorn main:app --reload
```

## Endpoint

```text
POST /calculate
```

## Example Request

```json
{
    "expression": "(10 + 5) * 2"
}
```

## Example Response

```json
{
    "expression": "(10 + 5) * 2",
    "result": 30
}
```