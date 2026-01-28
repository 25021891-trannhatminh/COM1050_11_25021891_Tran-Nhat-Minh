# Problem 1
def unique_sorted_student_ids(lst1,lst2):
    if lst1 == []:
        return lst2
    if lst2 == []:
        return lst1
    unique = list(map(int,lst1)) + list(map(int,lst2))
    
    unique = set(unique)
    unique = list(unique)
    unique.sort()
    
    return (list(map(str,unique)))

# Problem 2
def top3_frequent_names(lst):
    if lst == [] or len(lst) == 1:
        return lst
    name_with_freq = {}
    for name in lst:
        if name in name_with_freq:
            name_with_freq[name] += 1
        else:
            name_with_freq[name] = 1
    top_freq = list(name_with_freq.values())
    top_freq.sort(reverse=True)
    res = []
    if len(top_freq) > 3:
        top_freq = top_freq[:3]
    for freq in top_freq:
        for name in name_with_freq:
            if name_with_freq[name] == freq and (name not in res):
                res.append(name)
    if name_with_freq[res[0]] == name_with_freq[res[1]] and name_with_freq[res[1]] == name_with_freq[res[2]]:
        res.sort()
    for i in range(2):
        if name_with_freq[res[i]] == name_with_freq[res[i+1]]:
            if res[i+1] < res[i]:
                res[i+1],res[i] = res[i],res[i+1]
    return res

# Problem 3
def most_frequent_triple(lst):
    if lst == []:
        return None
    triple_with_freq = {}
    for i in lst:
        if i not in triple_with_freq:
            triple_with_freq[i] = 1
        else:
            triple_with_freq[i] += 1
    freq = list(triple_with_freq.values())
    max_freq = sorted(freq)[-1]
    for i in triple_with_freq:
        if triple_with_freq[i] == max_freq:
            return i

# Problem 4
def reconcile_users(registered_lst, paid_lst):
    if registered_lst == []:
        return (paid_lst,[],[])
    if paid_lst == []:
        return ([],registered_lst,[])
    if registered_lst == [] and paid_lst == []:
        return ([],[],[])
    both = []
    registered_not_paid = []
    registered_lst,paid_lst = map(set,[registered_lst, paid_lst])
    for i in registered_lst:
        if i in paid_lst:
            if i not in both:
                both.append(i)
            paid_lst.remove(i)
        else:
            if i not in registered_not_paid:
                registered_not_paid.append(i)
    paid_not_registered = list(paid_lst)
    both.sort()
    registered_not_paid.sort()
    paid_not_registered.sort()
    return paid_not_registered,registered_not_paid,both

# Problem 5
def contains_duplicate(lst):
    if lst == []:
        return False
    copy_lst = []
    for i in lst:
        if i not in copy_lst:
            copy_lst.append(i)
    return len(copy_lst) < len(lst)

# Problem 6
def squares_div_by3_not6(arr):
    res = [x for x in arr if x % 2 != 0]
    res = [x for x in res if x % 3 == 0]
    res = [x**2 for x in res]
    return res

# Problem 7
def even_numbers_in_matrix(matrix):
    if matrix == []:
        return []
    res = [x for row in matrix for x in row if x % 2 == 0 ]
    return res

# Problem 8
def flatten_2d(matrix):
    if matrix == []:
        return []
    res = [x for row in matrix for x in row]
    return res

# Problem 9
def contains_nearby_duplicate(arr1, k):
    if k < 0 or len(arr1) <= 1:
        return False
    temp = {}
    for i in range(len(arr1)):
        if arr1[i] not in temp:
            temp[arr1[i]] = i
        else:
            return abs(temp[arr1[i]] - i) <= k
        
# Problem 10
def merge_similar_items(items1, items2):
    proces_lst = items1 + items2
    value_dict = {}
    for item in proces_lst: 
        if item[0] not in value_dict:
            value_dict[item[0]] = item[1]
        else:
            value_dict[item[0]] = value_dict[item[0]] + item[1]
    ret = [list(item) for item in value_dict.items()]
    ret.sort(key= lambda x :x[0])
    return ret

# Problem 11
def farm_configurations(n):
    if n == 0:
        return [(0,0)]
    if n % 2 != 0:
        return []
    chickens = n // 2
    cows = 0
    res = [(chickens,cows)]
    while chickens >= 0:
        legs_4_cows = n-(chickens*2)
        if legs_4_cows > 0 and legs_4_cows % 4 == 0:
            cows = legs_4_cows // 4
            res.append((chickens,cows))
        chickens = chickens - 2
    return(res)

# Problem 12
def can_make_odd_sum(arr):
    if arr == []:
        return False
    odd_pos = -1
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            odd_pos = i
            break
    if odd_pos == -1:
        return False
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i] = arr[odd_pos]
    return (sum(arr) % 2 != 0)

# Problem 13
def balanced_array(n: int) -> tuple[str, list[int]]:
    half_len = n // 2
    
    if half_len % 2 != 0:
        return ('NO', []) 
    evens = []
    odds = []
    for i in range(1, half_len + 1):
        evens.append(i * 2)
        
    for i in range(1, half_len):
        odds.append(i * 2 - 1)
        
    last_odd = sum(evens) - sum(odds)
    odds.append(last_odd)
    
    return ('YES', evens + odds)