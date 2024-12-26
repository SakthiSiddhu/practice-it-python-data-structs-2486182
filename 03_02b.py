import csv
import itertools
from collections import namedtuple
def main():
    file_path = 'data/Customer.csv'

    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        first_row = next(csv_reader)
       
        Customer = namedtuple('Customer',[*first_row])
        for row in csv_reader:
            customer = Customer(*row)
            print(customer)

if __name__ == "__main__":
    main()