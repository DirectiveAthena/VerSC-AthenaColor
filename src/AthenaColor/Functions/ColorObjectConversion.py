# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library

# Custom Packages
from AthenaColor.Objects.ColorSystems.Opaque import (
    RGB ,
    HEX ,
    CMYK,
    HSL ,
    HSV
)
from AthenaColor.Objects.ColorSystems.Transparent import (
    RGBA ,
    HEXA ,
)
import AthenaColor.Functions.ColorTupleConversion as CTC

# ----------------------------------------------------------------------------------------------------------------------
# - OPAQUE COLORS -
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# - RGB -
# ----------------------------------------------------------------------------------------------------------------------
def to_RGB(color:RGB|HEX|CMYK|HSL|HSV) -> RGB:
    if isinstance(color, RGB):
        return color
    elif isinstance(color, HEX):
        return RGB(r=color.r,g=color.g,b=color.b)
    elif isinstance(color, HSV):
        return RGB(*CTC.hsv_to_rgb(h=color.h, s=color.s, v=color.v))
    elif isinstance(color, HSL):
        return RGB(*CTC.hsl_to_rgb(h=color.h, s=color.s, l=color.l))
    elif isinstance(color, CMYK):
        return RGB(*CTC.cmyk_to_rgb(c=color.c, m=color.m, y=color.y, k=color.k))
    else:
        raise ValueError(f"No known Opaque Color system: {color=}")

# ----------------------------------------------------------------------------------------------------------------------
# - Hexadecimal -
# ----------------------------------------------------------------------------------------------------------------------
def to_HEX(color:RGB|HEX|CMYK|HSL|HSV) -> HEX:
    if isinstance(color, RGB):
        return HEX(CTC.rgb_to_hex(r=color.r, g=color.g, b=color.b))
    elif isinstance(color, HEX):
        return color
    elif isinstance(color, HSV):
        return HEX(*CTC.hsv_to_hex(h=color.h, s=color.s, v=color.v))
    elif isinstance(color, HSL):
        return HEX(*CTC.hsl_to_hex(h=color.h, s=color.s, l=color.l))
    elif isinstance(color, CMYK):
        return HEX(*CTC.cmyk_to_hex(c=color.c, m=color.m, y=color.y, k=color.k))
    else:
        raise ValueError(f"No known Opaque Color system: {color=}")

# ----------------------------------------------------------------------------------------------------------------------
# - HSV -
# ----------------------------------------------------------------------------------------------------------------------
def to_HSV(color:RGB|HEX|CMYK|HSL|HSV) -> HSV:
    if isinstance(color, RGB):
        return HSV(*CTC.rgb_to_hsv(r=color.r, g=color.g, b=color.b))
    elif isinstance(color, HEX):
        return HSV(*CTC.hex_to_hsv(str(color)))
    elif isinstance(color, HSV):
        return color
    elif isinstance(color, HSL):
        return HSV(*CTC.hsl_to_hsv(h=color.h, s=color.s, l=color.l))
    elif isinstance(color, CMYK):
        return HSV(*CTC.cmyk_to_hsv(c=color.c, m=color.m, y=color.y, k=color.k))
    else:
        raise ValueError(f"No known Opaque Color system: {color=}")

# ----------------------------------------------------------------------------------------------------------------------
# - HSL -
# ----------------------------------------------------------------------------------------------------------------------
def to_HSL(color:RGB|HEX|CMYK|HSL|HSV) -> HSL:
    if isinstance(color, RGB):
        return HSL(*CTC.rgb_to_hsl(r=color.r, g=color.g, b=color.b))
    elif isinstance(color, HEX):
        return HSL(*CTC.hex_to_hsl(str(color)))
    elif isinstance(color, HSV):
        return HSL(*CTC.hsv_to_hsl(h=color.h, s=color.s, v=color.v))
    elif isinstance(color, HSL):
        return color
    elif isinstance(color, CMYK):
        return HSL(*CTC.cmyk_to_hsl(c=color.c, m=color.m, y=color.y, k=color.k))
    else:
        raise ValueError(f"No known Opaque Color system: {color=}")

# ----------------------------------------------------------------------------------------------------------------------
# - CMYK -
# ----------------------------------------------------------------------------------------------------------------------
def to_CMYK(color:RGB|HEX|CMYK|HSL|HSV) -> CMYK:
    if isinstance(color, RGB):
        return CMYK(*CTC.rgb_to_cmyk(r=color.r, g=color.g, b=color.b))
    elif isinstance(color, HEX):
        return CMYK(*CTC.hex_to_cmyk(str(color)))
    elif isinstance(color, HSV):
        return CMYK(*CTC.hsv_to_cmyk(h=color.h, s=color.s, v=color.v))
    elif isinstance(color, HSL):
        return CMYK(*CTC.hsl_to_cmyk(h=color.h, s=color.s, l=color.l))
    elif isinstance(color, CMYK):
        return color
    else:
        raise ValueError(f"No known Opaque Color system: {color=}")

# ----------------------------------------------------------------------------------------------------------------------
# - TRANSPARENT COLORS -
# ----------------------------------------------------------------------------------------------------------------------A
def to_RGBA(color:RGBA|HEXA) -> RGBA:
    if isinstance(color, RGBA):
        return color
    elif isinstance(color, HEXA):
        return RGBA(*CTC.hexa_to_rgba(str(color)))
    else:
        raise ValueError(f"No known Transparent Color system: {color=}")

def to_HEXA(color:RGBA|HEXA) -> HEXA:
    if isinstance(color, RGBA):
        return HEXA(*CTC.rgba_to_hexa(r=color.r, g=color.g, b=color.b, a=color.a))
    elif isinstance(color, HEXA):
        return color
    else:
        raise ValueError(f"No known Transparent Color system: {color=}")
