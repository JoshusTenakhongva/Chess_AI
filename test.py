import pygame
from pygame.locals import (
    K_UP, 
    K_DOWN, 
    K_LEFT, 
    K_RIGHT, 
    K_ESCAPE, 
    KEYDOWN,
    QUIT,
)

class Player( pygame.sprite.Sprite ):
    
    def __init__( self, pygame ): 
        super( Player, self ).__init__()
        self.surf = pygame.Surface( (75, 75) )
        self.surf.fill( (0, 0, 0) )
        self.rect = self.surf.get_rect()
        self.movespeed = 1
        
    def update_position( self, pressed_keys ):
        if pressed_keys[ K_UP ]:
            self.rect.move_ip( 0, -self.movespeed) 
            
        if pressed_keys[ K_DOWN ]:
            self.rect.move_ip( 0, self.movespeed )
            
        if pressed_keys[ K_LEFT ]:
            self.rect.move_ip( -self.movespeed, 0 )
            
        if pressed_keys[ K_RIGHT ]:
            self.rect.move_ip( self.movespeed, 0 )
        

def main(): 
    
    # Initialize the screen size 
    screensize = { 'x': 600, 'y': 800 } 
    
    # Initialize the game and the screen we're gonna print to 
    pygame, screen = initialize_game( screensize )        
    
    # Start the main game loop 
    game_loop( pygame, screen, screensize )
    
def initialize_game( screensize ): 

    # Initialize pygame 
    pygame.init()    
    
    # Create the screen 
    screen = pygame.display.set_mode([ screensize['x'], screensize['y'] ])
    
    return pygame, screen
    
######################################
#
#   Game Loop 
#
######################################
def game_loop( pygame, screen, screensize ):
    
    # Create the player character and add them to a dict of actors
    actors = { 'player': Player( pygame ) }
    
    # Main game loop 
    running = True
    while running: 

        # Check if the user quits
        running = check_user_not_quit( pygame ) 
        
        # Check for events: user input, etc
        events = check_events( actors )
        
        # Update the states of the game objects
        update_game_object_states( pygame, events )
        
        # Update the display and audio
        update_display( pygame, screen, screensize, actors )
        
        update_audio()
    
    # If the game is no longer running, quit    
    pygame.quit()
    
    
#############################
#
#   Event Game Loop Functions
#
#############################
def check_user_not_quit( pygame ): 

    # Check if one of the events in the game is a quit 
    for event in pygame.event.get():
    
        # Check if the user hit the exit window button 
        if event.type == pygame.QUIT:
        
            # If so, return that the user quit
            return False
            
        if event.type == KEYDOWN and event.key == K_ESCAPE: 
            return False 
            
    # If no quit events occurred, do not quit the game
    return True
    
    
def check_events( actors ):

    check_user_input( actors )
    
    # Return the new events
    return True
    
    
def check_user_input( actors ):

    pressed_keys = pygame.key.get_pressed()
    
    actors['player'].update_position( pressed_keys )
    
        
############################
#
#   Object Info Updating Functions
#
############################
    
def update_game_object_states( pygame, events ):
    
    True
    
############################
#
#   Visual Updating Functions
#
############################
def update_display( pygame, screen, screensize, actors ):
    
    # Set the default background as white
    screen.fill(( 255, 255, 255 ))
    
    # Blit the player character into the screen
    screen.blit( actors['player'].surf, actors['player'].rect )
    
    # Updates the display   
    pygame.display.flip()
    
#############################
#
#   Audio Updating Functions
#
#############################  

def update_audio():
    True
    
      
def adjust_game_speed():
    True
    
    
# Calling Main
main()
    

