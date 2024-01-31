from enum import Enum

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

    ## MATH QUESTIONS

    easy_questions = [
        ("1 + 9", "10"),
        ("5 – 2", "3"),
        ("18 / 3", "6"),
        ("9 * 10", "90"),
        ("4 ** 3", "64")
    ]

    medium_questions = [
        ("Simplify 924/1092", "11/13"),
        ("6x + y = 25, 2x – 3y = 25", "5"),
        ("3(2y + 4) = 8y", "6"),
        ("Carol is three times older than Andrew. Brad is two years older than Andrew. In six years, the sum of Andrew’s and Brad’s ages will be the same as Carol’s age. How old is Carol?", "24"),
        ("13 – 2(2x + 1) = 1", "5/2"),
        ("f(x) is a function such that f(x) + 3 f(8 – x) = x for all real numbers x. Find the value of f(2).", "2"),
        ("A car travels from A to B at an average speed of 50 km/hour. At what average speed would it have to travel from B to A, averaging 60 km/hour for the whole trip?", "75"),
        ("Solve for x. 3x – 2y = 0, 3x + y = 9", "2"),
        ("Find the distance between (-4, -3) and (4, 3).", "10"),
        ("Solve for x. x / 5 + (x – 1) / 3 = 1/5", "1")
    ]

    hard_questions = [
        ("What’s the derivative: h(y) = y**-4 – 9y**-3 + 8y**-2 + 12", "-4y**-5+27y**-4–16y**-3 "),
        ("Find the derivative: (y**5 – 5y**3 + 2y)/(y**3)", "2y–4y**-3"),
        ("Find the derivative: z = 3x**3 -9x", "9x**2–9"),
        ("Find the derivative: g(z) = 4z**2 – 3z**-7 + 9z", "28z**6+21z**-8+9"),
        ("Find the tangent line to g(x) = 16/x – 4(x)**1/2 at x = 4.", "y=-2x+4"),
        ("Find the integral: 4x**6 – 2x**3 + 7x – 4.", "4/7x**7–(1/2)x**4+7/2x**2–4x+c"),
        ("Find the integral: 2cos(w) – sec(w)tan(w).", "2sin(w)–sec(w)+c"),
        ("Find the integral: 4sin(x/3).", "-12cos(x/3)+c"),
        ("Find the integral: (x+4)**(8/7) (x-3)**(6/7).", "[(x-3)]/(x+4)]**(1/7)"),
        ("Find the integral: cos(loge x)", "(x/2)[cos(logex)+sin(loge x)]+c"),
        ("The position of a particle is given by x(t) = t**3/3 – 4t**2 + 12t. In which time interval(s) does the particle have a positive velocity?", "[0,2) (6, infinity)"),
        ("Suppose a plane is traveling at a distance of s = f(t) which is a function of time, t, as given by s = f(t) = 8t**2 – 4t + 23. What is the planes acceleration?", "16"),
        ("Suppose that the number of people infected with the flu in a certain city is given by f(t) = 0.5e**t + t**2 in hundreds, with being the time in days since flu season began. How many times higher is the rate of spread of the flu on day 6 than day 2? (Round to nearest whole number)", "28"),
        ("Find the third derivative: x**5 + 2x**3 – x + 4", "60x**2+12"),
        ("Find the derivative: (3x-4)/(2x**2 – 1).", "(-6x**2+16x–3)/(2x**2–1)**2")
    ]
    
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

    class ENEMY_ID(Enum):
        SKELETON = 1
        VAMPIRE = 2
        WEREWOLF = 3
        GHOST = 4
        OGRE = 5

    # ENEMIES
    ENEMY_TYPES = {
        ENEMY_ID.SKELETON : "Skeleton",
        ENEMY_ID.VAMPIRE : "Vampire",
        ENEMY_ID.WEREWOLF : "Werewolf",
        ENEMY_ID.GHOST : "Ghost",
        ENEMY_ID.OGRE : "Ogre",
    }

    ENEMY_ART = { 
        ENEMY_ID.SKELETON :
r"""                                                                                
                                     ......                                     
                           ...........................                          
                      .....................................                     
                  ............................................                  
                .................................................               
              .....................................................             
             .......................................................            
           ..........................................................           
           ...........................................................          
          .............................................................         
          .............................................................         
          .............................................................         
          ...........*%%%%%%%*  ...................(%%%%%%%............         
          ........ %%%%%%%%%%%%%...............  %%%%%%%%%%%%( ........         
          ........%%%%%%%%%%%%%%%...............%%%%%%%%%%%%%%%........         
          .......#%%%%%%%%%%%%%%% ............ ,%%%%%%%%%%%%%%%.......          
           ......,%%%%%%%%%%%%%%(....... .......%%%%%%%%%%%%%%%.......          
           .......,%%%%%%%%%%%%.. ... .%%( ...  .(%%%%%%%%%%%% .......          
          .......  ..(%%%%%%*. ..... %%%%%%/ .......(%%%%%%*...........         
          .............. . ........ %%%%%%%%/.......... . .............         
          ........................ /%%%%%%%%%..........................         
          .........................(%%%%%%%%%.........................          
            ...................... . . ..  . .......................            
                 ...............................................                
                      ......................................                    
                      .....................................                     
                      ......,*,........,*,........,*,......                     
                      ......**.........**,.........**......                     
                        ..,**,.........**,.........,**,..                       
                              .........***........                              
""",
        ENEMY_ID.VAMPIRE :        
r"""
                                                                                
                                        ,,*****,                                
                      *,,,        ,,,,,,,,,,,,,,******,                         
                     **,,,,,,,,,,,,,,,,,,,,,,,,,,,,,****.                       
                     .*,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,**,,,                    
                .**,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,***                 
               ,**,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,***               
              .***,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,**.             
               ,*,,,,,,,,,(%%%%%%%%(,,,,,,,,/%%%%%%%%#,,,,,,,,,,,**             
             ,**,,,,,,,*%%%%%%%%%%%%%%#,,(%%%%%%%%%%%%%%*,,,,,,,,,*,            
             ***,,,,,,/%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%(,,,,,,,,*,            
             **,,,,,,*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%/,,,,,,,,             
             **,,,,,,#%%%%/******(%%%%%%%%%%%%#*******#%%%%,,,,,,,**            
            *****,,,,%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%(,,,,,,**.           
            ****,(*,*%%%%%%*,,,,*%%%%%%%%%%%%%%%,,,,,#%%%%%#,,,*,,,*.           
             **,/#/,(%%%%%%,,,,,*%%%%%%%%%%%%%%#,,,,,(%%%%%%,,((,,,,            
             ,,,*##*#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*/#(,,,             
              ,,,*(#%%%%%%%%%%%%%%%%%%#####%%%%%%%%%%%%%%%%%##(,,,.             
      /*,,,,,,,,,,,,*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#,,,,,,,,,,,,*,      
   *,,,,,,,,,,,,,,,,,/%%%%%%%%%%%//%%%%%%%%%%#*%%%%%%%%%%%#,,,,,,,,,,,,,,,,,,*  
    *,,,,,,,,,,,,,**,,,%%%%%%%%%%%(/*********/%%%%%%%%%%%/,,,*,,,,,,,,,,,,,*    
     ,*,,,,,,,,,,,,,,,,,*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#,,,,,,,,,,,,,,,,,*,     
       ,,,,,,,,,,,,,,,,,,,,#%%%%%%%%%%%%%%%%%%%%%%%%%*,,,,,,,,,,,,,,,,,,,       
         ,,,,,,,,,,,,,,,,,,,,,*%%%%%%%%%%%%%%%%%%(,,,,,,,,,,,,,,,,,,,,,         
           ,,,,,,,,,,,,,,,,,,,,,*(&@@@@@@@@@@@%/,,,,,,,,,,,,,,,,,,,,            
             ....,,,,****,*,,,,,@@@@@@@@@@@@@@@@/,,,,*,,,**,,,.....             
              ****,,,,,,*####*..@@@@@@@@@@@@@@@@*../###(,,,,,,,***.             
           ***,,,,,,,,....,,%/*%%%&@@@@@@@@@@&&%%(.#(,......,,,,,,,,*,          
         **,,,,,,,...........,%(&@@@@@@@@@@@@@@@/%/.............,,,,,,,.        
        *,,,,,,,................%&%&@@@@@@@@@%%&,.................,,,,,,,       
        ,,,,,,,.................%@@@@@@@@@@@@@@&,..................,,,,,,       
                                                                                
""",
        ENEMY_ID.WEREWOLF :            
r"""
                                                                                
                                                                                
       #############(                                       ##############(     
      /###################                             ###################(     
      /#####%&&&&&&%#############################################%%%######(     
      ,######&&&&&&&&&&&%#################################%&&&&&&&&&%#####(     
       %#####%&&&&&&&&&&&&%###########################%&&&&&&&&&&&&&######      
        (#####%&&&&&&&&&##################################%&&&&&&&&######.      
         #######&&&&&%######################################%&&&&%######        
           ######%&&#########################################%&%######.         
            #########################################################           
             (######################################################            
              #####################################################             
             (#############((#######################################            
            ############/......,#################(......(############           
          ##############,......./################.......*##############         
       .#################......,#################,......(################       
     /##############################################/(####################(     
   *#########################################################################   
  .###########################################################################, 
       .################################################################ /####  
     ###############&&&&&&&&&&&&%################%&&&&&&&&&&&############,      
     ##### ########%&&&&&&&&&&&&&&%############%&&&&&&&&&&%%%###### *####%      
          ################%&&&&&&&&%##(*,*/###&&&&&&&&&#############,           
         ,######&       ###%&&&&&&&,..........(&&&&&&%###       ###%*           
                        ,###%&&&&&%...........(&&&&&&###*                       
                         ####%&&&&&&%*......(&&&&&&&###%                        
                          *###%&/.%&&&(...*&&&%*.%&###/                         
                            ###%&&&(*/#&&&&(/(%&&%###,                          
                             ,#####%&&&&&&&&&&%####*                            
                                 ###############,                               
                                                                                
""",
        ENEMY_ID.GHOST :            
r"""
                                                                                
                               /&&&&&&&&&&&&&&&&&&&@                            
                           &&&&&&&&&&&&&&&&&&&&&&&&&&&&&                        
                        &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&,                     
                     /&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&                   
                   *&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@                 
                  #&&&&&&&&&&&&&&&&&&&&&&&&@@@@@@@@@&&&&&&&&&&&&                
 &&&&&&#         &&&&&&%...,(&&&&&&&&&&&&@@@@@@@@@@@@@&&&&&&&&&&@.       &&&&&&#
&&&&&&&&.       &&&&&&&&&&&#,.../&&&&&&&@@@@#.....(@@@@&&&&&&&&&&&      &&&&&&&&
@&&&&&&&&(     &&&&&&&&&#.........*&&&&&@@@@&,....&@@@@&&&&&&&&&&&/    &&&&&&&&#
 &&&&&&&&&&&  *&&&&&&&&(,&&&&&&&&&&&&&&&&@@@@@@@@@@@@@&&&&&&&&&&&%& (&&&&&&&&&&#
 (&&&&&&&&&&%%&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@@@@@@&&&&&&&&&&&&&&%&&&&&&&&&&&%& 
  .&&&&&&&&&%&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%&&&&&&&&&&%%  
    &&&&&&%%%&&&&&&&&/..,/(%&&&&&&&&&&&&&&&&&&&&&%#(*...%&&&&&&&%%&&&&&&%%%%/   
      &%%%%%%&&&&&&&&*.........................,........(&&&&&&&%%&%%%%%%&#     
         &%%%&&&&&&&&&*.......,*****************.......#&&&&&&&&%%%%%%%/        
            .@&&&&&&&&&%......*///////***//////*.....,&&&&&&&&%%%%&             
             #&&&&&&&&&&&&*...*/////////////////,..*&&&&&&&&&&%%%&              
             #&&&&&&&&&&&&&&&(*/////////////////#&&&&&&&&&&&&%%%&.              
              &&&&&&&&&&&&&&&&#////////////////(&&&&&&&&&&&&%%%%&.              
              *&&&&&&&&&&&&&&&&#//////////////(&&&&&&&&&&&%%%%%&                
              ,&&&&&&&&&&&&&&&&&&(//////////(&&&&&&&&&&&&%%%%%%,                
                &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%%%%%%%%                 
                /&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%%%%%%%%%&                  
                 .&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%%%%%%%%%%%%/                  
                   &&&&&&&&&&&&&&&&&&&&&&&&&&&%%%%%%%%%%%%%%%&                  
                     &&&&&&&&&&&&&&&&&&&&%%%%%%%%%%%%%%%%%%%%%%                 
                      .&&&&&&&&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#          
                        *&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%.         
                           .&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&%          
                               /&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&&              
                                    (&&%%%%%%%%%%%%%%%%%%&&%                                        
""",
        ENEMY_ID.OGRE :            
r"""
                                                                                
                  ,,,,,        ,,,,,,,,,,.                          .,,         
      ,,,,,,,,,,,,*%%#,,,,,,,   ,,,,,,,,,,,,.        ,,,,,(%%(,,,,,,,,,.    ,,  
       ,,,,,,,,,,*%%%%,,,,,,,,,  ,,,,,,,,,,,,,,   ,,,,,,,,#%%%#,,,,,,,,. .,,,,  
   ,.    .,,,,,,,#%%%%/,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,%%%%%*,,,,,,,,,,,,,,. 
    ,,,,,. .,,,,,#%%%%%*,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,(%%%%%/,,,,,,,,,,,,,,  
      ,,,,,,,,,,,#%%%%%%,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,(%%%%%#*,,,,,,,,,,,,,   
       ,,,,,,,,,,/%%%%%%%/,,,,,,,,,,,,,,,,,,,,,,,,,,,,*%%%%%%%#*,,,,,,,,,,,,.   
   ,,,. ,,,,,,,,,*##%%%%%%%#(/////*,,,,,,,,,,**/////(%%%%%%%%#(,,,,,,,,,,,,     
   ,,,,,,,,,,,,,,,*###%%%%###//////////////////////(##%%%%###(,,,,,,,,,,, ,,,,. 
  ,,,,,,,,,,,,,,,,,(#######(////////////////////////(########*,,,,,,,,,,,,,,,,. 
  ,,,,****,,,,,,,*///(((////////////////////////////////(((////,,,,,,,****,,,,. 
  ,,,,******,,,,*//////////////////////////////////////////////*,,,,******,,,,. 
  ,,,,********,,////////////////////////////////////////////////*,,*******,,,,. 
  ,,,,*******,,//////,,,,,,,,,,,,,,*/////////,,,,,,,,,,,,,,,/////,,,******,,,,  
  ,,,,******,,*////*,,,*&@@@@@@@(,,,,///////,,,,#@@@@@@@%,,,,*////,,,******,,,  
  ...,*****,,,*////*,,(@@@%...(@@@/,,//////*,,/@@@/...&@@@/,,*////*,,,*****...  
   ..,****,,,,//////,,(@@@*....%@@#,*///////*,#@@%....*&@@/,,/////*,,,,****..   
   ...***,,,,*///////*,*&@@@@@@@@/,///####////,(@@@@@@@@&,,*///////,,,,***,..   
    ...*,,,,,*//(######(/**,,,**/////######(/////*,,,,**/(#####(///,,,,,*,..    
     ...,,,,,*//##########////(##################(////(#########(//,,,,,,..     
      .,,,,,,.////(#######////(##/*(#########**###////(#######////*.,,,,,,      
       ,,,,,,.*//////////////////////(#####///////////////////////,.,,,,,.      
       ,,,,,,.,/////,***********/////////////////***********/////*..,,,,,       
       *,,,,,..,/////,,.  .**************************,.  ,,*/////,.,,,,,,       
        ,,,,,,,,,/////,,. ,@@@@,*@@@#.&@@@.*@@@& %@@@/  ,,*////*,,,,,,,,        
         ,,,,,,,,,/////*,,.*.                       ,,.,,/////,,,,,,,,,         
          ,,,,,,,, ./////,,,.   %@@@*.%@@@. @@@@,   ,,,*///// ,,,,,,,,          
            ,,,,,,   ,/////,,,,,,,,,,,,,,,,,,,,,,,,,,*/////   ,,,,,,            
             ,,,,,      */////****////////////****//////.      ,,,.             
                ,           *///////////////////////           *,               
                                   (/////////                                                                      
"""           

                            
    }

     
    ENEMY_ACTIONS = [
        "dancing like a disco inferno",
        "laughing uncontrollably at its own jokes",
        "pretending to be a superhero, cape flapping dramatically",
        "skipping with a silly grin",
        "spinning in circles until they're dizzy",
        "flapping its arms like a chicken trying to fly",
        "gobbling down food in record time",
        "whistling a tune while doing a handstand",
        "yodeling at the top of its lungs",
        "zigzagging through the room like a drunk",
        "clucking like a chicken while doing the chicken dance",
        "wiggling its eyebrows suggestively",
        "gulping down a glass of water in one go",
        "pretending to be a mime trapped in an invisible box",
        "twerking to its favorite song",
        "quacking like a duck for no apparent reason",
        "galloping around like a wild horse",
        "giggling uncontrollably at a cheesy rom-com",
        "hopping on one foot while rubbing its belly and patting its head",
        "waddling like a penguin",
        "screaming into a pillow",
        "pretending to be a robot malfunctioning",
        "doing the worm on the floor",
        "balancing a spoon on its nose",
        "playing air guitar",
        "attempting to lick its elbow",
        "doing the 'macarena' with enthusiasm",
        "trying to touch its nose with its tongue",
        "imitating a famous movie scene",
        "doing a somersault and landing clumsily",
        "performing a magic trick with household objects",
        "walking backward while pretending to moonwalk",
        "sneezing in slow motion",
        "pretending to be a dinosaur",
        "beatboxing with its mouth full",
        "mimicking the sound of a car engine revving",
        "putting on a puppet show with socks as characters",
        "playing a game of imaginary hopscotch",
        "balancing a book on its head while walking in circles",
        "attempting to breakdance on bubble wrap",
        "playing an invisible accordion",
        "doing the 'worm' on a slippery surface",
        "wobbling like a wacky inflatable tube man",
        "making funny faces in the mirror",
        "pretending to be a mime stuck in an invisible box",
        "juggling imaginary fruit",
        "hopping on one foot while patting its head and rubbing its stomach",
        "pretending to be a zombie with exaggerated movements",
        "balancing a broomstick on its chin",
        "hopping like a frog",
        "pretending to be a robot learning to dance",
        "doing a series of exaggerated sneezes",
        "walking in slow motion",
        "imitating a famous painting with its body",
        "pretending to be a ninja sneaking around",
        "performing an interpretive dance to a random song",
        "attempting to do the splits",
        "juggling invisible flaming torches",    
        "pretending to be a ninja dodging invisible obstacles",
        "trying to lick its elbow while hopping on one foot",
        "doing a dramatic interpretive dance to elevator music",
        "pretending to be a cat chasing an imaginary mouse",
        "practicing its best monster impressions",
        "doing the cha-cha-cha with an invisible partner",
        "attempting to do a handstand against the wall",
        "pretending to be a penguin sliding on ice",
        "hula-hooping with an invisible hula-hoop",
        "trying to touch its toes without bending its knees",
        "pretending to be a cowboy riding an invisible horse",
        "skipping backwards while singing the alphabet",
        "performing a series of dramatic hair flips",
        "hopping on one foot while making funny faces",
        "doing a series of ridiculous stretches",
        "practicing its best superhero poses",
        "pretending to be a mime stuck in an invisible box",    
]



