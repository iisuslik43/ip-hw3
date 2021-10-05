import numpy as np


def read_data():
    with open('in.txt') as f:
        content = f.read()
    return [[float(number) for number in line.split()] for line in content.split('\n')]


def find_ranks(data):
    data.sort(key=lambda x: x[1])
    data = [[x[0], x[1], len(data) - i] for i, x in enumerate(data)]
    data.sort()

    rank = {}
    for x, y, i in data:
        rank[y] = rank.get(y, []) + [i]
    rank = {y: np.mean(y_ranks) for y, y_ranks in rank.items()}
    ranks = [rank[y] for x, y, i in data]
    return ranks


def write_to_file(numbers):
    with open('out.txt', 'w') as f:
        f.write(' '.join(map(str, numbers)))


def main():
    data = read_data()
    N = len(data)
    if N < 9:
        print('N is less then 9')
        exit(1)
    ranks = find_ranks(data)
    p = int(round(N / 3))
    R1 = sum(ranks[:p])
    R2 = sum(ranks[(N - p):])

    standard_deviation = (N + 0.5) * np.sqrt(p / 6)
    mera = (R1 - R2) / (p * (N - p))
    write_to_file([int(round(R1 - R2)), int(round(standard_deviation)), round(mera, 2)])


if __name__ == '__main__':
    main()
