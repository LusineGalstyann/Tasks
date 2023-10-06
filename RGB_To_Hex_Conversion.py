def hex_element(color):

    color = 255 if color > 255 else color
    color = 0 if color < 0 else color
    rgb='0'+hex(color).upper()[2::] if len(hex(color)[2::])==1 else hex(color).upper()[2::]
    return rgb

def rgb(r, g, b):
    hex_rgb = ''
    hex_rgb+=hex_element(r)
    hex_rgb += hex_element(g)
    hex_rgb += hex_element(b)
    return hex_rgb
