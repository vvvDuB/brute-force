def word_match(text: str) -> int:
    COMMON_ENGLISH = ["the", "and", "of", "to", "a", "in", "is", "it", "you", "that"]
    
    words = text.split(" ")
    counter = 0
    for w in words:
        if w in COMMON_ENGLISH:
            counter += 1
    
    return counter 

def brute_force(text: str) -> str:
    decrypted = []
    
    for key in range(26):
        result = []
        shift = key % 26

        for c in text:
            if ("A" <= c <= "Z") or ("a" <= c <= "z"):
                base = ord("A") if c.isupper() else ord("a")
                shifted = (ord(c) - base + shift) % 26
                result.append(chr(base + shifted))
            else:
                result.append(c)
        
        t = (key, "".join(result))
        decrypted.append(t)

    return decrypted

def main()-> None:
    text = input("Dammi una frase: ")
    
    decrypted = brute_force(text)
    for el in decrypted:
        w_count = word_match(el[1])
        if w_count:
            print(f"Key = {el[0]}") 
            print(f"{el[1]}")

if __name__ == "__main__":
    main()
