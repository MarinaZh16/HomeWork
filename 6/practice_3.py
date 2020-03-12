def convert_size(s):                                                # так можно любой размер перевести 
    size={'XXS': ('rus 42', 'ger 36', 'usa 8', 'fr 38', 'gb 24'),   # в международный
      'XS': ('rus 44', 'ger 38', 'usa 10', 'fr 40', 'gb 26'),       # ввод в формате 'usa 18'
      'S': ('rus 46', 'ger 40', 'usa 12', 'fr 42', 'gb 28'),
      'M': ('rus 48', 'ger 42', 'usa 14', 'fr 44', 'gb 30'),
      'L': ('rus 50', 'ger 44', 'usa 16', 'fr 46', 'gb 32'),
      'XL': ('rus 52', 'ger 46', 'usa 18', 'fr 48', 'gb 34'),
      'XXL': ('rus 54', 'ger 48', 'usa 20', 'fr 50', 'gb 36'),
      'XXXL': ('rus 56', 'ger 50', 'usa 22', 'fr 52', 'gb 38')}
    for i in size:
        if s in size[i]:  
           return i

def all_size(s):
    size={'XXS': ('rus 42', 'ger 36', 'usa 8', 'fr 38', 'gb 24'),
      'XS': ('rus 44', 'ger 38', 'usa 10', 'fr 40', 'gb 26'),       #переводим международный размер
      'S': ('rus 46', 'ger 40', 'usa 12', 'fr 42', 'gb 28'),        # во все остальные
      'M': ('rus 48', 'ger 42', 'usa 14', 'fr 44', 'gb 30'),
      'L': ('rus 50', 'ger 44', 'usa 16', 'fr 46', 'gb 32'),
      'XL': ('rus 52', 'ger 46', 'usa 18', 'fr 48', 'gb 34'),
      'XXL': ('rus 54', 'ger 48', 'usa 20', 'fr 50', 'gb 36'),
      'XXXL': ('rus 56', 'ger 50', 'usa 22', 'fr 52', 'gb 38')}
    return size[s]
    
print('Введите размер (XS, S, M и т.д)')        
i_s=all_size(str(input()).upper())
print(i_s)        

