from collections import namedtuple
from collections import defaultdict
from pprint import pprint
import csv 
def main():
    file = 'data/OrderItems.csv'
    with open(file,'r') as f:
        itemDict = defaultdict(int)
        csv_reader = csv.reader(f)
        head = next(csv_reader)
        Item = namedtuple('Item',[*head])
        itemList = []
        for row in csv_reader:
            item = Item(*row)
            #default dict behaviour*****
            itemDict[item.ProductID]+=int(item.Quantity)
        pprint(itemDict)

        # for row in csv_reader:
        #     print(row)
    #add code here

    return

if __name__ == "__main__":
    main()