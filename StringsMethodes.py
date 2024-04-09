# ----------------------------
# ----- Strings Methods ------
# ----------------------------
# ---------- Part 1 ----------
   
# strip()  rstrip() lstrip()

a =  "   I Love Python   "
#print(len(a.strip()))
#print(len(a.rstrip()))
#print(len(a.lstrip()))

print(a.strip()) # for remove the space in the right and the left (I Love Python)
print(a.rstrip()) # for remove the space in the right(   I Love Python)
print(a.lstrip()) # for remove the space in the left (I Love Python   )


a = "#######I love Python######"
print(a.strip('#')) # result => (I Love Python)
print(a.rstrip('#'))# result => (#######I love Python)
print(a.lstrip('#')) # result => (I love Python######)

# title()
b= "I Love 2d Graphics and 3g Technology and python"
print(b.title())

# capitalize()
b= "I Love 2d Graphics and 3g Technology and python"
print(b.capitalize())

# zfill

c, d, e, f = "1" , "11" , "111" , "1111"
print(c) # => 1
print(d) # => 11
print(e) # => 111
print(f) # => 1111

print(c.zfill(3)) # => 001
print(d.zfill(3)) # => 011
print(e.zfill(3)) # => 111
print(f.zfill(3)) # => 1111

# upper() 
g = "salma"

print(g.upper()) # => SALMA

# lower()
h = "SAlma"

print(h.lower()) # => salma

# ---------- Part 2 ---------

# split() rsplit()
#  Its purpose is to divide a string into a list (or array) of substrings based on a specified delimiter.

a = "I Love Python and PHP"
print(a.split())
