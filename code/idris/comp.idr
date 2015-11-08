module comp

data color = red | green | blue | magenta | cyan | yellow

complement: color -> color
complement red = cyan
complement yellow = blue
complement green = magenta
complement cyan = red
complement blue = yellow
complement _ = green
