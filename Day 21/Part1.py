if __name__ == "__main__":
    with open("input.txt", "r") as f:
        l = [line.replace("contains", "").replace(")", "").strip() for line in f]

    l = [i.split(" ( ") for i in l]
    l = [[set(ingrs.split()), set(alrgs.split(", "))] for ingrs, alrgs in l]
 
    ingredients = set()
    for ingrs, _ in l:
        ingredients = ingredients | ingrs
     
    d = {} 
    for ingrs, alrgs in l:
        for alrg in alrgs:
            d[alrg] = d[alrg] & ingrs if alrg in d else ingrs    
    
    for item in d.values():
        ingredients = ingredients - item
  
    s = 0           
    for ingrs, _ in l:
        s += len(ingrs & ingredients)
    print(s)
