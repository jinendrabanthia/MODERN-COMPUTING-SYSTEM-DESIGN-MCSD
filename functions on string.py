#wapp all functions
#len(),strip(),rstrip(),lstrip(),find(),index(),rindex(),rfind(),replace(),count(),title()
#lower(),upper(),isnumeric(),isalpha(),isalnum(),isspace(),islower(),isupper(),count(),
#replace(),split(),join(),upper(),swapcase(),lower(),title(),capitalize(),startswith(),
#endswith()
# WAPP - Python String Functions

s = "  Hello Python 123  "

# 1. len()
print("len():", len(s))

# 2. strip()
print("strip():", s.strip())

# 3. rstrip()
print("rstrip():", s.rstrip())

# 4. lstrip()
print("lstrip():", s.lstrip())

# 5. find()
print("find():", s.find("Python"))

# 6. index()
print("index():", s.index("Python"))

# 7. rfind()
print("rfind():", s.rfind("o"))

# 8. rindex()
print("rindex():", s.rindex("o"))

# 9. replace()
print("replace():", s.replace("Python", "Java"))

# 10. count()
print("count():", s.count("o"))

# 11. title()
print("title():", s.title())

# 12. lower()
print("lower():", s.lower())

# 13. upper()
print("upper():", s.upper())

# 14. isnumeric()
print("isnumeric():", "12345".isnumeric())

# 15. isalpha()
print("isalpha():", "Python".isalpha())

# 16. isalnum()
print("isalnum():", "Python123".isalnum())

# 17. isspace()
print("isspace():", "   ".isspace())

# 18. islower()
print("islower():", "hello".islower())

# 19. isupper()
print("isupper():", "HELLO".isupper())

# 20. split()
print("split():", "Python Java C++".split())

# 21. join()
words = ["Python", "Java", "C++"]
print("join():", " ".join(words))

# 22. swapcase()
print("swapcase():", "Hello World".swapcase())

# 23. capitalize()
print("capitalize():", "hELLO WORLD".capitalize())

# 24. startswith()
print("startswith():", s.strip().startswith("Hello"))

# 25. endswith()
print("endswith():", s.strip().endswith("123"))

# --------------------------------------------------
# QUICK DIFFERENCE
# --------------------------------------------------

# find() -> returns -1 if not found
print("find:", "hello".find("x"))

# index() -> gives ValueError if not found
# print("index:", "hello".index("x"))

# rfind() -> finds last occurrence
print("rfind:", "banana".rfind("a"))

# rindex() -> finds last occurrence
print("rindex:", "banana".rindex("a"))

# split() -> String to List
print("split:", "A B C".split())

# join() -> List to String
print("join:", "-".join(["A", "B", "C"]))

# capitalize() -> Only first character uppercase
print("capitalize:", "hELLO WORLD".capitalize())

# title() -> First character of every word uppercase
print("title:", "hello world".title())