def main():
    ar = [1,3,2,4,5,-1,-1]

    import random
    ar = random.sample(range(-50,50), 10)

    print(ar)
    arm = MergeSort(ar, 0, len(ar)-1)
    print(arm)
    armd = [-1 if (arm[i+1] - arm[i]) < 0 else 0 for i in range(len(arm)-1)]
    print(armd)
    
import cProfile
cProfile.run('main()')