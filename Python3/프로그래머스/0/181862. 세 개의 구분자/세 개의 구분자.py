import re

def solution(myStr):
    parts = re.split('[abc]', myStr)
    result = [p for p in parts if p]
    return result if result else ["EMPTY"]