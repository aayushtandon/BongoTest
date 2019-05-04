class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father


person_a = Person("User", "1", None)
person_a = person_a.__dict__
person_b = Person("User", "2", person_a)
person_b = person_b.__dict__
#print person_b

a = {
        "key1": 1, "key2": {
                            "key3": 1, "key4": {
                                                "key5": 4,"user":person_b
                                               }
                           }
        }

def print_depth(data, main_str,lvl_count):
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
                if tup.index(ele) == 0:
                    print str(ele)+' '+str(lvl_count)
                else:
                    pass
            else:
                lvl_count = lvl_count + 1
                print_depth(ele,main_str,lvl_count)
print_depth(a,'',1)