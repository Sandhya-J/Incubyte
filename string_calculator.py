class StringCalculator:
    def add(self, numbers):
        if not numbers:
            return 0
        number_list = [int(num.strip()) for num in numbers.split(',')]
        return sum(number_list)
