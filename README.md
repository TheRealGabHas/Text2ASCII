# Text2ASCII

## Description
This python script ([converter.py](https://github.com/TheRealGabHas/Text2ASCII/blob/main/converter.py)) contains two functions:
- `encode()` is used to return a list of Integer, one item per character in its ASCII form.
- `decode()` is used to do the opposite, it return a string "decoded" from a list of ASCII (int) values.

## How to use
* You can copy the functions contained in [converter.py](https://github.com/TheRealGabHas/Text2ASCII/blob/main/converter.py) inside the script
* Or you can put the script inside the same folder as your python script and import it with the following line:
```py
from converter import *
```


## Examples
encode() function:
```py
# We import the script
>>> from converter import *

>>> encode("Hello World !")
[72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100, 32, 33]
```

decode() function:
```py
# We import the script
>>> from converter import *

>>> decode([72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100, 32, 33])
"Hello World !"
```
