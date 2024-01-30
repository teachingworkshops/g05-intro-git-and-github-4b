class Assets:
    # ROOMS INFO
    ANNEX_EAST_NAME = 'Annex East'
    ANNEX_EAST_DESC = 'Annex East Desc'

    ANNEX_SOUTH_NAME = 'Annex South'
    ANNEX_SOUTH_DESC = 'Annex South Desc'

    ANNEX_CENTRAL_NAME = 'Annex Central'
    ANNEX_CENTRAL_DESC = 'Annex Central Desc'

    ANNEX_NORTH_NAME = 'Annex North'
    ANNEX_NORTH_DESC = 'Annex North Desc'

    IRA_ALLEN_NAME = 'Ira Allen'
    IRA_ALLEN_DESC = 'Ira Allen Desc'

    TANSEY_GYM_NAME = 'Tansey Gym'
    TANSEY_GYM_DESC = 'Tansey Gym Desc'

    BEATTY_NAME = 'Beatty'
    BEATTY_DESC = 'Beatty Desc'

    THE_QUAD_NAME = 'Quad'
    THE_QUAD_DESC = 'Quad Desc'

    WILLSON_HALL_NAME = 'Willson Hall'
    WILLSON_HALL_DESC = 'Willson Hall Desc'

    KINGSMAN_HALL_NAME = 'Kingsman Hall'
    KINGSMAN_HALL_DESC = 'Kingsman Hall Desc'

    RUBENSTEIN_HALL_NAME = 'Rubenstein Hall'
    RUBENSTEIN_HALL_DESC = 'Rubenstein Hall Desc'

    WILLISTON_HALL_NAME = 'Williston Hall'
    WILLISTON_HALL_DESC = 'Williston Hall Desc'

    WENTWORTH_HALL_NAME = 'Wentworth Hall'
    WENTWORTH_HALL_DESC = 'Wentworth Hall Desc'

    WATTSON_HALL_NAME = 'Wattson Hall'
    WATTSON_HALL_DESC = 'Wattson Hall Desc'                 

    #INTRO
    INTRO_MSG = r"""
    You wake up in an empty room of what seems to be a dungeon with a note that says:

    'Hello, this is Professor Gyllinsky. Welcome to the ACTUAL final project for our class.
    Remember when you told me that you didn't need math to be a good developer?
    If you want to escape this monster-filled dungeon, YOU will need your math skills. Good luck!'

    As confused as you are that a software engineering professor would go through this length of events
    just so you can prove your math skills, you see a door directly infront of you. 
    What will you do?
    """
    #GAME NAME
    GAME_NAME = r"""                                            
         ____          _         _   _            ____                          
        |    \ ___ ___|_|_ _ ___| |_|_|_ _ ___   |    \ _ _ ___ ___ ___ ___ ___ 
        |  |  | -_|  _| | | | .'|  _| | | | -_|  |  |  | | |   | . | -_| . |   |
        |____/|___|_| |_|\_/|__,|_| |_|\_/|___|  |____/|___|_|_|_  |___|___|_|_|
                                                               |___| 
            """
            
    #CREDITS
    CREDITS = r"""
    
    
    """
    
    #DEATH MESSAGES (make this a list of different death messages and return a random one when called method)
    def death_message():
        return "dead"
