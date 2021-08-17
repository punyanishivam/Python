def dir_reduc(arr):

    result = []

    for i in arr:
        if i == "NORTH":
            if "SOUTH" in result:
                result.remove("SOUTH")
        # elif i == "SOUTH":
        #     if "NORTH" in result:
        #         result.remove("NORTH")
        # elif i == "EAST":
        #     if "WEST" in result:
        #         result.remove("WEST")
        # elif i == "WEST":
        #     if "EAST" in result:
        #         result.remove("EAST")
        else:
            result.append(i)
    return result

a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
print(dir_reduc(a))
