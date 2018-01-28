weight = [150,120,140,160,170]
height = [60,40,80,90,100]

def bmi(w,h):
    div1 = [a/b for a,b in zip(w,h)]
    return [x/y for x,y in zip(div1,h)] 
