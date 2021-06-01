# def balance_parens(string):
#     # Define a function that is called with a string
#     # iterate through the string from left to right +1 for each open parens -1 for each close parens, when counter < 0 remove that right parens
#     output = []
#     final = []
#     internal_parens(string.split(), output)
#     internal_parens(output[::-1], final)
#     final_string = ""
#     return final_string.join(final)[::-1]

# def internal_parens(array, output):
#     count = 0
#     for x in array:
#         if not(count <= 0 and x == ")"):
#             output.append(x)
#         elif (x == "("):
#             count += 1
#         elif(x == ")"):6
#             count -= 1



# print(balance_parens('hi!()('))




def balance_parens(string):
    # Define a function that is called with a string
    # 
    pass
    result = ''