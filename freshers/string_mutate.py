def mutate(string, index, letter):
    ans = ''
    ans += string[:index]
    ans += letter
    ans += string[index+1:]
    return ans


print(mutate("randomworfrandomword", 9, 'd'))
