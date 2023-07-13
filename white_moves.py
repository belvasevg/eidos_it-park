#функция по перемещению объектов на белом столе
def white_actions(i):
    #Импортируем функцию закрытия трёхкулачкового захвата
    from gripper_actions import dropping
    #импортируем расчёт смещений из функции white_table()
    from calculation import white_table
    act_white,pre_white = white_table()
    pre=pre_white[i]
    act=act_white[i]
    #После присваивания списка переходи в старовую точку из которой будут производиться смещения
    line("start_pos_white",200.0,1000.0,0.0,"belay31")
    wait_msec(400)
    lin_rel(pre,[0,0,0],"belay_white_table",200.0,1000.0,False,0.0,"belay31")
    wait_msec(400)
    lin_rel(act,[0,0,0],"belay_white_table",200.0,1000.0,False,0.0,"belay31")
    wait_msec(400)
    dropping()
    wait_msec(400)
    lin_rel([0,0,180],[0,0,0],"belay_white_table",200.0,1000.0,False,0.0,"belay31")
    wait_msec(400)
