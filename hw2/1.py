def perm(elements):  
    p = []  
    results = []  
    permNext(elements, p, results)  
    return results

def permNext(elements, p, results):
    if len(p) == len(elements):  
        results.append(p[:])  
        return
    for x in elements:  
        if x not in p:  
            p.append(x)  
            permNext(elements, p, results)  
            p.pop() 

def main():
    user_input = input("請輸入一組值用逗號隔開： ")
    elements = [x.strip() for x in user_input.split(",")] 
    results = perm(elements)
    for idx, result in enumerate(results, start=1):
        print(f"{idx:3}: {result}")

main()
