import matplotlib.pyplot as plt


def lagerange(x, point_X, point_Y, i, point_num):
    denominator = 1.0
    molecule = 1.0
    res = 0.0

    for j in range(0, point_num):
        if (j != i):
            denominator = denominator * (point_X[i] - point_X[j])
            molecule = molecule * (x - point_X[j])
        else:
            continue

    res = molecule / denominator
    res = res * point_Y[i]
    return res


point_X = list(eval(input("请输入所有横坐标:")))
point_Y = list(eval(input("请输入所有纵坐标:")))

fig_before = plt.figure()
before = fig_before.add_subplot(111)

before.set(xlim=[-20, 20], ylim=[-20, 20], title='Data_before_lagerange', ylabel='Y-Axis', xlabel='X-Axis')
before.plot(point_X, point_Y, color='lightblue', linewidth=1.5)
before.scatter(point_X, point_Y, s=25, c='r') 


insert_X = list(eval(input("请输入预插入值的横坐标:")))

for x in insert_X:
    result = 0
    for i in range(0, len(point_X)):
        result = result + lagerange(x, point_X, point_Y, i, len(point_X))
    point_X.append(x)
    point_Y.append(result)
        

print(point_Y)

fig_after = plt.figure()
after = fig_after.add_subplot(111)
after.set(xlim=[-20, 20], ylim=[-20, 20], title='Data_after_lagerange', ylabel='Y-Axis', xlabel='X-Axis')
after.plot(point_X, point_Y, color='lightblue', linewidth=1.5)
after.scatter(point_X, point_Y, s=25, c='r') 
plt.show()
