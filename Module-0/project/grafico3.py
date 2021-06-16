from datasets import Simple, Split, Xor
N = 100
Simple(N, vis=True).graph("initial")

def xor_classify(pt):
    if pt[0] < 0.5 and pt[1] < 0.5 or pt[0] > 0.5 and pt[1] > 0.5:
        return 0.0
    else:
        return 1.0


Xor(N, vis=True).graph("initial", model=xor_classify)