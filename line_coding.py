"""
Name : Vedang Kamat
Roll No : 22B-ET-074
Class : BE, SEM VII
Branch : Electronics and Telecommunication Engineering
Goa College of Engineering, Farmagudi
"""

import matplotlib.pyplot as plt

# ====================================================
# Encoding Functions
# ====================================================

def ami_encode(bits):
    """AMI (Alternate Mark Inversion)"""
    encoded, prev = [], -1
    for b in bits:
        if b == 0:
            encoded.append(0)
        else:
            prev = 1 if prev == -1 else -1
            encoded.append(prev)
    return encoded

def b8zs_encode(bits):
    """B8ZS (Bipolar with 8-Zero Substitution)"""
    encoded, last_polarity, zero_count = [], -1, 0
    for b in bits:
        if b == 1:
            encoded.extend([0]*zero_count)
            zero_count = 0
            last_polarity = -last_polarity
            encoded.append(last_polarity)
        else:
            zero_count += 1
            if zero_count == 8:
                if last_polarity == 1:
                    encoded.extend([0,0,0,+1,-1,0,-1,+1])
                    last_polarity = +1
                else:
                    encoded.extend([0,0,0,-1,+1,0,+1,-1])
                    last_polarity = -1
                zero_count = 0
    encoded.extend([0]*zero_count)
    return encoded

def hdb3_encode(bits):
    """HDB3 (High-Density Bipolar-3)"""
    encoded, last_polarity, nonzero_count, zero_count = [], -1, 0, 0
    for b in bits:
        if b == 1:
            encoded.extend([0]*zero_count)
            zero_count = 0
            last_polarity = -last_polarity
            encoded.append(last_polarity)
            nonzero_count += 1
        else:
            zero_count += 1
            if zero_count == 4:
                if nonzero_count % 2 == 0:
                    b = 1 if last_polarity == -1 else -1
                    v = 1 if last_polarity == -1 else -1
                    encoded.extend([b,0,0,v])
                    last_polarity = -last_polarity
                    nonzero_count += 2
                else:
                    v = last_polarity
                    encoded.extend([0,0,0,v])
                    nonzero_count += 1
                zero_count = 0
    encoded.extend([0]*zero_count)
    return encoded

def manchester_encode(bits):
    """Manchester: 0 → low-high, 1 → high-low"""
    encoded = []
    for b in bits:
        encoded.extend([0,1] if b == 0 else [1,0])
    return encoded

def diff_manchester_encode(bits):
    """Differential Manchester"""
    encoded, prev = [], 1
    for b in bits:
        if b == 0:
            prev = 0 if prev == 1 else 1
        encoded.append(prev)
        prev = 0 if prev == 1 else 1
        encoded.append(prev)
    return encoded

def biphasem_encode(bits):
    """Biphase-M: transition at start; extra transition for 1"""
    encoded, prev = [], 0
    for b in bits:
        prev = 0 if prev == 1 else 1
        encoded.append(prev)
        if b == 1:
            prev = 0 if prev == 1 else 1
        encoded.append(prev)
    return encoded

def biphases_encode(bits):
    """Biphase-S: transition at start; extra transition for 0"""
    encoded, prev = [], 0
    for b in bits:
        prev = 0 if prev == 1 else 1
        encoded.append(prev)
        if b == 0:
            prev = 0 if prev == 1 else 1
        encoded.append(prev)
    return encoded

def nrzl_encode(bits):
    """Unipolar NRZ-L"""
    return [1 if b == 1 else 0 for b in bits]

def nrzm_encode(bits):
    """NRZ-M: 1 → invert, 0 → keep"""
    encoded, current = [], 1
    for b in bits:
        if b == 1:
            current = 0 if current == 1 else 1
        encoded.append(current)
    return encoded

def nrzs_encode(bits):
    """NRZ-S: 0 → invert, 1 → keep"""
    encoded, current = [], 0
    for b in bits:
        if b == 0:
            current = 0 if current == 1 else 1
        encoded.append(current)
    return encoded

def unipolar_rz(bits):
    """Unipolar RZ: 1 → [1,0], 0 → [0,0]"""
    encoded = []
    for b in bits:
        encoded.extend([1,0] if b == 1 else [0,0])
    return encoded


# ====================================================
# Main
# ====================================================

def main():
    encodings = {
        "1": ("Unipolar NRZ-L", nrzl_encode, "unipolar"),
        "2": ("Unipolar NRZ-M", nrzm_encode, "unipolar"),
        "3": ("Unipolar NRZ-S", nrzs_encode, "unipolar"),
        "4": ("Unipolar RZ", unipolar_rz, "rz"),
        "5": ("Manchester", manchester_encode, "rz"),
        "6": ("Differential Manchester", diff_manchester_encode, "rz"),
        "7": ("Biphase-M", biphasem_encode, "rz"),
        "8": ("Biphase-S", biphases_encode, "rz"),
        "9": ("AMI", ami_encode, "bipolar"),
        "10": ("HDB3", hdb3_encode, "bipolar"),
        "11": ("B8ZS", b8zs_encode, "bipolar"),
    }

    # Default bitstream
    default_bits = "100000000100001"
    print("\nAvailable Encodings:")
    for k,v in encodings.items():
        print(f"{k}. {v[0]}")

    choice = input("\nChoose encoding [1-11]: ").strip()
    if choice not in encodings:
        print("Invalid choice.")
        return

    name, func, etype = encodings[choice]

    # Input bit sequence
    input_str = input(f"Enter bit sequence [default: {default_bits}]: ").strip()
    if input_str == "":
        input_str = default_bits

    try:
        bits = [int(ch) for ch in input_str]
        if any(b not in (0,1) for b in bits):
            raise ValueError
    except ValueError:
        print("Invalid input! Only 0/1 allowed.")
        return

    n = len(bits)
    encoded = func(bits)

    # Extend input
    x_bits = list(range(n+1))
    bits_ext = bits + [bits[-1]]

    # Handle encoding axis
    if etype == "rz":  # double resolution
        x_encoded = [i*0.5 for i in range(len(encoded)+1)]
    else:
        x_encoded = list(range(len(encoded)+1))
    encoded_ext = encoded + [encoded[-1]]

    # Plotting
    plt.figure(figsize=(12,6))

    # Input
    plt.subplot(2,1,1)
    plt.step(x_bits, bits_ext, where="post", color="black", linewidth=2)
    plt.fill_between(x_bits, bits_ext, step="post", alpha=0.3, color="black")
    plt.ylim(-0.2, 1.2)
    plt.yticks([0,1], ["0","1"])
    plt.xticks(range(n+1))
    plt.xlim(0, n)
    plt.grid(True, linestyle="--", linewidth=0.7, color="gray")
    plt.title("Input Bitstream")

    # Encoded
    plt.subplot(2,1,2)
    plt.step(x_encoded, encoded_ext, where="post", color="black", linewidth=2)
    plt.fill_between(x_encoded, encoded_ext, step="post", alpha=0.3, color="black")
    
    if etype == "bipolar":
        plt.ylim(-1.2, 1.2)
        plt.yticks([-1,0,1], ["-V","0","+V"])
    else:
        plt.ylim(-0.2, 1.2)
        plt.yticks([0,1], ["0","+V"])

    plt.xticks(range(n+1))
    plt.xlim(0, n)
    plt.grid(True, linestyle="--", linewidth=0.7, color="gray")
    plt.title(f"{name} Encoded Signal")

    plt.xlabel("Bit Index")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()

