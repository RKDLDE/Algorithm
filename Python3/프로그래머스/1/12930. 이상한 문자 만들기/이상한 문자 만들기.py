def solution(s):
    result = []
    
    for word in s.split(" "):
        transformed = ""
        for i, ch in enumerate(word):
            transformed += ch.upper() if i % 2 == 0 else ch.lower()
        result.append(transformed)
    return " ".join(result)
            
#     for word in words:
#         cnt = 0
#         for ch in word:
#             if cnt % 2 == 0:
#                 result += ch.upper()
#             else:
#                 result += ch.lower()
#             cnt += 1

            
#     return result.strip()