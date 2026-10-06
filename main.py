# Lists -  a data collection option that is ORDERED and MUTABLE 
    # we declare lists using []
def main():
    # declaring an empty list that we can add to later 
    my_list = []
    my_other_list = list()

    # declaring a list with items already in it 
    my_classes = ["Math", "Post-AP", "English"]

    # using len() to find the length of the list 
    print(len(my_classes))
    # we can index using the name of the list followed by [x]
    # our last element in our list is always len(list) - 1
    print(my_classes[2])
    print(my_classes[len(my_classes)-1])
    #using a negative index always accesses from right to left 
    print(my_classes[-1])
    print(my_classes[-2])
    #using a 0 index always gives us our first element 
    print(my_classes[0])

    # we can update and replace items of our list with indeces 
    my_classes[1] = "AP Comp Sci"
    print(my_classes)

    # we can concatenate on to our list elements with +=
    my_classes[1] +=" A"
    print(my_classes)

    print(len(my_classes) >= 4)

    print(my_classes.index("Math"))
    # if the item is not present, it breaks our code 
    #  print(my_classes.index("Journalism"))
    
    # item in list -- returns a boolean 
    print("Math" in my_classes)
    print("Journalism" in my_classes)

    # adding a list element on to the end of our list, use append()
    my_classes.append("Journalism")
    print(my_classes)

    # add items to a list in a specific spot with .insert(index, item)
    # when we use an index that is larger than the list, it will append to the end 
    my_classes.insert(2, "Biology")
    print(my_classes)
    print(my_classes.pop())
    print(my_classes)

    # we can sort our lists to rearrange them 
    # for strings, sorts alphabetically 
    print(my_classes.sort())
    print(my_classes)

    numList = [6, -4, 3, 9]
    numList.sort()
    print(numList)

    my_classes.sort(reverse=True)
    numList.sort(reverse=True)
    print(my_classes)
    print(numList)

    # make a copy of your list that is sorted with sorted()
    print(sorted(my_classes, reverse=True))
    sorted_classes = sorted(my_classes)
    print(sorted_classes)

if __name__ == "__main__":
    main()
