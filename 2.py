# Write a script to print out a set containing all the colours
# from color_list_1 which are not present in color_list_2
color_list_1 = input('Enter the first color list: ')
color_list_2 = input('Enter the second color list: ')
set1 = set(color_list_1.split(","))
set2 = set(color_list_2.split(","))
unique_colors1 = set1.difference(set2)
print (unique_colors1)
