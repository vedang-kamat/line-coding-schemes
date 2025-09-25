"""
Name : Vedang Kamat
Roll No : 22B-ET-074
Class : BE, SEM VII
Branch : Electronics and Telecommunication Engineering
Goa College of Engineering, Farmagudi
"""

import matplotlib.pyplot as plt

# ========== Biphase-S Encoding Function ==========
def biphases_encode(bits):
    """
    Biphase-S encoding:
    - Each bit has two half-bit slots
    - Always transition at start of bit
    - If bit is 0, additional transition in middle
    """
    encoded = []
    prev = 0  # starting level (V)
    for b in bits:
        # transition at start
        prev = 0 if prev == 1 else 1
        encoded.append(prev)
        # middle transition for 0
        if b == 0:
            prev = 0 if prev == 1 else 1
        encoded.append(prev)
    return encoded

# ========== Main ==========
def main():
    # Default bitstream
    default_bits = "100000000100001"

    # Input bit sequence
    input_str = input("Enter the bit sequence [default: 100000000100001]: ").strip()
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

    # Apply Biphase-S encoding
    encoded = biphases_encode(bits)

    # Time axis for plotting
    x_bits = list(range(n + 1))
    bits_ext = bits + [bits[-1]]

    x_encoded = [i*0.5 for i in range(len(encoded)+1)]  # two half-bit slots per bit
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

    # ---- Biphase-S Encoded Signal ----
    plt.subplot(2,1,2)
    plt.step(x_encoded, encoded_ext, where='post', color='black', linewidth=2)
    plt.fill_between(x_encoded, encoded_ext, step='post', alpha=0.3, color='black')
    plt.ylim(-0.2, 1.2)
    plt.yticks([0,1], ["0","V"])
    plt.xticks(range(n+1))
    plt.xlim(0, n)
    plt.grid(True, linestyle='--', linewidth=0.7, color='gray')
    plt.title("Biphase-S Encoded Signal")

    plt.xlabel("Bit Index")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()

