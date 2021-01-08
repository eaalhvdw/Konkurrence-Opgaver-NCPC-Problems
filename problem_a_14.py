# -*- coding: utf-8 -*-
"""
Created on Tue May 19 16:57:28 2020

@author: Louise Hamle
"""
from edge_list_graph import Graph as Graph
from edge_list_graph import Vertex as Vertex

# Build graph from routes information.
def build_graph(routes):
    
    G = Graph()
    
    for r in routes: # r = [a, b, c], a & b: Vertices, c: int edge label.
        a1 = r[0]
        a2 = r[1]
        c = r[2]
        
        v1 = Vertex(a1)
        v2 = Vertex(a2)
        
        vertices = list(G.vertices())
        
        if vertices:
            found_v1 = False
            found_v2 = False
            v1_str = v1.__str__()
            v2_str = v2.__str__()
            
            for v in vertices:
                v_str = v.__str__()
                
                if v_str == v1_str:
                    found_v1 = True
                    va = v
                elif v_str == v2_str:
                    found_v2 = True
                    vb = v
                else:
                    continue
            if not found_v1:
                va = G.insert_vertex(a1)
            if not found_v2:
                vb = G.insert_vertex(a2)
        else:
            va =  G.insert_vertex(a1)
            vb = G.insert_vertex(a2)
    
        G.insert_edge(c, va, vb)
    
    return G


# Sort airports in routes with 2, 0 or 1 lounges.
def sort_airports_by_routes(graph):   
    airports_lounge = []
    airports_no_lounge = []
    undecided_airports = []

    # Convert list iterator object of 
    # vertices in graph into a list.
    airports = list(graph.vertices())
    
    for a in airports:
        routes_a = list(graph.incident_edges(a))
        
        must_have_lounges_a = 0
        cannot_have_lounges_a = 0
        undecided_a = 0
        
        for r_a in routes_a:
            # Convert edge object into an int 
            # value by means of string methods.
            r_int = int(r_a.__str__())
            
            if r_int == 2:
                must_have_lounges_a += 1
            elif r_int == 0:
                cannot_have_lounges_a += 1
            else:
                undecided_a += 1
        
        if must_have_lounges_a != 0 and cannot_have_lounges_a != 0:
            return "impossible"
        elif must_have_lounges_a != 0:
            if not airports_lounge:
                airports_lounge.append(a)
            else:
                found_m_a = False
                for m_a in airports_lounge:
                    if a is m_a:
                        found_m_a = True
                    else:
                        continue
                if not found_m_a:
                    airports_lounge.append(a)
                else:
                    continue       
        elif cannot_have_lounges_a != 0:
            if not airports_no_lounge:
                airports_no_lounge.append(a)
            else:
                found_cn_a = False
                for cn_a in airports_no_lounge:
                    if a is cn_a:
                        found_cn_a = True
                    else:
                        continue
                if not found_cn_a:
                    airports_no_lounge.append(a)
                else:
                    continue         
        else:
            if not undecided_airports:
                undecided_airports.append(a)
            else:
                found_u_a = False
                for u_a in undecided_airports:
                    if a is u_a:
                        found_u_a = True
                    else:
                        continue
                if not found_u_a:
                    undecided_airports.append(a)
                else:
                    continue
    return [airports_lounge, airports_no_lounge, undecided_airports]


# 2-coloring algorithm: resolve 
# special case - all routes are 1.
def two_coloring(graph):
    # Colors
    red = []
    green = []

    # Get airports from graph.
    airports = list(graph.vertices())
    
    # Color first.
    first = airports[0]
    green.append(first)
    
    # Color all neighbour airports to
    # the first airport another color.
    first_neighbors = graph.adjacent_vertices(first)
    for neighbor in first_neighbors:
        red.append(neighbor)
    
    # Color the rest of the airports such 
    # that no two neighbour airports are 
    # the same color. Return impossible
    # if impossible.
    for airport in airports:
        # Skip the first.
        if airport is first:
            continue
        else:
            # Airport is green.
            if airport in green:
                neighbours = graph.adjacent_vertices(airport)
                for neighbour in neighbours:
                    # Neighbour is already red.
                    if neighbour in red:
                        continue
                    # All neighbour airports must be red.
                    elif neighbour in green:
                        return "impossible"
                    # Neighbour has no color yet.
                    else:
                        red.append(neighbour)
            # Airport is red.
            elif airport in red:
                neighbours = graph.adjacent_vertices(airport)
                for neighbour in neighbours:
                    if neighbour in green:
                        continue
                    elif neighbour in red:
                        return "impossible"
                    else:
                        green.append(neighbour)
            # Airport has no color
            else:
                neighbours = graph.adjacent_vertices(airport)
                red = 0
                green = 0
                # Evaluate neighbours' colors.
                for neighbour in neighbours:
                    if neighbour in red:
                        red += 1
                    elif neighbour in green:
                        green += 1
                    else:
                        continue
                if red != 0 and green != 0:
                    return "impossible"
                elif red != 0:
                    green.append(airport)
                else:
                    red.append(airport)
                        
    # Return the smallest amount of vertices.
    if len(green) < len(red):
        return len(green)
    else:
        return len(red)
