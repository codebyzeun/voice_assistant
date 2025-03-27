import re

def calculate(expression):
    try:
        expression = re.sub(r'[^0-9+\-*/().]', '', expression)
        result = eval(expression)
        return f"The result is {result}"
    except Exception as e:
        return "Sorry, I couldn't solve that. Please try again."
