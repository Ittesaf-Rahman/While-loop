a = 1
while a <= 6:
    print(a)
    a = a + 1


numbers = 1
sum = 0
while numbers < 10:
   sum += numbers
   numbers +=numbers
print(sum)


x = int(input("Enter a number = "))
factroial = 1
while x > 0:
    factroial  = factroial * x
    x = x - 1
print(factroial)

z = input("Enter a string = ")
reverse_string = ""
index = len(z) - 1
while index >= 0:
    reverse_string = reverse_string + z[index]
    index = index - 1
print(reverse_string)

n = int(input("Enter a number = "))
temp = ""
temp = n
sum2 = 0
while temp > 0:
    d = temp % 10
    sum2 += d ** 3
    temp = temp // 10
if sum2 == n:
    print("Yes this is a armostone number")
else:
    print("No this is not a armostone number")