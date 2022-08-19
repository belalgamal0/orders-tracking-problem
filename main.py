from file_method import FileMethod as fileMethod
from solution import Solution

solution = Solution

solution.common_product_and_ratio(solution.products_unique, 0)
fileMethod.write_output_file('0_' + solution.input_name, solution.file1_output)
solution.common_brand()
fileMethod.write_output_file('1_' + solution.input_name, solution.file2_output)
