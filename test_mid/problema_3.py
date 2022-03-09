# Scrie un program care sa afiseze toate combinarile de 2 litere dintre valorile dictionarului de mai jos:

dictionar = {"1": "abc","2": "s","3": "o","4": "n","5": "lm","6": "jk","7": "gi","8": "def","9": "abc"}

for a in dictionar['1']:
    for b in dictionar['2']:
        for c in dictionar['3']:
            for d in dictionar['4']:
                for e in dictionar['5']:
                    for f in dictionar['6']:
                        for g in dictionar['7']:
                            for h in dictionar['8']:
                                for i in dictionar['9']:
                                    print(a + b + c + d + e + f + g + h + i)
