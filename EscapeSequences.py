# ------------------------------------------------
# Escape Sequences Characters
# \b => back Space
# \newline => Escape New Line + \
# \ => Escape  back  slash 
# \' => Escape  single Quotes
# \" => Escape  Double Quotes
# \n => Line Feed 
# \r => Carriage Return
# \t => Horizontal Tab
# \xhh => Character Hex Value 
# ------------------------------------------------

# Back Space
print("Hello\bWorld") # Will Remove last letter 'O'
# Result => Hell World

# Escape New Line + \
print("hello \
      i love \
      Python")
# Result => hello       i love       Python

# Escape Back Slash
print("hello python \\")
# error : print("hello python \") # it's can running
# Result => hello python \

# Escape Single Quote  
print('hello python Quote \'test\'')
# Result => hello python Quote 'test'

# Escape Double Quotes  
print("hello python Quote  \"test\" ")
# Result => hello python Quote  "test"

# Line Feed
print("Hello World\n secound line")
# Result => Hello World
#           secound line

# Carriage Return
print("123456\rAbcde")
# Result => Abcde6

# Horizontal Tab
print("Hello\tpython")
# Result => Hello   python

#Character Hex Value 
print("\x4f\x73")
# Result => Os  '\x4f => O  , \x73 => s , .. '
