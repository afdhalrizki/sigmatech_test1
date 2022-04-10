from operator import le
from turtle import st


open = ["[","{","(","<"]
close = ["]","}",")",">"]
  
# Function to check parentheses
def check_parentheses(str):
    if 0 < len(str) < 4096:
        stack = []
        for i in str:
            if i in open:
                stack.append(i)
            elif i in close:
                pos = close.index(i)
                if ((len(stack) > 0) and
                    (open[pos] == stack[len(stack)-1])):
                    stack.pop()
                else:
                    return "FALSE"

        print(len(str))

        if len(stack) == 0:
            return "TRUE"
        else:
            return "FALSE"
    
    else:
        print(len(str))
        return "FALSE, more than 4096. {} long".format(len(str))
  
  
### TRUE value testing
string = "{{[<>[{{}}]]}}"
print(string,"-", check_parentheses(string))
  
string = "{<{[[{{[]<{{[{[]<>}]}}<>>}}]]}>}"
print(string,"-", check_parentheses(string))
  
string = "{{[{<[[{<{<<<[{{{[]{<{[<[[<{{[[[[[<{[{<[<<[[<<{[[{[<<<<<<<[{[{[{{<{[[<{<<<{<{[<>]}>}>>[]>}>]]}>}}]}]}]>>>>>>>]}]]}>>]]>>]>}]}>]]]]]}}>]]>]}>}}}}]>>>}>}]]>}]}}"
print(string,"-",check_parentheses(string))
  
string = "[<{<{[{[{}[[<[<{{[<[<[[[<{{[<<<[[[<[<{{[<<{{<{<{<[<{[{{[{{{{[<<{{{<{[{[[[{<<<[{[<{<<<>>>}>]}]>>>}]]]}]}>}}}>>]}}}}]}}]}>]>}>}>}}>>]}}>]>]]]>>>]}}>]]]>]>]}}>]>]]]}]}>}>]"
print(string,"-",check_parentheses(string))
 
string = "[[{[[<{{{{[[[<[{[[<{{{{[{[{[[[<<{<{[{<<<[[<[{[<{{[{[<[[<<[{<<[[[{<[{[[{{<<>[<<{{<<{[[[<{}{[{{{[[{{[[<[{}]>]]}}]]}}}]}>]]]}>>}}>>]>}}]]}]>}]]]>>}]>>]]>]}]}}>]}]>]]>>>}]}>}>>]]]}]}]}}}}>]]}]>]]]}}}}>]]}]]"
print(string,"-",check_parentheses(string))

string = "[{}<>]"
print(string,"-", check_parentheses(string))

### FALSE value testing
string = "]"
print(string,"-", check_parentheses(string))
  
string = "]["
print(string,"-", check_parentheses(string))
  
string = "[>]"
print(string,"-",check_parentheses(string))
  
string = "[>"
print(string,"-",check_parentheses(string))

string = "{<{[[{{[]<{[{[]<>}]}}<>>}}]]}>}"
print(string,"-", check_parentheses(string))

string = "{{[{<[[{<{<<<[{{{[]{<{[<[[<{{[[[[<{[{<[<<[[<<{[[{[<<<<<<<[{[{[{{<{[[<{<<<{<{[<>]}>}>>[]>}>]]}"
print(string,"-", check_parentheses(string))

string = ">}}]}]}]>>>>>>]}]]}>>]]>>]>}]}>]]]]]}}>]]>]}>}}}}]>>>}>}]]>}]}}"
print(string,"-", check_parentheses(string))

string = "[<{<{[{[{}[[<[<{{[<[<[[[<{{[<<<[[[<[<{{[<<{{<{<{<[<{[{{[{{{{[<<{{{<{[{[[[{<<<[{[<{<<>>[]}]>>>}]]]}]}>}}}>>]}}}}]}}]}>]>}>}>}}>>]}}>]>]]]>>>]}}>]]]>]>]}}>]>]]]}]}>}>]"
print(string,"-", check_parentheses(string))

string = "[{}<[>]"
print(string,"-", check_parentheses(string))