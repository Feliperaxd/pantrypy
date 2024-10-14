# -----------------------------------------------------------------------------
# PantryPy
# Copyright (c) 2023 Felipe Amaral dos Santos
# Licensed under the MIT License (see LICENSE file)
# -----------------------------------------------------------------------------

from .commons import AsNumeric
from .internals import (
    ArithmeticsResources, ComparisonsResources,
    FormattingResources, IndexableResources, IterableResources 
)


__all__ = [
    'Coordinates2D',
    'Coordinates3D',
    'Size2D',
    'Size3D',
    'Zone2D',
    'Zone3D'
]

class Coordinates2D(
    ArithmeticsResources, 
    ComparisonsResources, 
    FormattingResources, 
    IndexableResources, 
    IterableResources
):
    """
    An object representing 2D coordinates.
    This object accepts arithmetic and comparison operations, 
    and its defined attributes (x_coord, y_coord) can be indexed and iterated!
    
    Arithmetic operations will result in the same object. Comparative operations 
    will result in a tuple with a boolean value for each respective index. Equal 
    index values will be used for the operations.

    When converted to a string, this object will use the 'formatted' attribute to 
    represent itself.

    Attributes:
    - x_coord (AsNumeric): The X-coordinate value.
    - y_coord (AsNumeric): The Y-coordinate value.
    - formatted (str): A formatted string representation of the coordinates.
    - structure (Tuple[AsNumeric, ...]): A tuple representing the coordinate 
    structure.
    """


    def __init__(
        self: 'Coordinates2D',
        x_coord: AsNumeric,
        y_coord: AsNumeric
    ) -> None:
        
        self.x_coord = x_coord
        self.y_coord = y_coord

        self.formatted = f'{x_coord:+}{y_coord:+}'
        self.structure = (x_coord, y_coord)


class Coordinates3D(
    ArithmeticsResources, 
    ComparisonsResources, 
    FormattingResources, 
    IndexableResources, 
    IterableResources
):
    """
    An object representing 3D coordinates.
    This object accepts arithmetic and comparison operations, 
    and its defined attributes (x_coord, y_coord, z_coord) can be indexed and 
    iterated!
    
    Arithmetic operations will result in the same object. Comparative operations 
    will result in a tuple with a boolean value for each respective index. Equal 
    index values will be used for the operations.

    When converted to a string, this object will use the 'formatted' attribute to 
    represent itself.

    Attributes:
    - x_coord (AsNumeric): The X-coordinate value.
    - y_coord (AsNumeric): The Y-coordinate value.
    - z_coord (AsNumeric): The Z-coordinate value.
    - formatted (str): A formatted string representation of the coordinates.
    - structure (Tuple[AsNumeric, ...]): A tuple representing the coordinate 
    structure.
    """


    def __init__(
        self: 'Coordinates3D',
        x_coord: AsNumeric,
        y_coord: AsNumeric,
        z_coord: AsNumeric
    ) -> None:
        
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.z_coord = z_coord

        self.formatted = f'{x_coord:+}{y_coord:+}{z_coord:+}'
        self.structure = (x_coord, y_coord, z_coord)


class Size2D(
    ArithmeticsResources, 
    ComparisonsResources, 
    FormattingResources, 
    IndexableResources, 
    IterableResources
):
    """
    An object representing 2D size.
    This object accepts arithmetic and comparison operations, 
    and its defined attributes (width, height) can be indexed and iterated!
    
    Arithmetic operations will result in the same object. Comparative operations 
    will result in a tuple with a boolean value for each respective index. Equal 
    index values will be used for the operations.

    When converted to a string, this object will use the 'formatted' attribute to 
    represent itself.

    Attributes:
    - width (AsNumeric): The width value.
    - height (AsNumeric): The height value.
    - formatted (str): A formatted string representation of the size.
    - structure (Tuple[AsNumeric, ...]): A tuple representing the 
    size structure.
    """

    
    def __init__(
        self: 'Size2D',
        width: AsNumeric,
        height: AsNumeric
    ) -> None:
        
        self.width = width
        self.height = height

        self.formatted = f'{width}x{height}'
        self.structure = (width, height) 

class Size3D(
    ArithmeticsResources, 
    ComparisonsResources, 
    FormattingResources, 
    IndexableResources, 
    IterableResources
):
    """
    An object representing 3D size.
    This object accepts arithmetic and comparison operations, 
    and its defined attributes (width, height, length) can be indexed and iterated!
    
    Arithmetic operations will result in the same object. Comparative operations 
    will result in a tuple with a boolean value for each respective index. Equal 
    index values will be used for the operations.

    When converted to a string, this object will use the 'formatted' attribute to 
    represent itself.

    Attributes:
    - width (AsNumeric): The width value.
    - height (AsNumeric): The height value.
    - length (AsNumeric): The length value.
    - formatted (str): A formatted string representation of the size.
    - structure (Tuple[AsNumeric, ...]): A tuple representing the size structure.
    """

    
    def __init__(
        self: 'Size3D',
        width: AsNumeric,
        height: AsNumeric,
        length: AsNumeric
    ) -> None:
        
        self.width = width
        self.height = height
        self.length = length

        self.formatted = f'{width}x{height}x{length}'
        self.structure = (width, height, length) 


class Zone2D(
    ArithmeticsResources, 
    ComparisonsResources, 
    FormattingResources, 
    IndexableResources, 
    IterableResources
):
    """
    An object representing a 2D Zone.
    This object accepts arithmetic and comparison operations, 
    and its defined attributes (x_coord, y_coord, width, height) 
    can be indexed and iterated!

    Arithmetic operations will result in the same object. Comparative operations 
    will result in a tuple with a boolean value for each respective index. Equal 
    index values will be used for the operations.
    
    When converted to a string, this object will use the 'formatted' attribute to 
    represent itself.
    
    Attributes:
    - x_coord (AsNumeric): The X-coordinate value.
    - y_coord (AsNumeric): The Y-coordinate value.
    - width (AsNumeric): The width value.
    - height (AsNumeric): The height value.
    - formatted (str): A formatted string representation of the size.
    - structure (Tuple[AsNumeric, ...]): A tuple representing the size structure.
    """


    def __init__(
        self: 'Zone2D',
        x_coord: AsNumeric,
        y_coord: AsNumeric,
        width: AsNumeric,
        height: AsNumeric,
    ) -> None:
        
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.width = width
        self.height = height

        self.formatted = f'{x_coord:+}{y_coord:+} : {width}x{height}' 
        self.structure = (x_coord, y_coord, width, height)


class Zone3D(
    ArithmeticsResources, 
    ComparisonsResources, 
    FormattingResources, 
    IndexableResources, 
    IterableResources
):
    """
    An object representing a 3D Zone.
    This object accepts arithmetic and comparison operations, 
    and its defined attributes (x_coord, y_coord, z_coord, width, height, length) 
    can be indexed and iterated!

    Arithmetic operations will result in the same object. Comparative operations 
    will result in a tuple with a boolean value for each respective index. Equal 
    index values will be used for the operations.
    
    When converted to a string, this object will use the 'formatted' attribute to 
    represent itself.
    
    Attributes:
    - x_coord (AsNumeric): The X-coordinate value.
    - y_coord (AsNumeric): The Y-coordinate value.
    - z_coord (AsNumeric): The Z-coordinate value.
    - width (AsNumeric): The width value.
    - height (AsNumeric): The height value.
    - length (AsNumeric): The length value.
    - formatted (str): A formatted string representation of the size.
    - structure (Tuple[AsNumeric, ...]): A tuple representing the size structure.
    """


    def __init__(
        self: 'Zone3D',
        x_coord: AsNumeric,
        y_coord: AsNumeric,
        z_coord: AsNumeric,
        width: AsNumeric,
        height: AsNumeric,
        length: AsNumeric
    ) -> None:
        
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.z_coord = z_coord
        self.width = width
        self.height = height
        self.length = length

        self.formatted = (
            f'{x_coord:+}{y_coord:+}{z_coord:+}' + 
            f' : {width}x{height}x{length}'
        )
        self.structure = (
            x_coord, y_coord, z_coord, 
            width, height, length
        )

