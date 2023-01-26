def main():
    rgb = get_rgb_values()
    normalised = rgb_normaliser(rgb)
    
    print("[%.3f %.3f %.3f]" % (normalised[0], normalised[1], normalised[2]))
    
    closest_clr = closest_colour(normalised)
    print(closest_clr)

def get_rgb_values():
    clrs = ["red", "green", "blue"]
    rgb = []
    for i in range(3):
        val = input(f"Enter {clrs[i]} value: ")
        rgb.append(int(val))
    return rgb

def rgb_normaliser(rgb):
    import numpy as np
    clist = np.array(rgb)
    clist_max = max(clist)
    return clist / clist_max

if __name__ == "__main__":
    main()