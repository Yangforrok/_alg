# 方法 1：直接計算
def power2n(n):
    return 2**n

# 方法 2a：遞迴 (錯誤的實現)
def power2n(n):
    pass
    # power2n(n-1)+power2n(n-1)

# 方法 2b：遞迴 (錯誤的實現)
def power2n(n):
    pass
    # 2*power2n(n-1)

# 方法 3：遞迴+查表 (錯誤的實現)
def power2n(n):
    pass
    # if ....
    # power2n(n-1)+power2n(n-1) 

# 方法 4：查表法實現
lookup_table = {0: 1}  # 初始表格，0次方為1

def power2n_new(n):
    # 如果在表中就直接返回
    if n in lookup_table:
        return lookup_table[n]
    
    # 如果不在表中，則計算後放入表中並返回
    lookup_table[n] = 2**n
    return lookup_table[n]

print('power2n_new(10)=:', power2n_new(10))
print('power2n_new(30)=:', power2n_new(30))
print('power2n_new(50)=:', power2n_new(50))