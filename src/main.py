
import logging

log = logging.Logger('sku-logger')

class SKU:

    def __init__(self):
        self.sku = ""

    # feed options based on importance
    def feed(self, *args):
        sku = ''
        n = 1
        for i in args:
            i = str(i)
            try:
                k = int(i)
                k = str(i)
            except:
                k = i[0:3].upper()
            if n > 1:
                sku += f'-{k}'
            else:
                sku += k
            n += 1 
        self.sku = sku

    # add on some options in a given skew
    def add(self, *args):

        if self.sku == '':
            log.exception('sku is empty: feed the generator with options, use SKU().feed(*args)')
            return
        sku = self.sku
        for i in args:
            i = str(i)
            try:
                k = int(i)
                k = str(i)
            except:
                k = i[0:3].upper()
            sku += f'-{k}'
            
        self.sku = sku

    def get_sku(self):
        return self.sku
