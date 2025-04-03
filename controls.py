import re

def clear(entry_var):
    entry_var.set("")

def clear_recent(entry_var):
    current = entry_var.get()
    if current:
        match = re.search(r"(-?\d+(\.\d+)?)(?=[÷×+\-]?$)", current)
        if match:
            updated_expression = current[:match.start()]
        else:
            updated_expression = ""
    entry_var.set(updated_expression)

def delete(entry_var):
    current = entry_var.get()
    entry_var.set(current[0:len(current)-1])

def click_button(value, entry_var):
    current = entry_var.get()

    if value == 'x²':
        entry_var.set(current + '²')

    elif value == '±':
        if current:
            match = re.search(r"(-?\d+(\.\d+)?)$|([÷×+\-])$", current)

            if match:
                last_number = match.group(0)  # extract last number

                if last_number.startswith('-'):
                    if len(last_number) < len(current):  # check if symbol is needed
                        new_number = '+' + last_number[1:]
                    else:
                        new_number = last_number[1:]
                else:
                    if len(last_number) < len(current):
                        new_number = '(-' + last_number + ')'
                    else:
                        new_number = '-' + last_number

                updated_expression = current[:match.start()] + new_number
                entry_var.set(updated_expression)

    elif value == '¹⁄ₓ':
        if current:
            match = re.search(r"(-?\d+(\.\d+)?)$|([÷×+\-])$", current)

            if match:
                last_number = match.group(0)
                if float(last_number) == 0:
                    entry_var.set("Error")  # division by 0
                    return

                new_number = f"1/({last_number})"
                updated_expression = current[:match.start()] + new_number
                entry_var.set(updated_expression)

    elif value == '√x':
        if current:
            match = re.search(r"(-?\d+(\.\d+)?)$|([÷×+\-])$", current)

            if match:
                last_number = match.group(0)
                if float(last_number) < 0:
                    entry_var.set("Error")  # sqrt of negative
                    return

                new_number = f"√({last_number})"
                updated_expression = current[:match.start()] + new_number
                entry_var.set(updated_expression)

    else:
        entry_var.set(current + str(value))