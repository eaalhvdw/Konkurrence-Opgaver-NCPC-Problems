# -*- coding: utf-8 -*-
"""
Created on Tue May 12 12:14:14 2020

@author: Louise Hamle
"""

import itertools
import math

""" Beregn hældning for alle linjer og lav dictionaries
    med linjer der har samme hældningskoefficient. """
def sort_lines_slope(lines):
    
    slope_dicts = []
    
    for line in lines:
        line_tuple = tuple(line)
        x1 = line_tuple[0]
        y1 = line_tuple[1]
        x2 = line_tuple[2]
        y2 = line_tuple[3]
        
        try:
            a = (y2 - y1)/(x2 - x1)
        except ZeroDivisionError:
            # Vertical line.
            a = "undefined"

        if not slope_dicts:
            slope = {line_tuple: a}
            slope_dicts.append(slope)
        else:
            found = False
            for slope in slope_dicts:
                if a in slope.values():
                    slope[line_tuple] = a
                    found = True
                    break
            if not found:
                slope = {line_tuple: a}
                slope_dicts.append(slope)    
    return slope_dicts


""" Grupper hældningsloefficienterne for ortogonale linjer parvist. """
def sort_lines_orthogonal(slope_dicts):
    
    orthogonals = []
    slopes = []
    
    for d in slope_dicts:
        a = list(d.values())[0]
        slopes.append(a)
        
    for i in range(len(slopes)):
        for j in range(i + 1, len(slopes)):
            try:
                if slopes[i] * slopes[j] == -1:
                    pair = (slopes[i], slopes[j])
                    orthogonals.append(pair)
            except TypeError:
                if type(slopes[i]) is str and slopes[j] == 0.0:
                    pair = (slopes[i], slopes[j])
                    orthogonals.append(pair)
                elif slopes[i] == 0.0 and type(slopes[j]) is str:
                    pair = (slopes[i], slopes[j])
                    orthogonals.append(pair)
                else:
                    continue  
    return orthogonals


""" Hjælpemetode: Beregn den korteste afstand mellem to linjer. """
def distance_between(l1, l2):
    
    l1_x1 = l1[0]
    l1_y1 = l1[1]
    l1_x2 = l1[2]
    l1_y2 = l1[3]
    
    l2_x1 = l2[0]
    l2_y1 = l2[1]
    l2_x2 = l2[2]
    l2_y2 = l2[3]
    
    P = ()
    
    try:
        a1 = (l1_y2 - l1_y1)/(l1_x2 - l1_x1)
    except ZeroDivisionError:
        # a1 is undefined, because l1 is vertical. 
        # a1 must be initialised, here I chose value 0.
        a1 = 0
        P = (l1_x1, l1_y1)

    try:
        a2 = (l2_y2 - l2_y1)/(l2_x2 - l2_x1)
    except ZeroDivisionError:
        # a2 is undefined because l2 is vertical. 
        # a2 must be initialised, here I chose value 0.
        a2 = 0
        P = (l2_x1, l2_y1)
    
    if not P:
        # A point on one of the lines.
        P = (l1_x1, l1_y1)
        # Calculate equation: y = ax + b
        # for the other line.
        b = l2_y1 - a2 * l2_x1
        dist_P_l = (abs(a2 * P[0] + b - P[1]))/math.sqrt(pow(a2, 2) + 1)
        return round(dist_P_l, 6)
    else:
        if P[0] == l1_x1:
            b = l2_y1 - a2 * l2_x1
            # l: y = a2x + b
            # P: (l1_x1, l1_y1)
            dist_P_l = (abs(a2 * P[0] + b - P[1]))/math.sqrt(pow(a2, 2) + 1)
            return round(dist_P_l, 6)
        else:
            b = l1_y1 - a1 * l1_x1
            # l: y = a1 * x + b
            # P: (l2_x1, l2_y1)
            dist_P_l = (abs(a1 * P[0] + b - P[1]))/math.sqrt(pow(a1, 2) + 1)
            return round(dist_P_l, 6)


""" Sorter ortogonale linjer efter afstand. """
def sort_lines_distance(orthogonals, slope_dicts):
    
    # Tuples with pairwise dictionaries.
    sorted_distance_tuples = []
    
    # Traversal of tuples with pairs of slopes.
    for pair in orthogonals:
        line_group_a = []
        line_group_b = []
        
        # Traversal of disctionaries
        # of lines with equal slopes.
        for d in slope_dicts:
            v = list(d.values())[0]
            a = pair[0]
            b = pair[1]
            
            # Find all lines with slope a, special cases.
            if type(a) is str and v == 0.0:
                for k in d:
                    line_group_a.append(k)
            elif a == 0 and type(v) is str:
                for k in d:
                    line_group_a.append(k)
            # Find all lines with slope b, special cases.
            elif type(b) is str and v == 0.0:
                for k in d:
                    line_group_b.append(k)
            elif b == 0 and type(v) is str:
                for k in d:
                    line_group_b.append(k)
            else:
                # Find all lines with slope a, normal cases.
                if v == a:
                    for k in d:
                        line_group_a.append(k)
                # Find all lines with slope b, normal cases.
                elif v == b:
                    for k in d:
                        line_group_b.append(k)
                else:
                    continue
        
        # Two lists of pairwise combinations of lines for lines
        # with slope a and for lines with slope b respectively.
        combinations_a = list(itertools.combinations(line_group_a, 2))
        combinations_b = list(itertools.combinations(line_group_b, 2))
        
        # Dictionary with distance as key
        # and number of lines as value.
        distance_dicts_a = {}
        distance_dicts_b = {}
    
        # Calculate the distance between each 
        # pair of combinations in each of the 
        # two lists of combinations. Sort the
        # combinations from each of the lists 
        # by distance and make a dictionary
        # for each of the lists with distance 
        # as key and number of lines withethat 
        # distance as value.
        for c in combinations_a:
            dist = distance_between(c[0], c[1])
            
            if dist in distance_dicts_a:
                distance_dicts_a[dist] += 1
            else:
                distance_dicts_a[dist] = 1
            
        for c in combinations_b:
            dist = distance_between(c[0], c[1])
            
            if dist in distance_dicts_b:
                distance_dicts_b[dist] += 1
            else:
                distance_dicts_b[dist] = 1
        
        # Save the two dictionaries in a tuple.
        orthogonal_pair_dicts_distances = (distance_dicts_a, distance_dicts_b)
        # Add the tuple to the list of sorted tuples.
        sorted_distance_tuples.append(orthogonal_pair_dicts_distances)
        
    return sorted_distance_tuples


#----------------------------- Test area --------------------------------------
"""
print("TEST 1: sort_lines_slope")
lines = [
    [0, 0, 1, 0],
    [0, 1, 1, 1],
    [0, 2, 2, 2],
    [0, 0, 0, 4],
    [1, -1, 1, 0],
    [2, -2, 2, 2],
    [1, 1, 2, 2],
    [1, 1, 0, 2],
    [3, 1, 2, 2],
    [1, 3, 0, 2]
    ]
print("Slopes list with dictionaries of lines and slope values grouped by slope:", sort_lines_slope(lines), "\n")

print("TEST 2: sort_lines_orthogonal")
slope_dicts = sort_lines_slope(lines)
orthogonals = sort_lines_orthogonal(slope_dicts)
print("Orthogonals list with tupels of slope values for orthogonal lines:", orthogonals, "\n")

print("TEST 3: distance_between")
l1 = (0, 0, 0, 4)
l2 = (1, -1, 1, 0)
distance = distance_between(l1, l2)
print("Linje l1:", l1)
print("Linje l2:", l2)
print("Den korteste afstand mellem l1 og l2:", distance, "\n")

print("TEST 4: sort_lines_distance")
sorted_lines_distance = sort_lines_distance(orthogonals, slope_dicts)
print("Distance list with tuples of pairwise dictionaries with orthogonal lines sorted by distances.", sorted_lines_distance, "\n")

"""