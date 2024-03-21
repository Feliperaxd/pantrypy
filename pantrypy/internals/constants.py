# -----------------------------------------------------------------------------
# PantryPy
# Copyright (c) 2023 Felipe Amaral dos Santos
# Licensed under the MIT License (see LICENSE file)
# -----------------------------------------------------------------------------


__all__ = [
    'ARITHMETIC_OPERATORS',
    'ASSIGNMENT_OPERATORS',
    'BITWISE_OPERATORS',
    'COMPARISION_OPERATORS',
    'LOGICAL_OPERATORS',
    'MEMBERSHIP_OPERATORS',
    'IDENTITY_OPERATORS'
]

ARITHMETIC_OPERATORS = [
    '+', '-', '*', 
    '/', '//', '%', 
    '**'
]
ASSIGNMENT_OPERATORS = [
    '=', '+=', '-=', 
    '*=', '/=', '//=', 
    '%=', ':='
]
BITWISE_OPERATORS = [
    '&', '|', '^', 
    '~', '<<', '>>'
]
COMPARISION_OPERATORS = [
    '==', '!=', '<', 
    '>', '<=', '>='
]
LOGICAL_OPERATORS = [
    'and', 'or', 'not'
]
MEMBERSHIP_OPERATORS = [
    'in', 'not in'
]
IDENTITY_OPERATORS = [
    'is', 'not is'
]
