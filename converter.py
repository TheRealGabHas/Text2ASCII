from typing import List


def encode(msg: str):
    code: List[int] = [ord(c) for c in msg]
    print(code)
    return code


def decode(code: List[int]):
    decoded: List[str] = [chr(element) for element in code]
    print(decoded)
    m: str = ""
    for item in decoded:
        m += str(item)
    print(m)


i: str = input("")
decode(encode(i))
