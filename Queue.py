#QUEUE FIF0

from collections import deque
bank = deque(["x","Y","Z"])
print(bank)
bank.popleft()
print(bank)
bank.popleft()
bank.popleft()

if not bank:
    print("No person left")