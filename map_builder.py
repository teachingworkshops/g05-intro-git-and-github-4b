from room_graph_builder import RoomGraphBuilder
from room import Room
from assets import Assets

def build_level():
   """
   Builds a graph out of WIT locations and returns initial node
   """
   # Creates all rooms for the level
   annex_east = Room(Assets.ANNEX_EAST_NAME, Assets.ANNEX_EAST_DESC)
   annex_south = Room(Assets.ANNEX_SOUTH_NAME, Assets.ANNEX_SOUTH_DESC)
   annex_central = Room(Assets.ANNEX_CENTRAL_NAME, Assets.ANNEX_CENTRAL_DESC)
   annex_north = Room(Assets.ANNEX_NORTH_NAME, Assets.ANNEX_NORTH_DESC)
   ira_allen = Room(Assets.IRA_ALLEN_NAME, Assets.IRA_ALLEN_DESC)
   tansey_gym = Room(Assets.TANSEY_GYM_NAME, Assets.TANSEY_GYM_DESC)
   beatty = Room(Assets.BEATTY_NAME, Assets.BEATTY_DESC)
   the_quad = Room(Assets.THE_QUAD_NAME, Assets.THE_QUAD_DESC)
   willson_hall = Room(Assets.WILLSON_HALL_NAME, Assets.WILLSON_HALL_DESC)
   kingsman_hall = Room(Assets.KINGSMAN_HALL_NAME, Assets.KINGSMAN_HALL_DESC)
   rubenstein_hall = Room(Assets.RUBENSTEIN_HALL_NAME, Assets.RUBENSTEIN_HALL_DESC)
   williston_hall = Room(Assets.WILLISTON_HALL_NAME, Assets.WILLISTON_HALL_DESC)
   wentworth_hall = Room(Assets.WENTWORTH_HALL_NAME, Assets.WENTWORTH_HALL_DESC)
   wattson_hall = Room(Assets.WATTSON_HALL_NAME, Assets.WATTSON_HALL_DESC)
   ceis_building = Room(Assets.CEIS_NAME, Assets.CEIS_DESC)

   wentworth_hall.set_exit(True)
   ira_allen.set_has_key(True)

   # Connects all rooms
   RoomGraphBuilder.path([annex_east, annex_south, tansey_gym, beatty, the_quad])
   RoomGraphBuilder.path([annex_south, annex_central, annex_north, ira_allen])
   RoomGraphBuilder.cycle([the_quad, willson_hall, kingsman_hall, rubenstein_hall,
                       williston_hall, wentworth_hall, wattson_hall])
   RoomGraphBuilder.star(the_quad, [willson_hall, kingsman_hall, rubenstein_hall,
                       williston_hall, wentworth_hall, wattson_hall])   
   RoomGraphBuilder.path([the_quad, ceis_building])

   # Returns starting Room
   return annex_east