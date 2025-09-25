"""
Name : Vedang Kamat
Roll No : 22B-ET-074
Class : BE, SEM VII
Branch : Electronics and Telecommunication Engineering
Goa College of Engineering, Farmagudi
"""

import matplotlib.pyplot as plt

# ========== HDB3 Encoding Function ==========
def hdb3_encode(bits):
    """
    HDB3 (High-Density Bipolar-3) encoding:
    - Based on AMI
    - Substitutes runs of 4 zeros with 000V or B00V
    """
    encoded = []
    last_polarity = -1
    nonzero_count = 0
    zero_count = 0
    n = len(bits)

    for i in range(n):
        if bits[i] == 1:
            # Flush pending zeros
            for z in range(zero_count):
                encoded.append(0)
            zero_count = 0

            # Normal AMI rule
            last_polarity = -last_polarity
            encoded.append(last_polarity)
            nonzero_count += 1
        else:
            zero_count += 1
            if zero_count == 4:
                if nonzero_count % 2 == 0:
                    # B00V substitution
                    b = 1 if last_polarity == -1 else -1
                    v = 1 if last_polarity == -1 else -1
                    encoded.append(b)   # B
                    encoded.append(0)   # 0
                    encoded.append(0)   # 0
                    encoded.append(v)   # V
                    last_polarity = -last_polarity
                    nonzero_count += 2
                else:
                    # 000V substitution
                    v = last_polarity
                    encoded.append(0)
                    encoded.append(0)
                    encoded.append(0)
                    encoded.append(v)
                    nonzero_count += 1
                zero_count = 0

    # Flush trailing zeros
    for z in range(zero_count):
        encoded.append(0)

    return encoded


# ========== Main ==========
def main():
    # Default bitstream
    default_bits = "100000000100001"

    # Input bit sequence
    input_str = input(f"Enter the bit sequence [default: {default_bits}]: ").strip()
    if input_str == "":
        input_str = default_bits

    # Convert to integer list
    try:
        bits = [int(ch) for ch in input_str]
        if any(b not in (0,1) for b in bits):
            raise ValueError
    except ValueError:
        print("Invalid input! Only 0s and 1s allowed.")
        return

    n = len(bits)

    # Apply HDB3 encoding
    encoded = hdb3_encode(bits)

    # Time axis for plotting
    x_bits = list(range(n + 1))
    bits_ext = bits + [bits[-1]]

    x_encoded = list(range(len(encoded) + 1))
    encoded_ext = encoded + [encoded[-1]]

    plt.figure(figsize=(12, 6))

    # ---- Input Bitstream ----
    plt.subplot(2,1,1)
    plt.step(x_bits, bits_ext, where='post', color='black', linewidth=2)
    plt.fill_between(x_bits, bits_ext, step='post', alpha=0.3, color='black')
    plt.ylim(-0.2, 1.2)
    plt.yticks([0,1], ["0","1"])
    plt.xticks(range(n+1))
    plt.xlim(0, n)
    plt.grid(True, linestyle='--', linewidth=0.7, color='gray')
    plt.title("Input Bitstream")

    # ---- HDB3 Encoded Signal ----
    plt.subplot(2,1,2)
    plt.step(x_encoded, encoded_ext, where='post', color='black', linewidth=2)
    plt.fill_between(x_encoded, encoded_ext, step='post', alpha=0.3, color='black')
    plt.ylim(-1.2, 1.2)
    plt.yticks([-1,0,1], ["-V","0","+V"])
    plt.xticks(range(len(encoded)+1))
    plt.xlim(0, len(encoded))
    plt.grid(True, linestyle='--', linewidth=0.7, color='gray')
    plt.title("HDB3 Encoded Signal")

    plt.xlabel("Bit Index")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()


