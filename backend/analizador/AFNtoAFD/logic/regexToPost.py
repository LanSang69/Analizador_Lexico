priority = {'*': 3, '?':3, '+':3, '&': 2, '|': 1}
cerraduras = ['*', '?', '+']

def is_alphabet(c):
    return c not in priority.keys() and c not in ['(', ')']

def add_concat_symbol(reg_exp):
    '''
    Replace 'and' operation with ? symbol
    '''
    new_reg_exp = ""
    for current_char in reg_exp:
        if(len(new_reg_exp)>0):
            prev_char = new_reg_exp[len(new_reg_exp)-1]
            if (prev_char == ')' or is_alphabet(prev_char) or prev_char in cerraduras) and (current_char == '('  or is_alphabet(current_char)):
                new_reg_exp += "&"
        new_reg_exp += current_char
    return new_reg_exp

def regex_to_postfix(reg_exp):
    postfix_exp=""
    operator_stack = []
    dictionaryElements = {}

    new_regex = ""
    i = 0
    j = 64
    while i < len(reg_exp):
        prev = j
        if reg_exp[i] != '[':
            new_regex += reg_exp[i]
        else:
            j+=1
            i += 1
            aux = ""
            while reg_exp[i] != ']':
                aux += reg_exp[i]
                i += 1
            dictionaryElements[chr(j)] = aux
        i += 1
        if prev != j:
            new_regex += chr(j)
    reg_exp = new_regex

    reg_exp = add_concat_symbol(reg_exp)
    

    for current_char in reg_exp:
        if is_alphabet(current_char):
            postfix_exp += current_char
        elif current_char == '(':
            operator_stack.append(current_char)
        elif current_char == ')':
            top = operator_stack.pop()
            while top != '(':
                postfix_exp += top
                top = operator_stack.pop()
        else:
            if len(operator_stack) == 0:
                operator_stack.append(current_char)
            else:
                top = operator_stack[len(operator_stack)-1]
                while top!='(' and priority[top] >= priority[current_char]:
                    postfix_exp += top 
                    operator_stack.pop()
                    if len(operator_stack) > 0:
                        top = operator_stack[len(operator_stack)-1]
                    else:
                        break
                operator_stack.append(current_char)
    while len(operator_stack) != 0:
        postfix_exp += operator_stack.pop()

    return postfix_exp, dictionaryElements