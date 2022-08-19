from file_method import FileMethod as fileMethod


class Solution:
    header_row = ["id", "location", "product", "quantity", "brand"]
    input_name = input("Please enter input file name: ")
    input_data = fileMethod.read_input_file(input_name)
    product_index = header_row.index("product")
    quantity_index = header_row.index("quantity")
    product_data = input_data['product'].tolist()
    brand_data = input_data['brand'].tolist()
    product_data, brand_data = zip(*sorted(zip(product_data, brand_data), key=lambda x: x[1]))
    products_unique = list(sorted(set(product_data), key=product_data.index))
    file1_output = []
    file2_output = []

    @staticmethod
    def most_frequent(input_list):
        return max(set(input_list), key=input_list.count)

    @classmethod
    def common_brand(cls):
        for i in range(len(cls.products_unique)):
            last_index = cls.product_data.index(cls.products_unique[i]) + cls.product_data.count(
                cls.products_unique[i])
            cls.file2_output.append(
                [cls.products_unique[i], cls.most_frequent(cls.brand_data[cls.product_data.index(cls.products_unique[i]):last_index])])

    @classmethod
    def common_product_and_ratio(cls, products: list, n: int):
        product_count = 0
        if n > products.__len__():
            return True
        else:
            for i in range(len(cls.input_data)):
                if cls.input_data.values[i][cls.product_index] == products[0]:
                    product_count += cls.input_data.values[i][cls.quantity_index]
            cls.file1_output.append([products[0], product_count / len(cls.input_data)])
            n += 1
            cls.common_product_and_ratio(products[n:], n)
