# Дополнительное задание 2
# Найти цифровой корень
# Поупражняться в рекурсии...

def digital_root(num: int) -> int:
    if num < 10:
        return num
    else:
        return digital_root(sum(int(i) for i in str(num)))

print(digital_root(889987))