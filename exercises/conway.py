# Conway's Game of Life

'''
    Conway's Game of Life is a grid of cells
    Each cell is either alive or dead
    Over time, cells live and die, and can be reborn

    The rules (as the grid evolves to the next generation):
        1. A live cell with fewer than two neighbours dies (underpopulation)
        2. A live cell with more than three neighbours dies (overpopulation
        3. A live cell with exactly three neighbours lives on
        4. A dead cell with exactly three neighbours is born (reproduction)

            0.0             0..
            00.     ==>     0.0
            ..0             00.

'''

### 1. Start by writing a function that calculates whether the cell should be
### alive or dead in the next generation

def evolve_cell(alive, neighbours):
    alive = True ### change this bit, then return the value
    return alive

# Write some tests here to check it works as expected
# It's good practise to write the tests first
assert evolve_cell(alive=False, neighbours=0) == False
assert evolve_cell(alive=True, neighbours=0) == True
# Add more tests when they're all passing...

print '''
    If you see this message it means all your tests are passing.
    Do you need to write another test?
    '''

### 2. Once you're happy the function works, try evolving a whole grid

### 3. Once you can evolve a full grid, try printing out the grid each time
