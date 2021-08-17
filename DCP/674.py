"""A girl is walking along an apple orchard with a bag in each hand.
She likes to pick apples from each tree as she goes along,
but is meticulous about not putting different kinds of apples in the same bag.
Given an input describing the types of apples she will pass on her path, in order,
determine the length of the longest portion of her path that consists of just two types of apple trees.
For example, given the input[2, 1, 2, 3, 3, 1, 3, 5], the longest portion will involve types 1 and 3, with a length of four.
"""


def longest_path(arr):

    count, max_count = 0, 0
    set_ = set()

    for i in arr:
        set_.add(i)
        if len(set_) > 2:
            set_ = set()
            set_.add(i)
            max_count = max(max_count, count)
            count = 1

        else:
            count += 1

    return max_count


arr = [2, 1, 2, 3, 3, 1, 3, 5]
print(longest_path(arr))
