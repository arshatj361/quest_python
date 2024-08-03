#maximum elements in the stack

def process_queries(queries):
    stack = []
    max_stack = []
    
    results = []
    
    for query in queries:
        parts = query.split()
        type_query = int(parts[0])
        
        if type_query == 1:
            x = int(parts[1])
            stack.append(x)
            if max_stack:
                max_stack.append(max(x, max_stack[-1]))
            else:
                max_stack.append(x)
                
        elif type_query == 2:
            if stack:
                stack.pop()
                max_stack.pop()
                
        elif type_query == 3:
            if max_stack:
                results.append(max_stack[-1])
    
    return results

def main():
    N = int(input("Enter the number of queries: "))
    queries = []
    for _ in range(N):
        query = int(input("enter the queries:"))
        queries.append(query)
    
    results = process_queries(queries)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()