#Строки вызова функций специально закомментированы. Если Вы захотите использовать только файл gripper_actions, то можете их раскомментировать.
#Однако при работе файла main, данные строки должны быть закомментированы. В противном случае, они будут воспроизводиться при запуске файла main.
def taking():
    wait_sec(1)
    set_do("Tool1_PNEV", True)
    wait_sec(1)
    set_do("Tool1_PNEV", False)
    wait_msec(500)
#taking()
def dropping():
    wait_sec(1)
    set_do("Tool23_PNEV", True)
    wait_sec(1)
    set_do("Tool23_PNEV", False)
    wait_msec(500)
#dropping()
