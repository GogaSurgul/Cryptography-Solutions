import base64

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def caesar_decrypt(text, shift):
    out = []
    for ch in text:
        if ch.isalpha():
            is_upper = ch.isupper()
            idx = alphabet.index(ch.lower())
            dec = alphabet[(idx - shift) % 26]
            out.append(dec.upper() if is_upper else dec)
        else:
            out.append(ch)
    return ''.join(out)

def brute_force_caesar(text):
    results = []
    for s in range(26):
        results.append((s, caesar_decrypt(text, s)))
    return results

def xor_decrypt(ct_bytes, key_str):
    key = key_str.encode()
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(ct_bytes)])

if __name__ == "__main__":
    # Task 1
    cipher1 = "Hvs Eiwqy Pfckb Tcl Xiadg Cjsf Hvs Zonm Rcu."
    print("=== Caesar brute-force for cipher1 ===")
    for shift, pt in brute_force_caesar(cipher1):
        print(f"{shift:2}: {pt}")
    print("\nBest readable result (manually observed):")
    print("=> The Quick Brown Fox Jumps Over The Lazy Dog.\n")

    # Task 2 - Step 1
    cipher2 = "mznxpz"
    print("=== Caesar brute-force for cipher2 ===")
    for shift, pt in brute_force_caesar(cipher2):
        print(f"{shift:2}: {pt}")

    # From brute-force we see shift 21 -> 'rescue'
    decrypted_cipher2 = caesar_decrypt(cipher2, 21)
    print("\nDecrypted cipher2 (shift 21):", decrypted_cipher2)


    # Step 2: anagram -> 'secure'
    passphrase = "secure"
    print("Recovered passphrase (anagram of 'rescue'):", passphrase)

    # Step 3: XOR decryption
    b64cipher = "Jw0KBlIMAEUXHRdFKyoxVRENEgkPEBwCFkQ="
    ct = base64.b64decode(b64cipher)
    plaintext_bytes = xor_decrypt(ct, passphrase)
    try:
        plaintext = plaintext_bytes.decode('utf-8')
    except UnicodeDecodeError:
        plaintext = repr(plaintext_bytes)
    print("\nXOR-decrypted plaintext:")
    print(plaintext)
