# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# String with special characters
my_text = str("abcgeekbrain geekbrain")
print(type(my_text))
li = list(my_text.split(" "))
print("String before conversion: ", li)
# using lambda function to find if the special characters are in the list
# Converting list to string using the join method
normal_string = " ".join(filter(lambda expr: "abc" not in expr, li))
print("String after conversion: ", normal_string)