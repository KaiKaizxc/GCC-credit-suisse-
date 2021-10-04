
import os
import sys


def theHackathon(n, m, a, b, f, s, t):
    # Participant code here
    # NAME LIST MUST BE IN A LIST

    name_list = {}
    for number_of_personal in range(n):
        employee_name, department = input(
            "Please enter the name and department of participants").split()
        name_list[employee_name] = department

    # NUMBER OF REQUESTS(m)============

    list_of_requests = []
    list_of_people_together_already = []
    already_requested = set()
    for number_of_requests in range(m):
        employee1, employee2 = input(
            "Please enter the names of both employees.").split()
        # CREATE A NEW SET SORTED
        sort_list = [employee1, employee2]
        sort_list.sort()
        sort_set = set(sort_list)
        # create a new set IN THE LIST NONE OF THEM ARE INSIDE
        if sort_set not in list_of_requests and (employee1 not in already_requested and employee2 not in already_requested):
            list_of_requests.append(sort_set)
            already_requested.update(employee1, employee2)
            list_of_people_together_already.append(sort_list)
        # UNION OF THE SET IF ONE IS ALREADY INSIDE
        elif employee1 in already_requested and employee2 not in already_requested:
            already_requested.update(employee2)
            list_of_people_together_already.append(sort_list)
            for requests in list_of_requests:
                if employee2 in requests:
                    # CHECK IF IT EXCEEDS MAXIMUM LIMIT
                    if len(requests) + 1 <= b:
                        f_counter = 0
                        s_counter = 0
                        t_counter = 0
                        for personal in requests.union(sort_set):
                            if name_list[personal] == '1':
                                f_counter += 1
                            elif name_list[personal] == '2':
                                s_counter += 1
                            else:
                                t_counter += 1
                        if f_counter > f or s_counter > s or t_counter > t:
                            pass
                        else:

                            list_of_requests[list_of_requests.index(
                                requests)] = requests.union(sort_set)

        elif employee2 in already_requested and employee1 not in already_requested:
            already_requested.update(employee1)
            list_of_people_together_already.append(sort_list)
            for requests in list_of_requests:
                if employee2 in requests:
                    # CHECK IF IT EXCEEDS MAXIMUM LIMIT
                    if len(requests) + 1 <= b:
                        f_counter = 0
                        s_counter = 0
                        t_counter = 0
                        for personal in requests.union(sort_set):
                            if name_list[personal] == '1':
                                f_counter += 1
                            elif name_list[personal] == '2':
                                s_counter += 1
                            else:
                                t_counter += 1
                        if f_counter > f or s_counter > s or t_counter > t:
                            pass
                        else:

                            list_of_requests[list_of_requests.index(
                                requests)] = requests.union(sort_set)

        # BOTH OF THEM ARE ALREADY INSIDE
        elif sort_list in list_of_people_together_already:
            pass
        # BOTH ARE ALREADY INSIDE COMBINE THEIR SETS
        else:

            for requests in list_of_requests:
                if employee1 in requests:
                    set1 = requests

                elif employee2 in requests:
                    set2 = requests

                else:
                    pass
            if len(set1)+len(set2) > b:
                pass
            else:
                set3 = set1.union(set2)
                f_counter = 0
                s_counter = 0
                t_counter = 0
                for personal in set3:
                    if name_list[personal] == '1':
                        f_counter += 1
                    elif name_list[personal] == '2':
                        s_counter += 1
                    else:
                        t_counter += 1
                if f_counter > f or s_counter > s or t_counter > t:
                    pass
                else:
                    list_of_requests.remove(set1)
                    list_of_requests.remove(set2)
                    list_of_requests.append(set3)

    # check the eliminate the groups w size <a
    for group_sizes in list_of_requests:
        if len(group_sizes) < a:
            list_of_requests.remove(group_sizes)
    if group_sizes:
        list_of_group_sizes = []
        for group_sizes in list_of_requests:
            group_size = len(group_sizes)
            list_of_group_sizes.append(group_size)

        largest = max(list_of_group_sizes)
        for largestgroup in list_of_requests:
            if len(largestgroup) == largest:
                largestgroup = list(largestgroup)
                largestgroup.sort()
                for individuals in largestgroup:
                    print(individuals)
    else:
        print("no groups")


if __name__ == '__main__':
    inputdata = input().split()

    n = int(inputdata[0])

    m = int(inputdata[1])

    a = int(inputdata[2])

    b = int(inputdata[3])

    f = int(inputdata[4])

    s = int(inputdata[5])

    t = int(inputdata[6])

    theHackathon(n, m, a, b, f, s, t)
