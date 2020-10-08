comparisons = {
    '<': 'blt',
    '<=': 'ble',
    '>': 'bgt',
    '>=': 'bge',
    '==': 'beq'
}

if_options = {
    'if_else': 'cmp $reg1, $reg2\n$comp $t_true\nb $t_false',
    'only_if': 'cmp $reg1, $reg2\n$comp $t_true'
}

while_options = {
    'while': 'cmp $reg1, $reg2\n$comp $t_true'
}