import re
import sys

class StringCalculator:
    def add(self, numbers):
        if not numbers:
            return 0
        
        try:
            number_list = [int(num.strip()) for num in re.split(r'[,\n]', numbers)]
            if len(number_list) > 10000:
                raise ValueError("Too many numbers to process")
            result = sum(number_list)
            
            if result > sys.maxsize // 2:  # handle overflow
                raise OverflowError("Sum too large to return safely")
                
            return result
            
        except ValueError as e:
            raise e
