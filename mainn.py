# import random

# def citati():
#     with open('quotes.txt', 'w', encoding='utf-8') as file:
#         sample_quotes = [
#             "Жизнь - это то, что с тобой происходит, пока ты строишь планы. - Джон Леннон\n",
#             "Единственный способ делать великие дела - это любить то, что ты делаешь. - Стив Джобс\n",
#             "Успех - это способность идти от неудачи к неудаче, не теряя энтузиазма. - Уинстон Черчилль\n",
#             "Будь тем изменением, которое ты хочешь видеть в мире. - Махатма Ганди\n"
#         ]
#         file.writelines(sample_quotes)  

#     with open('quotes.txt', 'r', encoding='utf-8') as file:
#         quotes = file.readlines()
#         random_quote = random.choice(quotes).strip()
#         print(f"Случайная цитата: {random_quote}")

# citati()

op1 = ['+', '-', '*', '/', '//', '%', '**','==', '!=', '>', '<', '>=', '<=','and', 'or', 'not','&', '|', '^', '~', '<<', '>>','in', 'not in','is', 'is not']
print()
a = input("введите первое число: ")
b = input("введите второе число: ")
print(op1)
op2 = input("выберите оператор: ")
if op2 not in ['in', 'not in', 'is', 'is not']:
    n1 = int(a)
    n2 = int(b)
else: 
    s1 = str(a)
    s2 = str(b)

if op2 == "+":
    result = n1 + n2
    print("итог: ", result)
if op2 == "-":
    result = n1 - n2
    print("итог:", result)
if op2 == "*":
    result = n1 * n2
    print("итог:", result)
if op2 == "/":
    if n2 == 0:
        print("на ноль делить нельзя")
    else:
        result = n1 / n2
        print("итог: ", result)
if op2 == "//":
    if n2 == 0:
        print("на ноль делить нельзя") 
    else:
        result = n1 // n2
        print("итог: ", result)
if op2 == "%":
    if n2 == 0:
        print("на ноль делить нельзя")
    else:
        result = n1 % n2
        print("итог:", result)
if op2 == "**":
    result = n1 ** n2
    print("итог: ", result)

if op2 == "==":
    result = n1 == n2
    print("итог: ", result)
if op2 == "!=":
    result = n1 != n2
    print("итог: ", result)
if op2 == ">":
    result = n1 > n2
    print("итог: ", result)
if op2 == "<":
    result = n1 < n2
    print("итог: ",result)
if op2 == ">=":
    result = n1 >= n2
    print("итог: ",result)
if op2 == "<=":
    result = n1 <= n2
    print("итог: ",result)

if op2 == 'and':
        log1 = (n1 != 0)
        log2 = (n2 != 0)
        result = log1 and log2
        print("итог: ", result)
if op2 == 'or':
        log1 = (n1 != 0)
        log2 = (n2 != 0)
        result = log1 or log2
        print("итог:", result)

if op2 == 'not':
    n3 = int(input("введите число для оператора not: "))
    if n3 == 0:
        result = True
    else: 
        result = False
    print("итог: ", result)

if op2 == '&':
        result = n1 & n2
        print("итог: ", result)
if op2 == '|':
        result = n1 | n2
        print("итог: ", result)
if op2 == '^':
        result = n1 ^ n2
        print("итог: ", result)
if op2 == '<<':
        result = n1 << n2
        print("итог: ", result)
if op2 == '>>':
        result = n1 >> n2
        print("итог: ", result)

if op2 == 'in':
    result = s1 in s2
    print(s1, "находится в ", s2 )
if op2 == 'not in':
    result = s1 not in s2
    print(s1, "не находится в ", s2 )
if op2 == 'is':
        result = s1 == s2
        print("итог", result)
        
if op2 == 'is not':
        result = s1 != s2
        print("итог:", result)
