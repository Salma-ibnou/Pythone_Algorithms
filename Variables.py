# ------------------------------------------------------------------------
# ------------------------- Variables : --------------------------------------------------
# ------------------------------------------------------------------------
# sytnax => [Variable Name] [Assignment Operator] [Value]
# 
#
# [1] Can Start With (a-z A-Z) or  Underscore like: ' Myvar , varbe , .. '
# [2] Can't Start with speciale Characters or Number like: ' 100variable , @Variable , ..'  
# [3] Can Include (0-9) or Underscore like: ' __myVariable , myvariable , my100varible , ... '
# [4] can't Include Special Characters like: ' My@variable , my-variable , .. ' 
# [5] Name is not like name [ Case Sensitve ] like: ' name = "my value" print(Name) => name isn't Name '
# ------------------------------------------------------------------------
name = "Salma Ibnou~Abs" # Single Word => the Normal Way 
myName = "Salma Ibnou~Abs" # Two Words => camelCase
my_name = "Salma Ibnou~Abs" # Two Words => Snake_case
#
# --------------------------- Examples : ---------------------------------
# ------ Source Code : Original Code You Write It In Computer-------------
# ------ Translation : Converting Source Code Into Machine Language ------
# ------ Compilation : Translate Code Before Run Time  -------------------
# ------ Run-time : Period App Take to Executing Commands  ---------------
# ------ Interpreted : code Translated On The Fly During Executin  -------
# ------------------------------------------------------------------------

# [1]: we can change the variables with any problems like we can put the one value in the var [x]  and we change the other value in the same code or scope like this ===>
#
x = 10
x = "Hello world"
print(x)
# 
# the resalt is ' Hello World ' but the first value is change it 
#
# Reserved Words
help("keywords")
#
#
#
a,b,c = 1, 2, 3
print(a)
print(b)
print(c)