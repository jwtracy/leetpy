
import re
import pprint

PARSER = re.compile(r'^SELECT (.*) FROM [a-z]+(?: WHERE (.*?))?(?: ORDER BY (.*?))?$')

# Example
print(PARSER.match("SELECT a FROM library WHERE b = 1 ORDER BY c").groups())
# This prints: ('a', 'b = 1', 'c')

LIBRARY = [
    {
        'title': 'The Ministry for the Future',
        'author': 'Kim Stanley Robinson',
        'year': 2020,
    },
    {
        'title': 'Circe',
        'author': 'Madeline Miller',
        'year': 2018,
    },
    {
        'title': 'Song of Achilles',
        'author': 'Madeline Miller',
        'year': 2012,
    },
    {
        'title': 'Designing Climate Solutions',
        'author': 'Hal Harvey',
        'year': 2018,
    },
]

def query(database: list, query: str):
    params = PARSER.match(query).groups()
    res = []
    select = params[0]
    where = ""
    if params[1]:
        where = params[1]
    order_by = ""
    if params[2]:
        order_by = params[2]
    for book in database:
        if where:
            ands = where.split("AND")
            mat = True
            for condition in ands:
                equality = condition.strip(" ").split(" ")
                print(equality)
                match equality[1]:
                    case "=":
                        if book[equality[0]] != " ".join(equality[2:]).strip("'"):
                            mat = False
                    case "<":
                        if book[equality[0]] > " ".join(equality[2:]).strip("'"):
                            mat = False
                    case ">":
                        if book[equality[0]] < " ".join(equality[2:]).strip("'"):
                            mat = False
            if mat:
                res.append(book)

    if order_by:
        ordinality = order_by.split(",")
        res.sort(key=lambda book: book[ordinality[0].strip(" ")])

    formated = []

    if select and select != "*":
        columns = select.split(",")
        for book in res:
            new_book = {}
            for c in columns:
                new_book[c.strip(" ")] = book[c.strip(" ")]
            formated.append(new_book)

    if not formated:
        formated = res
    
    return formated
import collections


# class Solution:
#     def licenseKeyFormatting(self, s: str, k: int) -> str:
#         stack = list(s)
#         k_bucket = 0
#         res = []
#         while stack:
#             if k_bucket == k:
#                 res.append("-")
#                 k_bucket = 0
# 
#             cur = stack.pop()
#             if cur == "-":
#                 continue
#             res.append(cur)
#             k_bucket += 1

import heapq

class Solution:
    
    def lengthLongestPath(self, input: str) -> int:
        def __isfile(s: str) -> bool:
            if "." in s:
                return True
            return False

        def __getdepth(s: str) -> int:
            cnt = 0
            for c in s:
                if c != "\t":
                    return cnt
                cnt += 1
        fs = input.splitlines()
        max_path_length = 0
        dir_stack = []
        for f in fs:
            cur_depth = __getdepth(f)
            file = f.strip("\t")
            while dir_stack and cur_depth <= dir_stack[-1][1]:
                dir_stack.pop()

            dir_stack.append((file, cur_depth))
            if __isfile(file):
                max_path_length = max(max_path_length, len("/".join([f[0] for f in dir_stack])))
                dir_stack.pop()
            
        return max_path_length

            


            


    
def main():
    print(collections.Counter("hello"))

if __name__ == "__main__":
    main()