from typing import List

#msg = your text. It will return ASCII
def encode(msg: str):
    code: List[int] = [ord(c) for c in msg]
    print(code) 
    return code

#code = your ASCII list obtained with the encode function
def decode(code: List[int]):
    decoded: List[str] = [chr(element) for element in code]
    print(decoded)
    m: str = ""
    #transform decoded (List) to m (str)
    for item in decoded:
        m += str(item)
    print(m)

# To test the code
#i: str = input("")
#decode(encode(i))
