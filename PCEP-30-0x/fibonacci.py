# Fibonacci es una sucesión matematica
# F(n)=F(n-1)+F(n-2)
# Valores iniciales: F(0) = 0, F(1) = 1

fibonacci_list = [0, 1]

for i in range(20):
    fibonacci_list.append(fibonacci_list[i] + fibonacci_list[i+1])

print(fibonacci_list)