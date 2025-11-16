import sys
import math

def main():
    data = sys.stdin.read().strip()
    if not data:
        # 입력이 없을 때 기본값
        c = 0.0
    else:
        # "c = 5.0" 형태를 처리
        try:
            c = float(data.split('=')[1])
        except:
            c = 0.0

    r = c
    area = math.pi * r * r

    print(f"area = {area}")

if __name__ == "__main__":
    main()
