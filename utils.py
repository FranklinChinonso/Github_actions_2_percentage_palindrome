def percentage_calculator(percent, whole):
    if whole == 0:
        return 0
    else:
        return (percent/100) * whole
    
def is_palindrome(s): 
    #evilisanameofafoemanasilive.
    #Evil is a name of a foeman as I live. 
     word = s.replace(" ","")
     word = word.lower()
     return word == word[::-1]   