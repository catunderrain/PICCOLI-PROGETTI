
'''#------------------------------------------------#"""
|                                                      |
|      XXXX         X       XXXXXXXXX   X          X   |
|    XX    XX    XX   XX       XX       X X      X X   |
|   XX          XX     XX      XX       X   X  X   X   |
|   XX          XXXXXXXXX      XX       X  _    _  X   |
|    XX    XX   XX     XX      XX        X    _,   X   |
|      XXXX     XX     XX      XX        =====o=====   |
|                                                      |
|              HINZU & MOCHI PRESENTATION              |
'''#------------------------------------------------#"""

from termcolor import colored
color = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']


def Tinhhoanvi(chuoi, k): 
    global color
    k = (k+1)
    print(colored(f'>>> xetchuoi {chuoi}', color[k], attrs=['bold']))
    if len(chuoi) == 1:
        return [chuoi]
    allhoanvi = []
    
    for i in range(len(chuoi)):
        current = chuoi[i]; 
        print(colored(f' \\\n  \\__current {current}', color[k], attrs=['bold']))
        chuoiconlai = chuoi[:i] + chuoi[i+1:]
        for hoanvi in Tinhhoanvi(chuoiconlai, k):
            allhoanvi.append([current] + hoanvi)
            print(colored(f'|  hv in thv {hoanvi}', color[k], attrs=['bold']))
            print(colored(f'|       c+hv {[current] + hoanvi}', color[k], attrs=['bold']))
            print(colored(f'|________all {allhoanvi}\n', color[k], attrs=['bold']))

    return allhoanvi


if __name__ == '__main__':
    chuoi = [1,2,3]
    allhoanvi = Tinhhoanvi(chuoi, -1)

    import numpy as np
    r = 5
    print(colored('Results table'.center(30), attrs=['bold']))
    print(colored(f'{'-'*30}', attrs=['bold']))
    for i, hoanvi in enumerate(allhoanvi):
        print(colored(f'{i+1}{(r-len(str(i+1)))*' '} {np.array(hoanvi)}'.center(30), attrs=['bold']))
        pass
