# ---------------------------------
# Strings Indexing & Slicing
#[1] All Data in Python is Object
#[2] Object Contain Elements
#[3] Every Element Has Its Own Index
#[4] Python Use Zero Based Indexing ( Index Start From Zero ) 
#[5] Use Square Brackets To Access Element 
#[6] Enable Accessing Parts Of String, Tuples or Lists
# ---------------------------------

# Indexing ( Access Single Item )
myString = "I Love Python"
print(myString[0] ) # Index 0 => I
print(myString[9] ) # Index 8 => t

print(myString[-1]) # Index -1=> First Character From End => n
print(myString[-6]) # Index -6=> 6th Character From End => p

# Slicing ( Access Multiple Sequence Item )
# [Start:End] End Not Included
# [Start:End:steps]

print(myString[8:11]) # yth

print(myString[3:5]) # ov

print(myString[:10]) # If Start Is Not Here Will Start from 0  (I Love Pyt)

print(myString[5:]) # If End IS Not Here Will Go To The End (e Python)

print(myString[:]) # Full Data (I Love Python)

print(myString[0::1]) # Full Data (I Love Python)
print(myString[::1])  # Full Data (I Love Python)
print(myString[::2])  # (ILv yhn)
print(myString[::3])  # (Io tn)


