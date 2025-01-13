def main(a):
    '''A qiymatini 2 kasrgacha yaxlitlang va uni qaytaring.
    
     Args:
     a (suzuvchi): raqam
    
     Qaytaradi:
     float: natija
     '''
    b = round(a, 2)
    return float(b)

x = main(5.265156)
print(x)