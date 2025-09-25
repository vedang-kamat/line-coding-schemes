"""
Name : Vedang Kamat
Roll No : 22B-ET-074
Class : BE, SEM VII
Branch : Electronics and Telecommunication Engineering
Goa College of Engineering, Farmagudi
"""

import matplotlib.pyplot as plt

# ========== NRZ-M Encoding Function ==========
def nrzm_encode(bits):
    """NRZ-M encoding: 1 -> invert level, 0 -> keep previous"""
    encoded = []
    current = 1  # starting level (V)
    for b in bits:
        if b == 1:
            current = 0 if current == 1 else 1  # invert
        encoded.append(current)
    return encoded

# ========== Main ==========
def main():
    # Default bitstream
    default_bits = "100000000100001"

    # Input bit sequence (string)
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

    # Apply NRZ-M encoding
    encoded = nrzm_encode(bits)

    # Extend lists by 1 for proper plotting
    x = list(range(n + 1))
    bits_ext = bits + [bits[-1]]         
    encoded_ext = encoded + [encoded[-1]]  

    plt.figure(figsize=(12, 6))

    # ---- Input Bitstream ----
    plt.subplot(2,1,1)
    plt.step(x, bits_ext, where='post', color='black', linewidth=2)
    plt.fill_between(x, bits_ext, step='post', alpha=0.3, color='black')
    plt.ylim(-0.2, 1.2)
    plt.yticks([0,1], ["0","1"])
    plt.xticks(range(n+1))
    plt.xlim(0, n)
    plt.grid(True, linestyle='--', linewidth=0.7, color='gray')
    plt.title("Input Bitstream")

    # ---- NRZ-M Encoded Signal ----
    plt.subplot(2,1,2)
    plt.step(x, encoded_ext, where='post', color='black', linewidth=2)
    plt.fill_between(x, encoded_ext, step='post', alpha=0.3, color='black')
    plt.ylim(-0.2, 1.2)
    plt.yticks([0,1], ["0","V"])
    plt.xticks(range(n+1))
    plt.xlim(0, n)
    plt.grid(True, linestyle='--', linewidth=0.7, color='gray')
    plt.title("NRZ-M Encoded Signal")

    plt.xlabel("Bit Index")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()


