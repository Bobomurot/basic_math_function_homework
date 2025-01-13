def main(a, b):
    '''A soni b ga bo'linganda qoldiqni toping va uning 3 darajasini hisoblab qaytaring.
    
     Args:
     a (int): raqam
     b (int): raqam
    
     Qaytaradi:
     int: natija.
     '''
    x = a % b
    y = x ** 3
    return y
