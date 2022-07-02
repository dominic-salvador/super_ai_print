import time

# Simulate CPU Thinking
print("Loading:")
for number in range(1,4):
    print("."*number, end="")
    print("")
    time.sleep(1)
print("Hello Mom!")
