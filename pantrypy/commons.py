# -----------------------------------------------------------------------------
# PantryPy
# Copyright (c) 2023 Felipe Amaral dos Santos
# Licensed under the MIT License (see LICENSE file)
# -----------------------------------------------------------------------------

from typing import Any, NewType, Union  

__all__ = [
    # Others
    'AsNumeric',

    # Codes
    'CSharpCode',
    'CSSCode',
    'CPPCode',
    'GoCode',
    'HTMLCode',
    'JavaCode',
    'JavaScriptCode',
    'KotlinCode',
    'MATLABCode',
    'ObjectiveCCode',
    'PerlCode',
    'PHPCode',
    'PythonCode',
    'RCode',
    'RubyCode',
    'RustCode',
    'ScalaCode',
    'ShellScriptCode',
    'SQLQuery',
    'SwiftCode',
    'TypeScriptCode',
    'MarkdownCode',
    
    # Colors
    'ColorName',
    
    'AlphaChannelFloat',
    'AlphaChannelInt',
    'BlackChannelFloat',
    'BlackChannelInt',
    'BlueChannelFloat',
    'BlueChannelInt',
    'BrightnessFloat',
    'BrightnessInt',
    'CyanChannelFloat',
    'CyanChannelInt',
    'GreenChannelFloat',
    'GreenChannelInt',
    'HueFloat',
    'HueInt',
    'MagentaChannelFloat',
    'MagentaChannelInt',
    'RedChannelFloat',
    'RedChannelInt',
    'SaturationFloat',
    'SaturationInt',

    # Operators
    'ArithmeticOperator',
    'AssignmentOperator',
    'BitwiseOperator',
    'ComparisonOperator',
    'LogicalOperator',
    'MembershipOperator',
    'IdentityOperator',

    # IDs
    'IdAny',
    'IdFloat',
    'IdInt',
    'IdStr',

    # Coordinates
    'XCoordinateFloat',
    'XCoordinateInt',

    'YCoordinateFloat',
    'YCoordinateInt',

    'ZCoordinateFloat',
    'ZCoordinateInt',

    # Dimensions
    'LengthFloat',
    'LengthInt',
    
    'WidthFloat',
    'WidthInt',

    'HeightFloat',
    'HeightInt',

    # Aliases
    'AsPath',
    'AsNumeric',
    'AsCollection'
]

# -- Others --
AsNumeric = Union[complex, float, int]
Collection = Union[dict, list, set, tuple]

# -- Queries -- 
SqlQuery = NewType('SqlQuery', str)

# -- Colors --
ColorName = NewType('ColorName', str)

AlphaChannelFloat = NewType('AlphaChannelFloat', float)
AlphaChannelInt = NewType('AlphaChannelInt', int)
BlackChannelFloat = NewType('BlackChannelFloat', float)
BlackChannelInt = NewType('BlackChannelInt', int)
BlueChannelFloat = NewType('BlueChannelFloat', float)
BlueChannelInt = NewType('BlueChannelInt', int)
BrightnessFloat = NewType('BrightnessChannelFloat', float)
BrightnessInt = NewType('BrightnessChannelInt', int)
CyanChannelFloat = NewType('CyanChannelFloat', float)
CyanChannelInt = NewType('CyanChannelInt', int)
GreenChannelFloat = NewType('GreenChannelFloat', float)
GreenChannelInt = NewType('GreenChannelInt', int)
HueFloat = NewType('HueChannelFloat', float)
HueInt = NewType('HueChannelInt', int)
MagentaChannelFloat = NewType('MagentaChannelFloat', float)
MagentaChannelInt = NewType('MagentaChannelInt', int)
RedChannelFloat = NewType('RedChannelFloat', float)
RedChannelInt = NewType('RedChannelInt', int)
SaturationFloat = NewType('SaturationChannelFloat', float)
SaturationInt = NewType('SaturationChannelInt', int)

# -- Operators --
ArithmeticOperator = NewType('ArithmeticOperator', str)
AssignmentOperator = NewType('AssignmentOperator', str)
BitwiseOperator = NewType('BitwiseOperator', str)
ComparisonOperator = NewType('ComparisonOperator', str)
LogicalOperator = NewType('LogicalOperator', str)
MembershipOperator = NewType('MembershipOperator', str)
IdentityOperator = NewType('IdentityOperator', str)

# -- IDs --
IdAny = NewType('IdAny', Any)
IdFloat = NewType('IdFloat', float)
IdInt = NewType('IdInt', int)
IdStr = NewType('IdStr', str)

# -- Coordinates --
XCoordinateFloat = NewType('XCoordinateFloat', float)
XCoordinateInt = NewType('XCoordinateInt', int)

YCoordinateFloat = NewType('YCoordinateFloat', float)
YCoordinateInt = NewType('YCoordinateInt', int)

ZCoordinateFloat = NewType('ZCoordinateFloat', float)
ZCoordinateInt = NewType('ZCoordinateInt', int)

# -- Dimensions --
LengthFloat = NewType('LengthFloat', float)
LengthInt = NewType('LengthInt', int)

WidthFloat = NewType('WidthFloat', float)
WidthInt = NewType('WidthInt', int)

HeightFloat = NewType('HeightFloat', float)
HeightInt = NewType('HeightInt', int)

# -- Aliases --
AsPath = Union[Path, str]
AsNumeric = Union[complex, float, int]
AsCollection = Union[dict, list, set, tuple]
