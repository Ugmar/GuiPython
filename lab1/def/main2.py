def func(a, k):
    list_fib = [1, 1]
    for i in range(k - 1):
        list_fib.append(list_fib[-1] + list_fib[-2])
    s = 0
    for i in range(len(list_fib) -1, -1, -1):
        s += list_fib[i] * (i + 1)
    if s < a:
        return False, 0
    else:
        ans = 0
        list_ans = []
        exit = False
        while k > 0 and not exit:
            for i in range(len(list_fib) -1, -1, -1):
                if ans + list_fib[k - 1] * i < a:
                    ans += list_fib[k -1] * i
                    list_ans.append(i)
                    k -= 1
                    break
                elif ans + list_fib[k - 1] * i == a:
                    list_ans.append(i)
                    exit = True
                    break
        if len(list_ans) < len(list_fib):
            list_ans.extend([0] * (len(list_fib) - len(list_ans)))
        return True, list_ans
