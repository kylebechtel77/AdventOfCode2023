with open('./Day1/input1', 'r') as f:
    total = 0
    for line in f:
        digits = [char for char in line.strip() if char.isnumeric()]
        line_result = digits[0] + digits[len(digits) - 1]
        total += int(line_result)

    print(total)