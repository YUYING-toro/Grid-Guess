from graphics import Canvas
import random 

    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400

CELL_SIZE = 50
ERASER_SIZE = 20

def load_numbers_from_file(filepath):
    numbers = []
    with open(filepath, 'r') as file_reader:
        for line in file_reader.readlines():
            cleaned_line = line.strip()
            if cleaned_line != '':
                numbers.append(cleaned_line)
    
    return numbers

def erase_objects(canvas):
    canvas.wait_for_click()
    """Erase objects in contact with the eraser"""
    mouse_x=canvas.get_mouse_x()
    mouse_y=canvas.get_mouse_y()

    start_x=mouse_x
    start_y=mouse_y

    end_x = start_x+ERASER_SIZE
    end_y = start_y+ERASER_SIZE
    overlapping_objs=canvas.find_overlapping(start_x,start_y
        ,end_x,end_y)
    canvas.set_hidden(overlapping_objs[0], True)

def gameFuntion (canvas):
    number_list = load_numbers_from_file("words.txt")
    rand_num = random.randint(0, len(number_list)-1)
    ans=number_list[rand_num]

    #display word
    cell_heigh = [1.25,2,4,400]
    random_heigh = random.choice(cell_heigh)

    canvas.create_text(
        CANVAS_WIDTH/10, 
        CANVAS_HEIGHT/random_heigh,
        text = ans,
        font = 'Arial', 
        font_size = 70, 
        color ='blue')
    #hide word
    num_rows = CANVAS_HEIGHT // CELL_SIZE
    num_cols = CANVAS_WIDTH // CELL_SIZE  
    for row in range(num_rows):
        for col in range(num_cols):
            left_x = col * CELL_SIZE
            top_y = row * CELL_SIZE
            right_x = left_x + CELL_SIZE
            bottom_y = top_y + CELL_SIZE
            
            # Create a single cell in the grid
            cell = canvas.create_rectangle(left_x, top_y, right_x, bottom_y, 'blue',"black")
        
    
    #eraser>> detect mouse
    canvas.wait_for_click()
    last_click_x, last_click_y = canvas.get_last_click()  # Get the starting location for the eraser

    eraser = canvas.create_rectangle(
        last_click_x, 
        last_click_y, 
        last_click_x + ERASER_SIZE, 
        last_click_y + ERASER_SIZE, 
        'pink'
    )

    while True:
        #let the eraser move aligned with the mouse
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_y()
        canvas.moveto(eraser, mouse_x, mouse_y)        
        erase_objects(canvas)

        
def main():
    input("Welcome to Grid & Guess! Use your virtual eraser to uncover one tile at a time and guess the hidden word. Press Enter to start the game.")
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    gameFuntion(canvas)


if __name__ == '__main__':
    main()
