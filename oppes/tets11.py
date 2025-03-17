import random


def generate_student_data(n_students, courses, cities, random_seed=42):
    '''
    Create a list of dict with dictionaries representing each attributes of each student.
    '''
    random.seed(random_seed)
    return [
        {
            "rollno": i, "city": random.choice(cities),
            **{course: random.randint(1, 100) for course in courses}
        }
        for i in range(1, n_students + 1)
    ]


def groupby(data: list, key: callable):
    '''
    Given a list of items, and a key, create a dictionary with the key as key function called
    on item and the list of items with the same key as the corresponding value.
    The order of items in the group should be the same order in the original list
    '''
    d = {}
    for item in data:
        k = key(item)
        li = []
        if isinstance(k, str):
            for t in data:
                if k == t[0]:
                    li.append(t)
        elif isinstance(k, int):
            for t in data:
                if k == len(t):
                    li.append(t)
        d[k] = li
    return d


def apply_to_groups(groups: dict, func: callable):
    '''
    Apply a function to the list of items for each group.
    '''
    d = {}
    for group in groups:
        f = func(groups[group])
        d[group] = f

    return d


def min_course_marks(student_data, course):
    '''Return the min marks on a given course'''
    return min(list(map(lambda y: y[course], student_data)))


def max_course_marks(student_data, course):
    '''Return the max marks on a given course'''
    return max(list(map(lambda y: y[course], student_data)))


def rollno_of_max_marks(student_data, course):
    '''Return the rollno of student with max marks in a course'''
    m = max_course_marks(student_data, course)
    i = list(map(lambda y: y[course], student_data)).index(m)
    return student_data[i]['rollno']


def sort_rollno_by_marks(student_data, course1, course2, course3):
    '''
    Return a sorted list of rollno sorted based on their marks on the three course marks.
    course1 is compared first, then course2, then course3 to break ties.
    Hint: use tuples comparision
    '''
    d = list(map(lambda y: (y['rollno'], y[course1], y[course2], y[course3]), student_data))
    l = list(sorted(d, key=lambda x: (x[1], x[2], x[3])))
    return list(map(lambda x: x[0], l))


def count_students_by_cities(student_data):
    '''
    Create a dictionary with city as key and number of students from each city as value.
    '''
    ...
    list_of_cities = list(map(lambda y: y['city'], student_data))
    no_students = list(map(lambda y: list_of_cities.count(y), list_of_cities))
    d = dict(zip(list_of_cities, no_students))
    return d


def city_with_max_no_of_students(student_data):
    '''
    Find the city with the maximum number of students.
    '''
    d = count_students_by_cities(student_data)
    s_s = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
    return list(s_s.keys())[0]


def group_rollnos_by_cities(student_data):
    '''
    Create a dictionary with city as key and
    a sorted list of rollno of students that belong to
    that city as the value.
    '''
    list_of_cities = list(map(lambda y: y['city'], student_data))
    k = list(map(lambda y: list(filter(lambda t: t['city'] == y, student_data)), list_of_cities))
    no_students = list(map(lambda y: sorted(list(map(lambda m: m['rollno'], y))), k))
    d = dict(zip(list_of_cities, no_students))
    return d


def city_with_max_avg_course_mark(student_data, course):
    '''
    Find the city with the maximum avg course marks.
    '''
    list_of_cities = list(map(lambda y: y['city'], student_data))
    k = list(map(lambda y: list(filter(lambda t: t['city'] == y, student_data)), list_of_cities))
    ty = list(map(lambda y: list(map(lambda z: z[course], y)), k))
    k = list(map(lambda u: sum(u) / len(u), ty))
    d = dict(zip(list_of_cities, k))
    do = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
    return list(do.keys())[0]


fruits = ["Apple", "Banana", "Avocado", "Amla", "Black berry", "Blue berry"]
print(groupby(fruits, lambda x: x[0]))
print(groupby(fruits, len))
groups = {
    "A": ["Apple", "Avocado"],
    "B": ["Banana", "Black berry", "Blue berry"]
}
print(apply_to_groups(groups, len))
print(apply_to_groups(groups, "-".join), )
student_data = generate_student_data(20, ["CT", "Math-1", "Stats-1", "English-1"],
                                     ["Chennai", "Patna", "Delhi", "Kolkata", "Mumbai"])
print(student_data)
R = min_course_marks(student_data, 'CT')
student_data = generate_student_data(20, ["CT", "Math-1", "Stats-1", "English-1"],
                                     ["Chennai", "Patna", "Delhi", "Kolkata", "Mumbai"])
print(rollno_of_max_marks(student_data, "Stats-1"))
student_data = generate_student_data(10, ["CT", "Math-1", "Stats-1", "English-1"],
                                     ["Chennai", "Patna", "Delhi", "Kolkata", "Mumbai"])
print(sort_rollno_by_marks(student_data, "CT", "Math-1", "Stats-1"))
student_data = generate_student_data(20, ["CT", "Math-1", "Stats-1", "English-1"],
                                     ["Chennai", "Patna", "Delhi", "Kolkata", "Mumbai"])
print(city_with_max_no_of_students(student_data))
student_data = generate_student_data(20, ["CT", "Math-1", "Stats-1", "English-1"],
                                     ["Chennai", "Patna", "Delhi", "Kolkata", "Mumbai"])
print(group_rollnos_by_cities(student_data))
student_data = generate_student_data(20, ["CT", "Math-1", "Stats-1", "English-1"],
                                     ["Chennai", "Patna", "Delhi", "Kolkata", "Mumbai"])
city_with_max_avg_course_mark(student_data, "Stats-1")
