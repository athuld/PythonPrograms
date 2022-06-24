import re

text = input("Enter a sentence: ")
old_string = input("Enter the string to replace: ")
new_string = input("Enter the new string: ")

new_text = re.sub(old_string,new_string,text)
print(f"\nNew Sentence: {new_text}")

ca_number = input("\nEnter the CA number: ")
numbers = re.findall(r'\d+',ca_number)
print(f"\nNumbers in the CA numbers are : {numbers}")
