#msg = your text
#This function returns ASCII as a List of int value
def encode(msg: str):
    code: list[int] = [ord(c) for c in msg]
    return code

#code = your ASCII list obtained with the encode function
#This function returns text (str)
def decode(code: list[int]):
    decoded: list[str] = [chr(element) for element in code]
    #transform decoded (List) to output (str)
    output: str = "".join(decoded)
    return output
