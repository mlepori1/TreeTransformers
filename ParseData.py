'''
These functions read in a the ListOps dataset and return the correct positional encodings
'''
from BinaryTree import Node

# Essentially a shift reduce parser with trivial parenthetical grammar
def parse_exp(exp):

    parse_stack = []

    for e in exp:

        if '[' in e:
            parse_stack.append(Node(e))

        elif ']' in e:
            lc = parse_stack[-1]
            rc = Node(e)
            newNode = Node('')
            newNode.addLeft(lc)
            newNode.addRight(rc)
            del parse_stack[-1]
            if len(parse_stack) == 0:
                return newNode
            else:
                lc = parse_stack[-1]
                rc = newNode
                newNode = Node('')
                newNode.addLeft(lc)
                newNode.addRight(rc)
                parse_stack[-1] = newNode
        else:
            lc = parse_stack[-1]
            rc = Node(e)
            newNode = Node('')
            newNode.addLeft(lc)
            newNode.addRight(rc)
            parse_stack[-1] = newNode
    return -1

# Determines tree position
def pos_in_tree(node, pos, results):
    if node.hasChildren():
        pos_in_tree(node.getLeft(), "0" + pos, results)
        pos_in_tree(node.getRight(), "1" + pos, results)
    else:
        results.append("1" + pos)


# Binary string to decimal conversion
def bin_to_dec(bin_str):
    dec = 0
    for i in range(len(bin_str)):
        if bin_str[-(i+1)] == "1":
            dec += 2**i
    return dec

# Driver function
def parse (text):
    text = text.replace('(', '')
    text = text.replace(')', '')
    expressions = text.split("\n")
    parsed = []
    i = 0
    for e in expressions:
        if len(e) != 0 and "[" in e:
            answer = e[0]
            e = e[1:].split()
            tree = parse_exp(e)
            result = []
            pos_in_tree(tree, "", result)
            tree_dec = [bin_to_dec(bin_str) for bin_str in result]
            parsed.append([answer, e, tree_dec])

    return parsed
