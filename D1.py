

def fibo(n):
    fi =[0,1]
    while fi [-1] < n:
        fi.append(fi[-1]+fi[-2])
    if n in fi:
        return f"o numero {n} está na sequencia."
    else:
        return f"o numero {n} não está na sequencia"

n = int(input("Digite o numero que voce deseja verificar se está na sequencia de Fibonacci"))
resp = fibo(n)
print(resp)
