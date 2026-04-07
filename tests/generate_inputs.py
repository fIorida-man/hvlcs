import random
import os


def generate_input(alphabet_size, str_len_a, str_len_b, max_val=20):
    chars = [chr(ord('a') + i) for i in range(alphabet_size)]
    lines = []
    lines.append(str(alphabet_size))
    for c in chars:
        v = random.randint(1, max_val)
        lines.append(f"{c} {v}")
    A = ''.join(random.choices(chars, k=str_len_a))
    B = ''.join(random.choices(chars, k=str_len_b))
    lines.append(A)
    lines.append(B)
    return '\n'.join(lines)


def main():
    os.makedirs('data', exist_ok=True)

    configs = [
        (5, 25, 25),
        (5, 50, 50),
        (5, 75, 75),
        (5, 100, 100),
        (8, 150, 150),
        (8, 200, 200),
        (8, 300, 300),
        (10, 400, 400),
        (10, 500, 500),
        (10, 750, 750),
    ]

    for i, (alpha, la, lb) in enumerate(configs, 1):
        content = generate_input(alpha, la, lb)
        fname = f"data/test_{i:02d}.in"
        with open(fname, 'w') as f:
            f.write(content)
        print(f"Created {fname}  (alpha={alpha}, |A|={la}, |B|={lb})")


if __name__ == '__main__':
    main()