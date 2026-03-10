# Population of Scotland in millions
a = 5.08   # 2004
b = 5.33   # 2014
c = 5.55   # 2024

# Calculate changes
d = b - a   # change from 2004 to 2014
e = c - b   # change from 2014 to 2024

# Compare d and e
if d > e:
    print("Population growth is decelerating.")
elif d < e:
    print("Population growth is accelerating.")
else:
    print("Population growth is constant.")

# Conclusion: d > e, so growth is decelerating.




X = True
Y = False

W = X or Y   # This will be True

# Truth table for "or":
# X     Y     X or Y
# True  True   True
# True  False  True
# False True   True
# False False  False




