name = "  basit  "
nam = "a-b-c-d"

# Basic string methods
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.title())
print(name.replace('basit', 'Ts-Developers'))
print(name.join([' ', 'Ts-Developers']))

# --- Additional Methods ---
print(name.strip())

# find() and index()
print(name.find('basit'))
print(name.index('basit'))

# startswith() and endswith()
print(name.startswith('  b'))
print(name.endswith('t  '))

# split with maxsplit
print(nam.split("-", 3))
