from itertools import count, cycle

print("-" * 20, "Start Iterator First")
start_item = 3

for i in count(start_item):
    if i > 10:
        break
    print(i)

print("-" * 20, "End Iterator First")
print()
print("-" * 20, "Start Iterator Second")

my_list = ["A", "8", 15.0, "V", "empty", 0]
max_iterations = 10
iteration_count = 0

for i in cycle(my_list):
    print(i)
    iteration_count += 1

    if iteration_count >= max_iterations:
        break

print("-" * 20, "End Iterator Second")
