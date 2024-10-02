

# name = input("Enter Your name :")

# number = int(input("Enter a number: "))


# print(f"Name: {name}")
# print(f"Number: {number}")


# majority number

nums = [2, 2, 1, 1, 1, 2, 2, 1, 1]

major = None
count = 0
for num in nums:

    if count == 0:
        major = num
    if num == major:
        count += 1
    else:
        count -= 1

print(major)
