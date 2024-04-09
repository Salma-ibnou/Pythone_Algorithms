# -------------------------
# ----- Concatenation -----
# -------------------------
 
msg = "I love"
lang = "Python"
print(msg + " " + lang) # + " " + for make espace

Full = msg + " " + lang 
print(Full)

a =("hello \
      i love \
      Python")
b = ("A \
      B \
      C")

print(a+ "  " + b)
# Result => hello       i love       Python  A       B       C

print(a+ "\n" + b)
# Result => hello       i love       Python
#           A       B       C

#error:can only concatenate str (not "int") to str
print("Hello" + 1)
