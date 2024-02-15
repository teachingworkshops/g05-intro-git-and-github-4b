from enum import Enum

class Assets:
    # ROOMS INFO
    ANNEX_EAST_NAME = 'Annex East'
    ANNEX_EAST_DESC = 'This area kind of feels like the east of a certain Annex building.'

    ANNEX_SOUTH_NAME = 'Annex South'
    ANNEX_SOUTH_DESC = 'Halls! Halls! And more halls!'

    ANNEX_CENTRAL_NAME = 'Annex Central'
    ANNEX_CENTRAL_DESC = 'There is no elevator here? And your class is on the top floor? I hope you brought some trail mix for that hike.'

    ANNEX_NORTH_NAME = 'Annex North'
    ANNEX_NORTH_DESC = 'You stand confused and scared. *The developers have never been in this area*'

    IRA_ALLEN_NAME = 'Ira Allen'
    IRA_ALLEN_DESC = 'I went once to this building and it was locked? At least it\'s open now.'

    TANSEY_GYM_NAME = 'Tansey Gym'
    TANSEY_GYM_DESC = 'A large gymnasium. Although you were the worst at basketball, no one is going to judge you here.'

    BEATTY_NAME = 'Beatty'
    BEATTY_DESC = 'The scent of food fills the air. At the same time feeling like it\'s crowded despite no one else being here. You want to sit down, but all the seats are taken... they always are.'

    THE_QUAD_NAME = 'Quad'
    THE_QUAD_DESC = 'A large square of grass. This place connects all other buildings in the vicinity.'

    WILLSON_HALL_NAME = 'Willson Hall'
    WILLSON_HALL_DESC = 'Very spacious rooms compared to the other building\'s rooms.'

    KINGSMAN_HALL_NAME = 'Kingman Hall'
    KINGSMAN_HALL_DESC = 'A long hallway connecting Willson and Rubenstein. A bunch of big fancy machines fill each room'

    RUBENSTEIN_HALL_NAME = 'Rubenstein Hall'
    RUBENSTEIN_HALL_DESC = 'There are a few vending machines here, you could stop and snack for a bit. Wait... $3.75 for a 4 ounce bag of jerky... daylight robbery.'

    WILLISTON_HALL_NAME = 'Williston Hall'
    WILLISTON_HALL_DESC = 'Sometimes, it feels like a sauna, other times... well, actually it always feels like a sauna... for better or for worse.'

    WENTWORTH_HALL_NAME = 'Wentworth Hall'
    WENTWORTH_HALL_DESC = 'Some of these desks do not look very comfortable to sit in. There is no way it can fit a laptop and a notebook at the same time. At least the technology hallway is pretty.\nThis is the exit, remember to have the key ready.'

    WATTSON_HALL_NAME = 'Watson Hall'
    WATTSON_HALL_DESC = 'A really big auditorium brings back old memories. You were here on day 1, now you are back again, how nostalgic.'
    
    CEIS_NAME = 'CEIS'
    CEIS_DESC = 'Everything looks new and better compared to the other buildings. The exterior is made of glass, so maybe put down the rock before someone turns you into a saying.'

    DELIMIT = "------------------------------------------------------"
    
    ## MATH QUESTIONS

    ##A few questions were deemed too easy or too hard and so to keep the game challenging but not impossible for the average player, they were commented out in their respecitve sections.
    ##Some of the remaining questions have also been slightly edited and reformated.

    # removed_easy = [
    #     ("1 + 9", "10"),
    #     ("5 – 2", "3"),
    #     ("18 / 3", "6"),
    #     ("1 + 1", "2"),
    #     ("9815 * 0", "0")
    #     ]

    #easy_questions = [("What’s the derivative: h(y) = \u222B y\u207B\u2074 – 9y\u207B\u00B3 + 8y\u207B\u00B2 + 12", "-4y^-5+27y^-4–16y^-3")]

    easy_questions = [
        ("9 * 12", "108"),
        ("4\u00B3", "64"),
        ("4\u00B9\u2215\u00B2", "2"),
        ("5 + 9 * 2", "23"),
        ("-4 + 10 * 5 / 2", "21"),
        ("8 * -3 + 7", "-17"),
        ("16 * 2 / 4 * -3", "-24"),
        ("7\u00B2", "49"),
        ("8 - 26", "-18"),
        ("11 * 11", "121"),
        ("89 - 17 * 2", "55"),
        ("109 + 11 * 3", "142"),
        ("18 * 3", "54"),
        ("42 + 79", "121"),
        ("86 * 3", "258")
    ]

  
    # removed_medium = [
    #     ("f(x) is a function such that f(x) + 3 f(8 – x) = x for all real numbers x. Find the value of f(2).", "2"),
    #     ("If a^2 - b^2 = 8 and a*b = 2, find a^4 + b^4.", "72"),
    #     ("Complete the square by adding a number to both sides: x^2 - 8x + 3 = 0.", "16"),
    #     ("What is the point of intersection of the lines x - y = 3 and -5x - 2y = -22?", "(4,1)"),
    # ]

    medium_questions = [
        ("Solve for x in this system of equations: 6x + y = 25, 2x – 3y = 25", "5"),
        ("Solve for y in the equation: 3(2y + 4) = 8y", "6"),
        ("Carol is three times older than Andrew. Brad is two years older than Andrew. In six years, the sum of Andrew’s and Brad’s ages will be the same as Carol’s age. How old is Carol?", "24"),
        ("Solve for x in this equation(be sure to simply your answer): 13 – 2(2x + 1) = 1", "5/2"),
        ("A car travels from A to B at an average speed of 50 km/hour. At what average speed would it have to travel from B to A, averaging 60 km/hour for the whole trip?", "75"),
        ("Solve for x. 3x – 2y = 0, 3x + y = 9", "2"),
        ("Find the distance between (-4, -3) and (4, 3).", "10"),
        ("Solve for x. x / 5 + (x – 1) / 3 = 1/5", "1"),
        ("If 6x = 42 and xk = 2, what is the value of k?", "2/7"),
        ("If 4x + 5 = 13x + 4 - x - 9, then what is x?", "5/4"),
        ("Solve for z: 5(z - 2) = 2(z - 3)", "4/3"),
        ("What is the x intercept coordinate of the line -3x + y = 3?", "(-1,0)"),
        ("(x + 5) / 4 = (x -3) / 2", "11"),
        ("Solve for x. \u221B64 + 8  - x = 5x", "2")
    ]

    # removed_hard = [("Find the integral: cos(loge x)", "(x/2)(cos(logex)+sin(loge x))+c"),
    #                 ("The position of a particle is given by x(t) = t^3/3 – 4t^2 + 12t. In which time interval(s) does the particle have a positive velocity?", "[0,2) (6, infinity)"),
    #                 ]
    
    hard_questions = [
        ("Find the derivative: y\u207B\u2074 – 9y\u207B\u00B3 + 8y\u207B\u00B2 + 12", "-4y^-5+27y^-4–16y^-3"),
        ("Find the derivative: (y\u2075 – 5y\u00B3 + 2y)/(y\u00B3)", "2y–4y^-3"),
        ("Determine the derivative: 3x\u00B3 -9x", "9x^2–9"),
        ("Find the derivative: 4z\u00B2 – 3z\u207B\u2077 + 9z", "28z^6+21z^-8+9"),
        ("Find the integral: \u222B 4x\u2076 – 2x\u00B3 + 7x – 4.", "4/7x^7–(1/2)x^4+7/2x^2–4x+c"),
        ("Determine the integral: \u222B 2cos(w) – sec(w)tan(w).", "2sin(w)–sec(w)+c"),
        ("Find the integral: \u222B 4sin(x/3).", "-12cos(x/3)+c"),
        ("Suppose a plane is traveling at a distance of s = f(t) which is a function of time, t, as given by s = f(t) = 8t^2 – 4t + 23. What is the planes acceleration?", "16"),
        ("Find the third derivative: x\u2075 + 2x\u00B3 – x + 4", "60x^2+12"),
        ("Determine the derivative: (3x-4)/(2x\u00B2 – 1).", "(-6x^2+16x–3)/(2x^2–1)^2"),
        ("Solve for the second derivative: y = 2t\u2074 - 10t\u00B2 + 13t", "24t^2-20"),
        ("Find the derivative: y = x(3x\u00B2 - 9)", "9x^2-9"),
        ("Solve for the derivative: x = (y - 4)(2y + y\u00B2)", "3y^2-4y-8"),
        ("Solve the integral: \u222B w\u207B\u00B2 + 10w\u207B\u2075 - 8w.", "-w^-1-(5/2)w^-4-8w+c")
    ]

    # removed_boss = [("Determine where the tangent line to f(x) = x^3 - 5x^2 + x is parallel to the line y = 4x + 23. Round to nearest hundredth.", "3.61"),
    #     ("What's the local minimum of f(x) = (2/3)x^3 + 7x^2 - 12x when -10 <= x <= 10. Round to the nearest hundredth.", "0.77")]
    
    boss_questions = [
        ("Suppose that the number of people infected with the flu in a certain city is given by f(t) = 0.5e^t + t^2 in hundreds, with being the time in days since flu season began. How many times higher is the rate of spread of the flu on day 6 than day 2? (Round to nearest whole number)", "28"),
        ("Determine the fourth derivative: 3t\u2077 - 6t\u2074 + 8t\u00B3 - 12t + 98", "630t^4-144t+48"),
        ("Find the integral: \u222B (x+4)^(8/7) (x-3)^(6/7).", "((x-3)/(x+4))^(1/7)"),
        ("Solve the integral: \u222B sin(x) + 10csc^2(x)", "-cos(x)-10cot(x)+c"),
        ("Determine f(x) given that f'(x) = 12x^2 - 4x and f(-3) = 17.", "4x^3-2x^2+143"),
        ("Find the tangent line to g(x) = 16/x – 4(x)^1/2 at x = 4.", "y=-2x+4")
    ]
    
    #INTRO
    INTRO_MSG = r"""
    You wake up in an empty room of what seems to be a dungeon with a note that says:

    'Hello, this is Professor Gyllinsky. Welcome to the ACTUAL final project for our class.
    Remember when you told me that you didn't need math to be a good developer?
    If you want to escape this monster-filled dungeon, YOU will need your math skills. Good luck!'

    As confused as you are that a software engineering professor would go through these lengths
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
    Brian Morillo
    Brian Sanchez
    Jonathan Kong-Shi
    Nehe Lorico
    """
    
    def death_message():
        return "That was wrong. You are NOT as smart as you thought you were. And for that, you will pay the price. You have been smited. Would you like to try again? Enter Y to restart or anything else to quit: "

    def win_message():
        return "You have successfully defeated Professor Gyllinsky, keep in mind your job is not over. Now you have gained the ire of the neighboring professors. You\'ll need to keep one eye open when sleeping."

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

    BOSS_NAME = "Professor Gyllinsky"   
    BOSS_ART = r"""
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%///%%%%%%%%%%%%%%%%%%%%%%%######
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#///%%%%%%%%%%%%%%%%%%%%%%#######
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#///%%%%%%%%%%%%%%%%%%%%#########
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#/,,,,,,,,,,***,,,**(%%%%%%%%%%%%%%%%##########
&&&&&&&&&&&&&&&&&&&&&&&&&&&&%/,,...,,,,,,.,,,,,,,,,,,,,,/#%%%%%%%%%%%%##########
&&&&&&&&&&&&&&&&&&&&&&&&&%*,.........,,,.,,,...,,,... ...,/#%%%%%%%%%%##########
&&&&&&%&&&&&&&&&&%&%&%%(*,............ .........,,,........,(%#%%%%%%###########
&%#%%&%%#%&&%%%%%%#%%(*,....        ........,,,,,,,,........./(##%%%############
&(###(#(%(####&#(##/,,,,...... ...... ......,,,......... .....*##%##%###########
&%####%&&&#%#%%###(,...,... .........................   .......*###%############
&%&%&%%&&%&%%%%%&%*........,,*****,....  ................   ...,################
%&&&&&&&&&&&&&&&%*....   .,/(//((/,,.........   .,***//*........*##############(
%%%%%%&%%%%&%%%%#,..    .*/((((###%%&&&%&&%%%%%%########(*.     *#############((
%%#%%#%%###%%&###,.    .*/(##%%##((##%%########(((/((####(*.   .*##############(
#((#((((#((%%#(%%*.....*/(((**////*****//(//****/(((((/(##(*...,(##############(
###%##%%%%%%%%%#((*..***./(///*******,*,(#(***,,,..,,**/((**,.,*,,#############(
&%%%%%&%%&%%%%%/,**,.,/(//*****/////**,/&@&#,***//////(####(/../*/#############(
&%%%%%%%%%%%%%%#*/*..*((###%%##(((((((##%@&%%#((((#%%%&&%##((*,,//#############(
%%%%%%%%%%%%%%%%(/*,,*((###%%%%&&&%(/(##%%&%%#((%%%%###%%##((/,*((############((
%%%%%%%%%%%%%%%%#/*,.*/((###(##((/*/#%%%%&&%%%%%**//(((((#((/*,*##############((
%%%%%%%%%%%%%%%%%#/,..*////////*,***,,,,****,,,*/**,,**///(/*,.*(#############((
%%%%%%%%%%%%%%%%%%#/..,*//***,..,,*,,,..,,,,..,,,*,...,*///*,.,(##############((
%%#################(,..,***/*,..  ...,,,,,,,,,,,. .,..*/**,,../###############((
####################/...,,**//****,,*//(#(#(//**////**/*,....,################((
%%%%%%%%%%%%%%%%%%%%#*. ..,**/*******//////////*///****,..  ,(################((
%%%%%%%%%%%%%%%%%%%%%#,   .,,***//****,,****,,***//**,..   ,(#################((
#%########%((##(###(*,.     ....,*///********////*,..        ,(###############((
#%%%%%%%%%%%%#(,.       ..      ....**/***////*,....             .,/##########((
%%%%%%%%%%%%(*,.       .**,.      ..  ...........     .,*.      ..  ,/#########(
#########((***,,...   .///**,..   .          ....    ,*////*.   .,,,.,*(######((
 **/**/****,,,,,..    .*///****,..             ...,**//((((((/..,,,**,*/########
    """      
    BOSS_ACTION = "Laughing at your despair"   
     
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



