multiple_line = '''some text with multiple lines
and some more text
and even more text
additionally, some more text with specified symbols like @#$%^&*()_+ and numbers 1234567890
and some more ' " text with quotes
and some more text with newlines
and some more text with tabs\t\t\t
and some more text with unicode characters like ü, ö, ä, and ß
and some more text with emojis 😊😂👍'''

print (multiple_line)

name = "John"
age = 30
sex = "male"
birth_year = 1990

str2 = f"{name} is a {age} year old {sex} born in {birth_year}."
print (f"\n\n{str2}")

print("qwertyu".ljust(10, "-"))