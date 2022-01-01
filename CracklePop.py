def crackle_pop(n: int) -> str:
    special_divisors = {
        3: "Crackle",
        5: "Pop",
    }
    message = ""
    for divisor, text in sorted(special_divisors.items()):
        if n % divisor == 0:
            message += text
    return message or str(n)


for n in range(1, 101):
    print(crackle_pop(n))
