


class SKU:

    def __init__(self):
        self.sku = ""

    # feed options based on importance
    def feed(self, *args):
        sku = ''
        for i in args:
            i = str(i)
            try:
                k = int(i)
                k = str(i)
            except:
                k = i[0:3].upper()
            sku += k
        self.sku = sku

    # add on some options in a given skew
    def add(self, *args):
        sku = self.sku
        for i in args:
            i = str(i)
            try:
                k = int(i)
                k = str(i)
            except:
                k = i[0:3].upper()
            sku += k
        self.sku = sku

    def get_sku(self):
        return self.sku

# example

s = SKU()

s.feed('DRESS','RED','SMALL')
s.add(1234)
sku = s.get_sku()

print(sku)