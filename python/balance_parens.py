def balance_parens(string):
    # Define a function that is called with a string that contains letters, numbers, or parens
    balanced_str = ''
    tbd_open_parens_index_list = []

    # Loop through the entire string
    # Balancing our string
    for c in string:
    # If character is not parens, ignore character and append
        if c != "(" and c != ")":
            balanced_str += c
        
    # If there is a parens, need to consider the following cases:
    # If open parens: then we MAY have a closing parens
        elif c == "(":
            # Append open to output
            balanced_str += c
            #This list will track our potential unbalanced open parens
            tbd_open_parens_index_list.append(len(balanced_str) -1)
    # If we get a close parens, check if it is paired with open parens.
        else:
            #If no open parens when closed parens found, ignore
            if len(tbd_open_parens_index_list) == 0:
                continue
            # Remove last open parens from the open parens list while appending the close along with it.
            else:
                tbd_open_parens_index_list.pop()
                balanced_str += c

    #If there are no open parens left unmatched, just return the balanced_str
    if len(tbd_open_parens_index_list) == 0:
        return balanced_str


    #This string will be the return, and is used to catch the indexes of unbalanced open parens.
    fully_balanced_str = ""
    for i, c in enumerate(balanced_str):
        if i in tbd_open_parens_index_list:
            continue
        fully_balanced_str += c
    # Return value is a string that has every open paren closed (left right parity)
    return fully_balanced_str
