def solution(arr, queries):
    result = []
    for s, e, k in queries:
        m = min((x for x in arr[s:e+1] if x > k), default = None)
        result.append(m if m is not None else -1)
#     for query in queries:
#         answer = []
#         s, e, k = query
#         for x in arr[s:e+1]:
#             if x > k:
#                 answer.append(x)
                
#         if answer:
#             result.append(min(answer))
#         else:
#             result.append(-1)
    return result