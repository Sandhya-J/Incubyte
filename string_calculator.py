import re
import sys

class StringCalculator:
    def add(self, numbers):
        if not numbers:
            return 0
        
        try:
            if numbers.startswith("//"):
                parts = numbers.split("\n", 1)
                if len(parts) != 2:
                    raise ValueError("Invalid custom delimiter format")
                
                custom_delimiter = parts[0][2:]
                numbers_part = parts[1]
                
                delimiters = f"[{re.escape(custom_delimiter)},\n]"
                number_list = [int(num.strip()) for num in re.split(delimiters, numbers_part)]
            else:
                number_list = [int(num.strip()) for num in re.split(r'[,\n]', numbers)]
            
            if len(number_list) > 10000:
                raise ValueError("Too many numbers to process")
            
            result = sum(number_list)
            
            if result > sys.maxsize // 2:  # handle overflow
                raise OverflowError("Sum too large to return safely")
                
            return result
            
        except ValueError as e:
            raise e
