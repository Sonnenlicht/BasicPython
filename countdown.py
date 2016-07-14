#! python3

import sys, time

num = int(sys.argv[1])
ctrl_c_pressed_already = False

for num in range(num, 0, -1):
    try:
        time.sleep(1)
        print(num)
    except KeyboardInterrupt:
        if ctrl_c_pressed_already:
            exit(1)
        print('^C Press Ctrl-C again to exit')
        ctrl_c_pressed_already = True
        
