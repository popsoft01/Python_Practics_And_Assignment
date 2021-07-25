import re

result = re.search('Python', 'Python is fun')
print(result.group() if result else "not found")
result2 = re.search('fun!', 'Python is fun')
print(result2.group() if result2 else 'not found')
