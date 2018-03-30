# -*- coding: utf-8 -*-
# <nbformat>4</nbformat>

# <codecell> {}

def how_many_flips(i):
    # Pull pancake stack from input
    all_pancake_sets = [map(int, y.split(' ')) for y in inp.split('\n')[1::3]]
    
    for pancakes in all_pancake_sets:
        #pancakes = map(int, inp.split('\n')[1].split(' ')) #11 5 2 10 3 5
        print '\nPancakes! ->', pancakes
        
        # Sort in reverse for reasons
        big_to_small = sorted(pancakes, reverse=True) #11 10 5 5 3 2
        flip_count = 0   
        
        for x in big_to_small: #x = 11
            where_we_want_it = len(big_to_small)-1
            unordered_pancakes = pancakes[0:where_we_want_it+1]
            big_pancake_idx = len(unordered_pancakes) - 1 - unordered_pancakes[::-1].index(x) #
            
            # check if it's where it's supposed to be. if not, do stuff.
            if big_pancake_idx != where_we_want_it:
                # fine. check if it's at the beginning. if not, place it at zero.
                if big_pancake_idx != 0:
                    # alright, how do we get it to 0.
                    # we figure out where it is right now (big_pancake_idx)
                    # so we grab the set of pancakes from 0 to and including that
                    top_cakes = pancakes[0:big_pancake_idx+1][::-1] # and flip it
                    bottom_cakes = pancakes[big_pancake_idx+1:] # grab the bottom ones 
                    
                    pancakes = top_cakes + bottom_cakes # MUSH 'EM TOGETHAH
                    flip_count += 1 # keep track o'dat
                    print 'Flip', flip_count, 'to ->', pancakes
    
                # okay, it's at zero now. flip 'em so it's where it's supposed to be
                
                # so now we know that the pancake is at index 0
                # but where do we want to flip it back to? the length of where_we_want_it
                top_cakes = pancakes[0:where_we_want_it+1][::-1] # and flipit
                bottom_cakes = pancakes[where_we_want_it+1:]
                
                pancakes = top_cakes + bottom_cakes # MUSH 'EM TOGETHAH
                flip_count += 1
                print 'Flip', flip_count, 'to ->', pancakes
                
            big_to_small = big_to_small[1:]
                
            if pancakes == sorted(pancakes):
                break#return flip_count
        #break#return flip_count            

# <codecell> {}

inp = '''8
7 6 4 2 6 7 8 7
----
8
11 5 12 3 10 3 2 5
----
10
3 12 8 12 4 7 10 3 8 10'''
how_many_flips(inp)

# <codecell> {"collapsed": true}



# <metadatacell>

{"kernelspec": {"display_name": "Python 2", "name": "python2", "language": "python"}}