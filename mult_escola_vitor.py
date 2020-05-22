#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Multiplicador:
    def multiplica(self, multiplicador, multiplicando):
        try:
            float(multiplicador)
            float(multiplicando)
            if multiplicador < 0 and multiplicando >= 0:
                negativo = 0
            elif multiplicador >= 0 and multiplicando < 0:
                negativo = 0
            else:
                negativo = 1
            size = len(str(multiplicando * multiplicador)) + 3
            lista = []
            lista.append(str(multiplicando).rjust(size))
            lista.append(f"x {str(multiplicador)}".rjust(size))
            lista.append("-" * size)
            dec = 0
            if "." in str(multiplicador):
                dec += len(str(multiplicador).split(".")[1])
                multiplicador = int(str(multiplicador).replace(".",""))
            if "." in str(multiplicando):
                dec += len(str(multiplicando).split(".")[1])
                multiplicando = int(str(multiplicando).replace(".",""))
            if "-" in str(multiplicador):
                multiplicador = int(str(multiplicador).replace("-",""))
            if "-" in str(multiplicando):
                multiplicando = int(str(multiplicando).replace("-",""))
            mid = list(map(lambda x: int(x)*multiplicando, str(multiplicador)))
            result = 0
            for a in range(0,len(mid)):
                result += mid[a] * 10 ** (len(mid)-a-1)
                if a == len(mid)-1:
                    lista.append(f"+ {str(mid[0])}".rjust(size - len(mid)+1))
                else:
                    lista.append(str(mid[-a - 1]).rjust(size - a))
            if negativo == 0:
                result = -result
            lista.append("-" * size)
            if dec != 0:
                result = f"{str(result)[0:-dec]}.{str(result)[-dec:]}"
            lista.append(str(result).rjust(size))
            x = "\n".join(lista)
        except:
            raise ValueError('Numero invalido')
        return [float(result), mid, x]

if __name__ == '__main__':
    a = Multiplicador().multiplica(99999999999999, 888888888888888)
    print(a[2])
