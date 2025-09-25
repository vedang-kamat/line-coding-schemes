"""
Name : Vedang Kamat
Roll No : 22B-ET-074
Class : BE, SEM VII
Branch : Electronics and Telecommunication Engineering
Goa College of Engineering, Farmagudi
"""

import matplotlib.pyplot as plt

# ========== Encoding Function ==========
def unipolar_rz(bits):
    """
    Unipolar Return-to-Zero (RZ) encoding:
    - '1' → +V in first half, 0 in second half
    - '0' → 0 in both halves
    """
    encoded = []
    for b in bits:
        if b == 1:
            encoded.extend([1, 0])  # +V then 0
        else:
            encoded.extend([0, 0])  # stays 0
    return encoded

# ========== Main ==========
def main():
    # Default bitstream
    default_bits = "100000000100001"

    # Input bit sequence (string)
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

    # Apply Unipolar RZ encoding
    encoded = unipolar_rz(bits)

    # ---- Input Bitstream extension ----
    x_bits = list(range(n + 1))
    bits_ext = bits + [bits[-1]]

    # ---- Encoded Signal extension (keep same axis length) ----
    x_encoded = [i * 0.5 for i in range(len(encoded) + 1)]
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

    # ---- Unipolar RZ Encoded Signal ----
    plt.subplot(2,1,2)
    plt.step(x_encoded, encoded_ext, where='post', color='black', linewidth=2)
    plt.fill_between(x_encoded, encoded_ext, step='post', alpha=0.3, color='black')
    plt.ylim(-0.2, 1.2)
    plt.yticks([0,1], ["0","+V"])
    plt.xticks(range(n+1))  # same ticks as input
    plt.xlim(0, n)
    plt.grid(True, linestyle='--', linewidth=0.7, color='gray')
    plt.title("Unipolar RZ Encoded Signal")

    plt.xlabel("Bit Index")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()


