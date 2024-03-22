# PantryPy
PantryPy is a Python library enhancing type hints and introducing new object annotations, simplifying code clarity and extensibility!

## Installation
To install, use the command `pip install pantrypy` in your terminal!

## Structures
Structures are objects created to represent that type, many of them can have special functionalities such as arithmetic operations or formatting when transformed into strings!
### Color Structures
Objects used to represent colors, each parameter represents its respective channel!
- `CMYKColor`: Used to represent colors in the CMYK model (Cyan, Magenta, Yellow, Black).
- `HexColor`: Used to represent colors in hexadecimal format.
- `HexAColor`: Used to represent colors in hexadecimal format with alpha channel.
- `HSBColor`: Used to represent colors in the HSB model (Hue, Saturation, Brightness).
- `RGBColor`: Used to represent colors in the RGB model (Red, Green, Blue).
- `RGBAColor`: Used to represent colors in the RGB model with alpha channel (Red, Green, Blue, Alpha).
- `RYBColor`: Used to represent colors in the RYB model (Red, Yellow, Blue).

#### Channel Value Limitation
| Color Type | Values                                    |
|------------|---------------------------------------------|
| CMYK       | 0 to 100 - 0 to 100 - 0 to 100 - 0 to 100 |
| Hex        | 00 to FF - 00 to FF - 00 to FF            |
| HexA       | 00 to FF - 00 to FF - 00 to FF - 00 to FF |
| HSB        | 0 to 360 - 0 to 100 - 0 to 100            |
| RGB        | 0 to 255 - 0 to 255 - 0 to 255            |
| RGBA       | 0 to 255 - 0 to 255 - 0 to 255 - 0 to 255 |
| RYB        | 0 to 255 - 0 to 255 - 0 to 255            |

```python
# --Usage!--
cmyk_clr = CMYKColor(99, 0, 43, 1)
hex_clr = HexColor('#03FC90')
hexa_clr = HexAColor('#03FC90FF')
hsb_clr = HSBColor(154, 99, 99)
rgb_clr = RGBColor(3, 252, 144)
rgba_clr = RGBAColor(3, 252, 144, 255)
ryb_clr = RYBColor(3, 252, 144)
```

### Geometry Structures




