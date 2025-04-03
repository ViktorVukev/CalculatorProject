def calculate(entry_var):
    try:
        expression = entry_var.get().replace('÷', '/').replace('×', '*').replace('²', '**2').replace('√', 'sqrt')
        result = do_calculations(expression)
        entry_var.set(result)
    except Exception as e:
        entry_var.set("Error")

def do_calculations(expression):
    try:
        if 'sqrt' in expression:
            expression = expression.replace('sqrt', 'math.sqrt')
        result = eval(expression)
        return str(result)

    except Exception as e:
        return "Error"