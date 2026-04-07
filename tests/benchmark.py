import subprocess
import time
import os

try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    HAS_PLT = True
except ImportError:
    HAS_PLT = False


def get_string_lengths(filepath):
    with open(filepath) as f:
        lines = f.read().strip().split('\n')
    k = int(lines[0])
    A = lines[k + 1]
    B = lines[k + 2]
    return len(A), len(B)


def main():
    input_files = sorted(
        [f for f in os.listdir('data') if f.startswith('test_') and f.endswith('.in')]
    )

    sizes = []
    times = []

    for fname in input_files:
        path = os.path.join('data', fname)
        la, lb = get_string_lengths(path)
        size = la * lb

        with open(path) as f:
            input_data = f.read()

        start = time.perf_counter()
        proc = subprocess.run(
            ['python3', 'src/hvlcs.py'],
            input=input_data, capture_output=True, text=True
        )
        elapsed = time.perf_counter() - start

        sizes.append(size)
        times.append(elapsed)
        print(f"{fname}: |A|={la}, |B|={lb}, m*n={size:>8}, time={elapsed:.4f}s")

        out_path = os.path.join('data', fname.replace('.in', '.out'))
        with open(out_path, 'w') as f:
            f.write(proc.stdout)

    if HAS_PLT:
        plt.figure(figsize=(8, 5))
        plt.plot(sizes, times, 'bo-')
        plt.xlabel('Input size (m * n)')
        plt.ylabel('Runtime (seconds)')
        plt.title('HVLCS Runtime vs Input Size')
        plt.grid(True)
        plt.tight_layout()
        plt.savefig('data/runtime_graph.png', dpi=150)
        print("\nGraph saved to data/runtime_graph.png")
    else:
        print("\nmatplotlib not installed. Install with: pip3 install matplotlib")
        print("Then re-run this script to generate the graph.")


if __name__ == '__main__':
    main()