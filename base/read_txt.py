def read_txt(filename):
    filepath = r"C:\Users\HUAWEI\Desktop\pytest\data\\" + filename
    with open(filepath, "r", encoding="utf-8") as f:
        return f.readlines()

# if __name__ == '__main__':
#     # arr = []
#     #
#     # for i in read_txt('cala.txt'):
#     #     ar                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                r.append(tuple(i.strip().split(',')))
#     #
#     # print(arr)