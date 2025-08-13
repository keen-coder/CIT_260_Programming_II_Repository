# Longer programming statements can be broken up into multiple lines using the \ (backslash) line
# continuation character.


var1: int = 10
var2: float = 2.5
var3: float = 473.3
var4: int = 22

result = var1 * 2 + var2 * 3 + \
         var3 * 4 + var4 * 5

# You can also enclose any statement in paranthesis and span multiple lines without having to use the
# continuation character (\)

monday: float = 235.43
tuesday: float = 6534.00
wednesday: float = 323.90

print("Monday's sales are", monday,
"and Tuesday's sales are", tuesday,
"and Wednesday's sales are", wednesday)

result = (var1 * 2 + var2 * 3 + 
          var3 * 4 + var4 * 5)