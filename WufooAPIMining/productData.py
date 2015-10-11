__author__ = 'saipc'


with open('products_export.csv', 'r') as csv:
    with open('productData', 'w') as writer:
        for line in csv:
            writer.write(line)

