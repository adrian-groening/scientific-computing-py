def arithmetic_arranger(problems, show_answers=False):

    # Error checks
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = []
    second_line = []
    dashes = []
    answers = []

    for problem in problems:
        parts = problem.split()

        if len(parts) != 3:
            return "Error: Invalid problem format."

        num1, operator, num2 = parts

        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."

        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Determine the width of the problem
        width = max(len(num1), len(num2)) + 2
        top = num1.rjust(width)
        bottom = operator + " " + num2.rjust(width - 2)
        dash = "-" * width
        first_line.append(top)
        second_line.append(bottom)
        dashes.append(dash)

        if show_answers:
            result = str(eval(problem))
            answers.append(result.rjust(width))

    # Assemble the formatted output
    arranged_problems = "    ".join(first_line) + "\n"
    arranged_problems += "    ".join(second_line) + "\n"
    arranged_problems += "    ".join(dashes)
    if show_answers:
        arranged_problems += "\n" + "    ".join(answers)

    return arranged_problems
    
print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True))



print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')