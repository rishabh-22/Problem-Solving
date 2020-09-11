from datetime import datetime


def check_valid_string(s):

    open_b = []
    star = []
    for i in range(len(s)):
        if s[i] == '(':
            open_b.append(i)
        elif s[i] == '*':
            star.append(i)
        elif s[i] == ')':
            if len(open_b):
                open_b.pop()
            elif len(star):
                star.pop()
            else:
                return False

    while len(open_b):
        if not len(star):
            return False
        elif star[-1] > open_b[-1]:
            star.pop()
            open_b.pop()
        else:
            return False

    return True


start = datetime.now()
print(check_valid_string("*()(())*()(()()((()(()()*)(*(())((((((((()*)(()(*)"))
end = datetime.now()
print("total time: ", end-start)


# C++ code
# class Solution {
# public:
#     bool
#
#
# checkValidString(string
# s) {
#
#     stack < int > open, star;
# int
# len = s.length();
#
# for (int i=0;s[i] != '\0';++i)
# {
# if (s[i] == '(')
# open.push(i);
# else if (s[i] == '*')
# star.push(i);
# else
# {
# if (!open.empty())
# open.pop();
# else if (!star.empty())
# star.pop();
# else
# return false;
# }
# }
#
# // Now
# process
# leftover
# opening
# brackets
# while (!open.empty())
# {
# if (star.empty())
# return false;
# else if (open.top() < star.top())
#     {
#         open.pop();
#     star.pop();
#     }
#     else // CASE: open.top() > star.top()
#     return false;
#     }
#     return true;
#     }
#     };
