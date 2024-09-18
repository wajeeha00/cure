def rabin_karp(pattern, text):
    # Constants for hash calculation
    p = 10**9 + 7  # A large prime number
    x = 263  # A base number used in hash function

    def poly_hash(s, prime, multiplier):
        """Computes the hash of a string s."""
        hash_value = 0
        for c in reversed(s):
            hash_value = (hash_value * multiplier + ord(c)) % prime
        return hash_value

    def precompute_hashes(text, pattern_len, prime, multiplier):
        """Precomputes the hashes of all substrings of length pattern_len in text."""
        T = len(text)
        H = [0] * (T - pattern_len + 1)
        # Compute the hash of the last substring of length pattern_len
        S = text[T - pattern_len:T]
        H[T - pattern_len] = poly_hash(S, prime, multiplier)
        # Precompute the highest power of x needed
        y = 1
        for i in range(pattern_len):
            y = (y * multiplier) % prime
        # Use a rolling hash to compute the rest
        for i in range(T - pattern_len - 1, -1, -1):
            H[i] = (multiplier * H[i + 1] + ord(text[i]) - y * ord(text[i + pattern_len])) % prime
        return H

    # Step 1: Compute the hash of the pattern
    p_len = len(pattern)
    t_len = len(text)
    pattern_hash = poly_hash(pattern, p, x)

    # Step 2: Precompute the hashes of all substrings of text
    H = precompute_hashes(text, p_len, p, x)

    # Step 3: Compare the pattern hash with all precomputed hashes
    result = []
    for i in range(t_len - p_len + 1):
        if pattern_hash == H[i]:
            # Confirm the match to avoid spurious hits
            if text[i:i + p_len] == pattern:
                result.append(i)

    return result

# Example Usage
pattern = input()
text = input()
result = rabin_karp(pattern, text)
print(" ".join(map(str, result)))