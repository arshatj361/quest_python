import sys

def main():
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    
    results = []
    
    for _ in range(T):
        N = int(input("enter the data:"))
        index += 1
        array = list(map(int, data[index:index + N]))
        index += N
        
        array.sort(reverse=True)
        
        results.append(" ".join(map(str, array)))
    
    print("\n".join(results))
