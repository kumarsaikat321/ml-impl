from utils.Least_square import least_sq

if __name__ == '__main__':
    #print("hello world !!!!")
    #dg = DataGenerator(3, 3)
    #print(dg.generate())

    ft = least_sq(3, 3, 5)
    print(ft.fit())

