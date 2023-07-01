from collections import Counter

# Add one character from the right to the window
character = s[r]
window_counts[character] = window_counts.get(character, 0) + 1

# If the frequency of the current character added equals to the desired count in t then increment the formed count by 1.
if character in dict_t and window_counts[character] == dict_t[character]:
    formed += 1
#--------------------------------------
# contract window
# --------------------------------------
# Try and contract the window till the point where it ceases to be 'desirable'.
while l <= r and formed == required:
    character = s[l]
    # Save the smallest window until now.
    if r - l + 1 < ans[0]:
        ans = (r - l + 1, l, r)
    # The character at the position pointed by the `left` pointer is no longer a part of the window.
    window_counts[character] -= 1
    if character in dict_t and window_counts[character] < dict_t[character]:
        formed -= 1
    # Move the left pointer ahead, this would help to look for a new window.
    l += 1
    # Keep expanding the window once we are done contracting.
r += 1
rn "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]

#res = slidingwindow("fa4chba4c","abc")
res = slidingwindow("bba","ab")
print("res", res)