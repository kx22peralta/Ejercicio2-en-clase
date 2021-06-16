from datasets import Simple, Split, Xor
N = 100
Simple(N, vis=True).graph("initial")

def simple_classify(pt):
    return 0.0 if pt[0] > 0.5 else 1.0

Simple(N, vis=True).graph("initial", model=simple_classify)