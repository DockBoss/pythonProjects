# Snake Methods/notes
I am using this as a think pad to fix current problems in my snake project.

## Snake
### movements
I need to edit the movements of the snake so it is always moving and when there is no key pressed.
1. abstract the movements from snake class and add it to the main loop
2. or just edit how the movements are read in and adjust the update function of snake accordinly 
### Resizing
I need to find a way to resize the sprite.
1. See if you can keep adding rect's to the sprite
    * Probably will not work, IDK how I would handle remembering where it was when re-printing 
1. Add a body sprite that will be placed directly on the behind the last sprite
    * Might need to create a function to help placing the body on the screen
        * just remember the side that the trailing sprite was connected to
    * This will also make collision detecton really easy.
### collision detecton
Need to figure out how to tell when the game is over
1. Not sure how I would handle it in this case.
2. .kill the snake when it collides with the body and end the game
    * Maybe I don't need to .kill the snake or body at all. Just end the game loop


## Food
### generating food
look into pygame events more

look into groupSingle
### randomly placing food                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      