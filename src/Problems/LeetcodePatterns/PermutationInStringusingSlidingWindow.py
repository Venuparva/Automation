from collections import Counter
s1 = "ab"
s2 = "eidbaooo"

def checkInclusion(s1: str, s2: str) -> bool:
    n1, n2 = len(s1), len(s2)
    d1 = Counter(s1)
    d2 = Counter(s2[:n1 - 1])
    j = 0
    print(s1)
    print(s2)
    print(s2[:n1 - 1])
    print(n2)
    print("-----")
    for i in range(n1 - 1, n2):
        print(s2[i])
        d2[s2[i]] += 1
        if d1 == d2:
            print("matches")
            print(d1,d2)
            return True
        d2[s2[j]] -= 1
        if d2[s2[j]] == 0:
            del d2[s2[j]]
        j += 1
        print("d2",d2)
    return False

checkInclusion(s1,s2)
