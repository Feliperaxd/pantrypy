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
    'CMYKColor',
    'HexColor',
    'HexAColor',
    'HSBColor',
    'RGBColor',
    'RGBAColor',
    'RYBColor'
] 

class CMYKColor(
    ArithmeticsResources, 
    ComparisonsResources, 
    FormattingResources, 
    IndexableResources, 
    IterableResources
):
    """
    An object representing a CMYK color.
    This object accepts arithmetic and comparison operations, 
    and its defined attributes (c_channel, m_channel, y_channel, k_channel) 
    can be indexed and iterated!

    Arithmetic operations will result in the same object. Comparative operations 
    will result in a tuple with a boolean value for each respective index. Equal 
    index values will be used for the operations.
    
    When converted to a string, this object will use the 'formatted' attribute to 
    represent itself.
    
    Channels c, m, y, k only accept ranges from 0 to 100, smaller or larger values 
    will be transformed into the nearest accepted value.

    Attributes:
    - c_channel (AsNumeric): The cyan channel value.
    - m_channel (AsNumeric): The magenta channel value.
    - y_channel (AsNumeric): The yellow channel value.
    - k_channel (AsNumeric): The black channel value.
    - formatted (str): A formatted string showing the channels.
    - structure (Tuple[AsNumeric, ...]): A tuple representing the color structure.
    """


    def __init__(
        self: 'CMYKColor',
        c_channel: AsNumeric,
        m_channel: AsNumeric,
        y_channel: AsNumeric,
        k_channel: AsNumeric
    ) -> None:
        
        self.c_channel = max(0, min(100, c_channel))
        self.m_channel = max(0, min(100, m_channel))
        self.y_channel = max(0, min(100, y_channel))
        self.k_channel = max(0, min(100, k_channel))

        self.formatted = (
            f'C:{self.c_channel}% M:{self.m_channel}% ' + 
            f'Y:{self.y_channel}% K:{self.k_channel}%'
        )
        self.structure = (
            self.c_channel, self.m_channel, 
            self.y_channel, self.k_channel
        )


class HexColor( 
    FormattingResources
):
    """
    An object representing a hexadecimal color.
    
    When converted to a string, this object will use the 'formatted' attribute to 
    represent itself.
    
    Attributes:
    - value (str): The color code. only accepts colors with 3 channels, 
    in this case 6 characters
    - formatted (str): A formatted string showing the color code.
    - structure (Tuple[str, str, str]): A tuple representing the color structure.
    """


    def __init__(
        self: 'HexColor',
        value: str
    ) -> None:
        
        self.value = str(value).removeprefix('#')
        self.value = self.value.upper()
        
        if len(self.value) != 6:
            raise ValueError(
                (
                    'Invalid hex color format. Expected 6 characters representing 3 channels, ' 
                    f'received {len(self.value)} characters!'
                )
            )

        self.r_channel = self.value[0] + self.value[1]
        self.g_channel = self.value[2] + self.value[3]
        self.b_channel = self.value[4] + self.value[5]

        self.formatted = f'#{self.value}'
        self.structure = (self.r_channel, self.g_channel, self.b_channel)


class HexAColor( 
    FormattingResources
):
    """
    An object representing a hexadecimal color with alpha channel.
    
    When converted to a string, this object will use the 'formatted' attribute to 
    represent itself.
    
    Attributes:
    - value (str): The color code. only accepts colors with 4 channels, 
    in this case 8 characters
    - formatted (str): A formatted string showing the color code.
    - structure (Tuple[str, str, str, str]): A tuple representing the color structure.
    """


    def __init__(
        self: 'HexAColor',
        value: str
    ) -> None:
        
        self.value = str(value).removeprefix('#')
        self.value = self.value.upper()
        
        if len(self.value) != 8:
            raise ValueError(
                (
                    'Invalid hex color format. Expected 8 characters representing 4 channels, ' 
                    f'received {len(self.value)} characters!'
                )
            )

        self.r_channel = self.value[0] + self.value[1]
        self.g_channel = self.value[2] + self.value[3]
        self.b_channel = self.value[4] + self.value[5]
        self.a_channel = self.value[6] + self.value[7]

        self.formatted = f'#{self.value}'
        self.structure = (
            self.r_channel, self.g_channel, 
            self.b_channel, self.a_channel
        )


class HSBColor(
    ArithmeticsResources, 
    ComparisonsResources, 
    FormattingResources, 
    IndexableResources, 
    IterableResources
):
    """
    An object representing a HSB color.
    This object accepts arithmetic and comparison operations, 
    and its defined attributes (hue, saturation, brightness) 
    can be indexed and iterated!

    Arithmetic operations will result in the same object. Comparative operations 
    will result in a tuple with a boolean value for each respective index. Equal 
    index values will be used for the operations.
    
    When converted to a string, this object will use the 'formatted' attribute to 
    represent itself.
    
    'saturation', 'brightness' only accept ranges from 0 to 100 and 'hue' only ranges 
    from 0 to 360, smaller or larger values will be transformed into the 
    nearest accepted value.

    Attributes:
    - hue (AsNumeric): The hue of color.
    - saturation (AsNumeric): The saturation of color.
    - brightness (AsNumeric): The brightness of color.
    - formatted (str): A formatted string showing the color characteristics.
    - structure (Tuple[AsNumeric, ...]): A tuple representing color characteristics.
    """

    
    def __init__(
        self: 'HSBColor',
        hue: AsNumeric,
        saturation: AsNumeric,
        brightness: AsNumeric,
    ) -> None:

        self.hue = max(0, min(360, hue))
        self.saturation = max(0, min(100, saturation))
        self.brightness = max(0, min(100, brightness))

        self.formatted = (
            f'Hue:{self.hue} Saturation:{self.saturation} ' +
            f'Brightness:{self.brightness}'
        )
        self.structure = (self.hue, self.saturation, self.brightness)


class RGBColor(
    ArithmeticsResources, 
    ComparisonsResources, 
    FormattingResources, 
    IndexableResources, 
    IterableResources
):
    """
    An object representing a RGB color.
    This object accepts arithmetic and comparison operations, 
    and its defined attributes (r_channel, g_channel, b_channel) 
    can be indexed and iterated!

    Arithmetic operations will result in the same object. Comparative operations 
    will result in a tuple with a boolean value for each respective index. Equal 
    index values will be used for the operations.
    
    When converted to a string, this object will use the 'formatted' attribute to 
    represent itself.
    
    Channels r, g, b only accept ranges from 0 to 255, smaller or larger values 
    will be transformed into the nearest accepted value.

    Attributes:
    - r_channel (AsNumeric): The red channel value.
    - g_channel (AsNumeric): The green channel value.
    - b_channel (AsNumeric): The blue channel value.
    - formatted (str): A formatted string showing the channels.
    - structure (Tuple[AsNumeric, ...]): A tuple representing color structure.
    """

    def __init__(
        self: 'RGBColor',
        r_channel: AsNumeric,
        g_channel: AsNumeric,
        b_channel: AsNumeric,
    ) -> None:

        self.r_channel = max(0, min(255, r_channel))
        self.g_channel = max(0, min(255, g_channel))
        self.b_channel = max(0, min(255, b_channel))

        self.formatted = f'R:{self.r_channel} G:{self.g_channel} B:{self.b_channel}'
        self.structure = (self.r_channel, self.g_channel, self.b_channel)
        

class RGBAColor(
    ArithmeticsResources, 
    ComparisonsResources, 
    FormattingResources, 
    IndexableResources, 
    IterableResources
):
    """
    An object representing a RGBA color.
    This object accepts arithmetic and comparison operations, 
    and its defined attributes (r_channel, g_channel, b_channel, a_channel) 
    can be indexed and iterated!

    Arithmetic operations will result in the same object. Comparative operations 
    will result in a tuple with a boolean value for each respective index. Equal 
    index values will be used for the operations.
    
    When converted to a string, this object will use the 'formatted' attribute to 
    represent itself.
    
    Channels r, g, b, a only accept ranges from 0 to 255, smaller or larger values 
    will be transformed into the nearest accepted value.

    Attributes:
    - r_channel (AsNumeric): The red channel value.
    - g_channel (AsNumeric): The green channel value.
    - b_channel (AsNumeric): The blue channel value.
    - a_channel (AsNumeric): The alpha channel value.
    - formatted (str): A formatted string showing the channels.
    - structure (Tuple[AsNumeric, ...]): A tuple representing the color structure.
    """


    def __init__(
        self: 'RGBAColor',
        r_channel: AsNumeric,
        g_channel: AsNumeric,
        b_channel: AsNumeric,
        a_channel: AsNumeric
    ) -> None:
        
        self.r_channel = max(0, min(255, r_channel))
        self.g_channel = max(0, min(255, g_channel))
        self.b_channel = max(0, min(255, b_channel))
        self.a_channel = max(0, min(255, a_channel))

        self.formatted = (
            f'R:{self.r_channel} G:{self.g_channel} ' + 
            f'B:{self.b_channel} A:{self.a_channel}'
        )
        self.structure = (
            self.r_channel, self.g_channel, 
            self.b_channel, self.a_channel
        )


class RYBColor(
    ArithmeticsResources, 
    ComparisonsResources, 
    FormattingResources, 
    IndexableResources, 
    IterableResources
):
    """
    An object representing a RYB color.
    This object accepts arithmetic and comparison operations, 
    and its defined attributes (r_channel, y_channel, b_channel) 
    can be indexed and iterated!

    Arithmetic operations will result in the same object. Comparative operations 
    will result in a tuple with a boolean value for each respective index. Equal 
    index values will be used for the operations.
    
    When converted to a string, this object will use the 'formatted' attribute to 
    represent itself.
    
    Channels r, y, b only accept ranges from 0 to 255, smaller or larger values 
    will be transformed into the nearest accepted value.

    Attributes:
    - r_channel (AsNumeric): The red channel value.
    - y_channel (AsNumeric): The yellow channel value.
    - b_channel (AsNumeric): The blue channel value.
    - formatted (str): A formatted string showing the channels.
    - structure (Tuple[AsNumeric, ...]): A tuple representing color structure.
    """

    
    def __init__(
        self: 'RYBColor',
        r_channel: AsNumeric,
        y_channel: AsNumeric,
        b_channel: AsNumeric,
    ) -> None:

        self.r_channel = max(0, min(255, r_channel))
        self.y_channel = max(0, min(255, y_channel))
        self.b_channel = max(0, min(255, b_channel))

        self.formatted = f'R:{self.r_channel} Y:{self.y_channel} B:{self.b_channel}'
        self.structure = (self.r_channel, self.y_channel, self.b_channel)
