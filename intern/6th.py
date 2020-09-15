import json
# def readwrite(in_dic, out_dic):
#     input = open(in_dic, 'r').readlines()
#     write = open('myfile.txt', 'w')


def sortFunction(value):
    return value["id"]


if __name__ == '__main__':
    in_dic = "text.txt"
    jso = []
    with open(in_dic, 'r') as inp:
        inpu = inp.readlines()
        for i in range(len(inpu)):
            jso.append(json.loads(inpu[i]))

    jso = sorted(jso, key=sortFunction)
    with open("shish.txt", "w+") as f:
        for i in range(len(jso)):
            f.write(str(jso[i]) + '\n')

