#Функция расчёта смещений на Сером столе
def gray_table():
    #Лист для позиций, где робот работает с заготовкой
    act_poses=[]
    #Лист для позиций над заготовкой
    pre_poses=[]
    #старовая позиция, относительно которой производится расчёт смещений
    start_pos=[0, 0, 0] #Indexes: 0 - X, 1 - Y, 2 - Z
    #Переменные смещений по осям: для x - dx,  для y - dy , для z - dz
    #Данные смещения рассчитаны для базы belay_table_figures
    dx=220.25
    dy=193.63
    dz=51
    #Цикл for используется для заполнения первого списка смещений в базе belay_table_figures, которая сделана для серого стола
    for i in range(2):
        prepos=start_pos.copy()
        prepos[2]-=dz
        actpos=start_pos.copy()
        actpos[2]-=dz
        prepos[0]+=dx*i
        prepos[0]=round(prepos[0],2)
        for j in range(2):
            prepos[1]+=dy*j
            prepos[1]=round(prepos[1],2)
            act_poses.append(actpos.copy())
            pre_poses.append(prepos.copy())
    return act_poses,pre_poses
#функция по расчёту значений смещений на белом столе
#В первом расчёте производятся смещения по осям x,y базы belay_table_figures, тогда как во втором только по оси x базы belay_white_table
def white_table():
    act_poses=[]
    pre_poses=[]
    start_pos=[0,0,0]
    dx=106
    dz=90
    #Цикл for для заполнения списка со значениями смещений относительно белого стола и базы belay_white_table
    for i in range(4):
        prepos=start_pos.copy()
        prepos[2]-=dz
        actpos=start_pos.copy()
        actpos[2]-=dz
        prepos[0]+=dx*i
        prepos[0]=round(prepos[0],2)
        act_poses.append(actpos.copy())
        pre_poses.append(prepos.copy())
    return act_poses,pre_poses
