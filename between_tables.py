#Здесь функции to_white() и to_gray() специально закомментированы. Если вы захотите проверить работу данного файла, можете их раскомментировать.
#Однако, если вы будете запускать файл main, данные строки должны быть закомментированы. Иначе данные функции будут воспроизводиться при импортировании их в файл main
#функция перехода от серого(сварочного стола) к белому столу
def to_white():
    line("point_1",200.0,1000.0,0.0,"belay31")
    line("point_2",200.0,1000.0,0.0,"belay31")
    line("point_3",200.0,1000.0,0.0,"belay31")
    line("point_4",200.0,1000.0,0.0,"belay31")
#to_white()
#функция перехода от белого стола к серому(сварочному столу)
def to_gray():
    line("point_4",200.0,1000.0,0.0,"belay31")
    line("point_3",200.0,1000.0,0.0,"belay31")
    line("point_2",200.0,1000.0,0.0,"belay31")
    line("point_1",200.0,1000.0,0.0,"belay31")
#to_gray()
