import matplotlib.pyplot as plt


point_X = list(eval(input("请输入所有横坐标:")))
point_Y = list(eval(input("请输入所有纵坐标:")))

insert_X = list(eval(input("请输入预插入值的横坐标:")))

fig_before = plt.figure()
before = fig_before.add_subplot(111)

before.set(xlim=[-30, 30], ylim=[-30, 30], title='Data_before_Newton', ylabel='Y-Axis', xlabel='X-Axis')
before.plot(point_X, point_Y, color='lightblue', linewidth=1.5)
before.scatter(point_X, point_Y, s=25, c='r') 

for x in insert_X:
    print("-----------------------------------------------------")
    res_1 = point_Y
    time = 1
    first_list = []
    for i in range(0, len(point_X)-1):
        list_demo = []
        for j in range(i + 1, len(point_X)):
            denominator = point_X[j] - point_X[j - time]
            molecule = res_1[j-i] - res_1[j-i-1]
            list_demo.append(molecule*1.0/denominator)
        first_list.append(list_demo[0])
        res_1 = list_demo
        time = time + 1
        flag = i + 1
        print("第%d阶差商表" % flag)
        print(res_1)
        print("第%d阶差商" % flag)
        print(res_1[0])
        result = point_Y[0]
    for i in range(0, len(point_X) - 1):
        for j in range(0, i + 1):
            result = result + first_list[i]*(x - point_X[j])
    if (x > point_X[len(point_X) - 1]):
        point_X.append(x)
        point_Y.append(result)
    else:
        for mid in point_X:
            if (mid > x):
                position = point_X.index(mid)
                point_X.insert(position, x)
                point_Y.insert(position, result)
print(point_X)
print(point_Y)        

fig_after = plt.figure()
after = fig_after.add_subplot(111)
after.set(xlim=[-30, 30], ylim=[-30, 30], title='Data_after_Newton', ylabel='Y-Axis', xlabel='X-Axis')
after.plot(point_X, point_Y, color='lightblue', linewidth=1.5)
after.scatter(point_X, point_Y, s=25, c='r') 
plt.show()