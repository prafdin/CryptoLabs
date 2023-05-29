import math
import pickle
from collections import Counter, defaultdict
from functools import reduce
from itertools import compress, product
from math import sqrt, log, erfc
from scipy.fftpack import fft
from scipy.special import gammaincc
from scipy import special as spc

class LFSR:
    memory_length = 5

    def __init__(self, memory, polynom):
        self.memory = memory
        self.polynom = polynom

    def tick(self):
        tmp = compress(self.memory, self.polynom) # apply polinom to memory bits
        out = reduce(lambda a, x: a ^ x, tmp)

        self.memory = self.memory[1:]
        self.memory.append(out)
        return out

    def last_out(self):
        return self.memory[-1]

    @staticmethod
    def create_lsfr1(memory):
        return LFSR(memory, [1, 0, 0, 1, 0])

    @staticmethod
    def create_lsfr2(memory):
        return LFSR(memory, [1, 1, 1, 1, 1])

    @staticmethod
    def create_lsfr3(memory):
        return LFSR(memory, [1, 0, 0, 1, 1])



def find_memory_with_max_N(lsfr: LFSR):
    memory_tests = list(map(list, product([0, 1], repeat=LFSR.memory_length)))
    memory_tests.remove(([0] * LFSR.memory_length))

    scores = {}
    for test_memory in memory_tests:
        lsfr.memory = test_memory
        lsfr.tick()
        count = 1
        while lsfr.memory != test_memory:
            count += 1
            lsfr.tick()
        scores[tuple(test_memory)] = count


    max_kv = max(scores.items(), key=lambda i: i[1])
    return list(max_kv[0])

def majority_vote(values):
    return Counter(values).most_common(1)[0][0]

def generate_valuesuence():
    lsfr1 = LFSR.create_lsfr1([])
    lsfr1.memory = find_memory_with_max_N(lsfr1)

    lsfr2 = LFSR.create_lsfr2([])
    lsfr2.memory = find_memory_with_max_N(lsfr2)

    lsfr3 = LFSR.create_lsfr3([])
    lsfr3.memory = find_memory_with_max_N(lsfr3)

    valuesuence_length = 1000000
    result = []

    geners = [lsfr1, lsfr2, lsfr3]
    values = []
    values.append(geners[0].tick())
    values.append(geners[1].tick())
    values.append(geners[2].tick())
    for _ in range(valuesuence_length):
        major_bit = majority_vote(values)
        result.append(major_bit)

        active_geners_idx = []
        if lsfr1.last_out() == major_bit:
            active_geners_idx.append(0)
        if lsfr2.last_out() == major_bit:
            active_geners_idx.append(1)
        if lsfr3.last_out() == major_bit:
            active_geners_idx.append(2)

        for g_i in active_geners_idx:
            values[g_i] = geners[g_i].tick()

    with open("out.txt", 'wb') as f:
        pickle.dump(result, f)

def spectral(values):
    signal = list(map(lambda x: 2 * x - 1, values))
    n = len(signal)
    s = abs(fft(signal))
    s_div_2 = s[:n // 2]
    t = sqrt(log(1 / 0.05) * n)
    n0 = (0.95 * n) / 2
    n1 = len(list(filter(lambda x: 0 < x < t, s_div_2)))
    d = (n1 - n0) / sqrt((n * 0.95 * 0.05) / 4)
    p_value = erfc(abs(d) / sqrt(2))

    print(f'Spectral: p_value = {p_value}')

def approximate_entropy(m, values):
    n = len(values)
    values += values[:m + 1]

    cnt1 = defaultdict(lambda: 0)
    cnt2 = defaultdict(lambda: 0)

    for i in range(n):
        cnt1[tuple(values[i:i + m])] += 1
        cnt2[tuple(values[i:i + m + 1])] += 1

    apen = 0.0
    for c in cnt1.values():
        apen += c * math.log(c / n)
    for c in cnt2.values():
        apen -= c * math.log(c / n)

    chi_squared = n * (math.log(2) - apen / n)
    pvalue = spc.gammaincc(2 ** (m - 1), chi_squared)

    print(f"Approximate entropy: p-value={pvalue}")

def random(values):
    sum = 0
    cnt = defaultdict(lambda: 0)

    for x in values:
        x = -1 if x == "0" else 1
        sum += x
        cnt[sum] += 1

    J = cnt[0] + 1
    for i in range(-9, 10):
        if i == 0:
            continue

        pvalue = math.erfc(abs(cnt[i] - J) / math.sqrt(2 * J * (4 * abs(i) - 2)))
        print(f"{i} p-value={pvalue}")

        if (pvalue < 0.01):
            print(f"rand_exc2: Attention for {i}!")

def read_pi():
    with open("data.pi", "r") as f:
        pi_data = f.read()

    pi_data = pi_data.replace(" ", "")
    pi_data = pi_data.replace("\n", "")
    pi_data = list(map(int, list(pi_data)))
    return pi_data

def read_e():
    with open("data.e", "r") as f:
        e_data = f.read()

    e_data = e_data.replace(" ", "")
    e_data = e_data.replace("\n", "")
    e_data = list(map(int, list(e_data)))
    return e_data


def main():
    # generate_valuesuence()
    with open("out.txt", 'rb') as f:
        values = pickle.load(f)

    values = read_pi()
    spectral(values)
    approximate_entropy(10, values)
    random(values)

if __name__ == '__main__':
    main()