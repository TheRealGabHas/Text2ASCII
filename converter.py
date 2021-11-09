from typing import List

#msg = your text
#This function returns ASCII as a List of int value
def encode(msg: str):
    code: List[int] = [ord(c) for c in msg]
    return code

#code = your ASCII list obtained with the encode function
#This function returns text (str)
def decode(code: List[int]):
    decoded: List[str] = [chr(element) for element in code]
    #transform decoded (List) to output (str)
    output: str = "".join(decoded)
    return output
