def balance_parens(string):
    # Define a function that is called with a string that contains letters, numbers, or parens
    balanced_str = ''
    tbd_open_parens_index_list = []
    # Balance our string
    # Loop through the entire string

    # If character is not parens, ignore character
    for c in string:
        if c!= "(" and c != ")":
            balanced_str += c
        
    # If there is a parens, need to consider the following cases:
    # If open parens: then we MAY have a closing parens
        elif c == "(":
            # Append index of open parens 
            balanced_str += c
            tbd_open_parens_index_list.append(len(balanced_str) -1)
    # If we get a close parens, check if it is paired with open parens.
        else:
            if len(tbd_open_parens_index_list) == 0:
                continue
            else:
                tbd_open_parens_index_list.pop()
                balanced_str += c

    fully_balanced_str = ""
    for i, c in enumerate(balanced_str):
        if i in tbd_open_parens_index_list:
            continue
        fully_balanced_str += c
    # Return value is a string that has every open paren closed (left right parity)
    return fully_balanced_str
