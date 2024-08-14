# Python Strings

# 'hello' is the same as "hello".

print("Hello")
print('Hello')


print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')


# Multiline Strings


a = "Hello"
print(a)



a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print(a)



a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''

print(a)



# String Length
a = "Hello, World!"
print(len(a)) # 13


# Check String
txt = "The best things in life are free!"
print("free" in txt)


txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

  