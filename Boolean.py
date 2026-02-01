# BOOLEAN OPERATORS
# The "or" needs only 1 of the conditions to be validated. the first time the machine sees a true value it'll stop and that will be the result.
# In a chain where everything is false, the last false item will be the final result.
# the "and" operator needs all the conditions given to be validated. In this case, if there is 1 single element that gives false, the final result will be false, even if the others are true.
# the final result if everything in the chain is true will be the last element

# Everything in Python is considered TRUE but 7 items:
# 0; 0.0; FALSE; None; [] (empty list); {}; () (loophole)

print ((7 < 10) or (100 > 10))
print(7 or 6)
print(0 or None or False or 22 or 0.0)
print(11 and 8 and 9 and 10)
print(7 and 8 and 9 and 10)
print(0 or None or False or 0.0 or [])
print((6 or 9) and ("bob or joe"))

