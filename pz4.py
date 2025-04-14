# Создаем пакет number_utils
# Создаем папку number_utils и в ней два файла: number_operations.py и number_transformer.py

# number_operations.py
class NumberProcessor:
    def __init__(self, numbers):
        # Инициализируем класс с списком чисел
        self.numbers = numbers

    def is_prime(self, n):
        # Функция для проверки, является ли число простым
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_primes(self):
        # Возвращаем список простых чисел из исходного списка
        return [num for num in self.numbers if self.is_prime(num)]

    def factorial(self, n):
        # Функция для вычисления факториала числа
        if n < 0:
            return None  # Факториал отрицательных чисел не существует
        if n == 0 or n == 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    def filter_numbers(self, condition):
        # Фильтруем числа по указанному условию
        return [num for num in self.numbers if condition(num)]


# number_transformer.py
def power(num, exp):
    # Функция для возведения числа в степень
    return num ** exp


def apply_map(numbers, func):
    # Применяем указанную функцию ко всем элементам списка
    return list(map(func, numbers))


def apply_filter(numbers, condition):
    # Применяем фильтр с заданным условием
    return list(filter(condition, numbers))


# Основной скрипт
if __name__ == "__main__":
    from number_operations import NumberProcessor
    from number_transformer import power, apply_map, apply_filter

    # Создаем список чисел
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Создаем объект NumberProcessor
    processor = NumberProcessor(numbers)

    # Демонстрируем методы класса
    print("Простые числа:", processor.get_primes())  # Получаем простые числа
    print("Факториал 5:", processor.factorial(5))  # Вычисляем факториал 5
    filtered_numbers = processor.filter_numbers(lambda x: x > 5)  # Фильтруем числа больше 5
    print("Числа больше 5:", filtered_numbers)

    # Используем функции из number_transformer.py
    powered_numbers = apply_map(numbers, lambda x: power(x, 2))  # Возводим в квадрат
    print("Числа, возведенные в квадрат:", powered_numbers)

    filtered_even_numbers = apply_filter(numbers, lambda x: x % 2 == 0)  # Фильтруем четные числа
    print("Четные числа:", filtered_even_numbers)

