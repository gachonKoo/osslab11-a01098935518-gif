import sys
import math

def main():
    data = sys.stdin.read().strip()

    if not data:
        c = 0.0
    else:
        try:
            # 입력이 "c = 5.0" 형태라고 가정
            c = float(data.split('=')[1])
        except:
            c = 0.0

    r = c
    area = math.pi * r * r

    print(f"area = {area}")

if __name__ == "__main__":
    main()
