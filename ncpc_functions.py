# -*- coding: utf-8 -*-
"""
Created on Tue May 12 00:28:04 2020

@author: jhaj
"""
import problem_a_14
import problem_i_14

def A_2013(N, t):
    t.sort(reverse=True)
    day_number = 1
    max_days = []
    for n in t:
        result = day_number + n + 1
        max_days.append(result)
        day_number += 1
    return max(max_days)

def E_2013(before, after):
    pass#TODO

def G_2013(N, before, after):
    pass#TODO

def A_2014(n, m, routes):
    
    # Build graph.
    G = problem_a_14.build_graph(routes)
    
    # Sort airports depending on routes.
    sorted_airports_groups = problem_a_14.sort_airports_by_routes(G)
    
    # In case of error from method sort_airports_by_routes.
    if sorted_airports_groups == "impossible":
        return "impossible"
    # No error yet and method returned list of three lists.
    else:
        airports_lounge = sorted_airports_groups[0]
        airports_no_lounge = sorted_airports_groups[1]
        undecided_airports = sorted_airports_groups[2]
    
        # All routes needs exactly one lounge between the airports it connects.
        if not airports_no_lounge and not airports_lounge:
            # Special case: 2-color algorithm.
            return problem_a_14.two_coloring(G)
        else:
            # Regular case.
        
            # Traverse the undecided airports.
            for airport in undecided_airports:            
            
                # Boolean is there lounges in neighbour airports.
                lounges = False
            
                # Convert list iterator object of 
                # adjacent vertices into a list.
                neighbour_airports = list(G.adjacent_vertices(airport))
            
                # Traversal of neighbour airports to this airport.
                for n in neighbour_airports:
                    # Search negihbours for lounges.
                    for airport_l in airports_lounge:
                        # Detected a lounge in neighbour.
                        if n is airport_l:
                            lounges = True
                        else:
                            continue            
            
                # None of the neighbour airports have a lounge.
                if not lounges:
                    # Add a lounge to this airport.
                    airports_lounge.append(airport)
        
    # Result
    return len(airports_lounge)
      
    
def D_2014(Gunnars_dice, Emmas_dice):
    pass#TODO

def E_2014(n, h):
    pass#TODO

def G_2014(n, k, x):
    pass#TODO

def I_2014(n, lines):
    
    num_of_squares = 0
    
    sorted_slopes = problem_i_14.sort_lines_slope(lines)
    sorted_orthogonals = problem_i_14.sort_lines_orthogonal(sorted_slopes)
    sorted_distances = problem_i_14.sort_lines_distance(sorted_orthogonals, sorted_slopes)

    for t in sorted_distances:
        dict_a = t[0]
        dict_b = t[1]
        
        for dist_a in dict_a:
            for dist_b in dict_b:
                if dist_a == dist_b:
                    nl_a = dict_a[dist_a]
                    nl_b = dict_b[dist_b]
                    squares = nl_a * nl_b
                    num_of_squares += squares
                else:
                    continue
    return num_of_squares