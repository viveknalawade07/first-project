#Write a Python program to get the largest number from a list.
number=[23,45,67,46,24]
largest=number[0]
for n in number:
    if n>largest:
        largest=n
print("The largest item in list is",largest)
