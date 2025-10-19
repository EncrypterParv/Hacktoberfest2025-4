def canAliceWin(n, a, b):
# Return "YES" if Alice has a winning strategy, otherwise return "NO"
    if abs(a-b)%2==0:
        return "YES"
    else:
        return "NO"
