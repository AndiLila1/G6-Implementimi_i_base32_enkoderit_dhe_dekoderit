alfabeti_dhe_numrat = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"
def base32_to_bits(text: str) -> str:
  bits = ""
  for char in text:
    index = alfabeti_dhe_numrat.index(char)
    bits += f"{index:05b}"
    return bits
def decode_base32(text: str) -> bytes:
  
