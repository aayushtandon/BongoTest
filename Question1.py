#[('key2', {'key3': 1, 'key4': {'key6': {'key7': 8}, 'key5': 4}}), ('key1', 1)]
#[('key3', 1), ('key4', {'key6': {'key7': 8}, 'key5': 4})]
#[('key6', {'key7': 8}), ('key5', 4)]
#[('key7', 8)]

def print_depth(data,lvl_count):
    list1 = data.items()
    list2 = []
    list3 = []
    for tupl in list1:
        if (isinstance(tupl[0], dict)==False and isinstance(tupl[1], dict)==False):
            list2.append(tupl)
        else:
            list3.append(tupl)
    list2.extend(list3)
    for tup in list2:
        for ele in tup:
            if isinstance(ele, dict)==False:
                if tup.index(ele)==0:
                    print str(ele)+' '+str(lvl_count)
                else:
                    pass
            else:
                lvl_count = lvl_count + 1
                print_depth(ele,lvl_count)



if __name__ == '__main__':

    a = {
        "key1": 1, "key2": {
                            "key3": 1, "key4": {
                                                "key5": 4
                                               }
                           }
        }
    print_depth(a,1)
