import sys, re
INPUT = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 9)


def main():
    S = INPUT().replace("?", ".")  # 入力文字列 S 中の文字の置換 : "?" (直前の 1 文字省略可能) -> "." (任意の 1 文字)
    T = INPUT()

    for i in range(len(S)-len(T), -1, -1):
        if re.match(S[i: i+len(T)], T):
            S = S.replace(".", "a")  # 辞書順最小 : "." -> "a"
            print(S[:i] + T + S[i+len(T):])
            exit()

    print("UNRESTORABLE")


if __name__ == '__main__':
    main()
