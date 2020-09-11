import operator


def person_lister(f):
    def inner(people):
        final = []
        # print(people)
        for person in people:
            for prop in person:
                if prop.isdigit():
                    prop = int(prop)
                    person[2] = prop
        people.sort(key=operator.itemgetter(2))
        # print(people)
        # for person in people:
        #     final.append(("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1])
        for person in people:
            # f(person)
            print(f(person))
        return final
    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]


if __name__ == '__main__':
    # people = [input().split() for i in range(int(input()))]
    people_temp = [['Mike', 'Thomson', '20', 'M'], ['Robert', 'Bustle', '102', 'M'], ['Andria', 'Bustle', '30', 'F'],
               ['Rishabh', 'Bhardwaj', '22', 'M']]
    name_format(people_temp)
    # print(*name_format(people_temp), sep='\n')



