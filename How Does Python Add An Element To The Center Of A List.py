# https://www.youtube.com/watch?v=V_wmZnnjgBQ
# How Does Python Add An Element To The Center Of A List?
my_list = ["a", "b", "d", "e"]
print("Original list:", my_list)
# Uh oh, we left out the "c" in our list
# Compute the target index
target_idx = int(len(my_list) / 2)
print("target index:", target_idx)
# Insert into the list
my_list.insert(target_idx, "c")
# Print the new contents of the list
print("New list:", my_list)
