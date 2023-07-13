#импортируем функции открытия и закрытия захвата
from gripper_actions import taking, dropping
#Импортируем функцию расчёта смещений на сером столе
from calculation import gray_table
#Импортируем функцию действий в зоне белого стола
from white_moves import white_actions
act_gray,pre_gray = gray_table()
#Импортруем функции перехода от серого стола к белому и наоборот
from between_tables import to_white, to_gray
wait_msec(300)
joint_ptp("home", 5.4, 50,0) #Home position
wait_msec(500)
joint_ptp("p_1",5,50,0) #No singularity

line("point_2",200.0,1000.0,0.0,"belay31")
line("point_3",200.0,1000.0,0.0,"belay31")
wait_sec(1)
#Цикл по перемещению объектов с серого стола на белый
for i in range(4):
    pre=pre_gray[i]
    line("start_gray",200.0,1000.0,0.0,"belay31")
    wait_msec(400)
    lin_rel(pre,[0,0,0],"belay_table_figures",200.0,1000.0,False,0.0,"belay31")
    wait_msec(400)
    lin_rel(act_gray[i],[0,0,0],"belay_table_figures",200.0,1000.0,False,0.0,"belay31")
    wait_msec(400)
    taking()
    wait_sec(1)
    lin_rel([0,0,100],[0,0,0],"belay_table_figures",200.0,1000.0,False,0.0,"belay31")
    wait_msec(400)
    to_white()
    wait_msec(500)
    #функция по перемещению объектов на белом столе в зависимости от значения итерации цикла
    white_actions(i)
    wait_msec(400)
    if i==3:
        line("pre_white_home",200.0,1000.0,0.0,"belay31")
        joint_ptp("home", 5.4, 50,0) #Home position
    else:
        to_gray()

