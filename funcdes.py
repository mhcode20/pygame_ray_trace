import math

def get_distance_to_object(position, direction):
    # Set the distance to the nearest object to a large value
    distance = float('inf')

    # Set the step size for the collision detection algorithm
    step_size = 0.1

    # Set the current position to the starting position
    current_position = list(position)

    # Set the flag that indicates if the object has been found to False
    object_found = False

    # Iterate until an object is found or the maximum distance is reached
    while not object_found and distance > 0:
        # Check if the current position is within the bounds of the environment
        if current_position[0] < 0 or current_position[0] >= environment_width or current_position[1] < 0 or current_position[1] >= environment_height:
            # If the current position is out of bounds, set the distance to 0
            distance = 0
            object_found = True
        else:
            # If the current position is within the bounds of the environment, check if there is an object at that position
            if is_object_at_position(current_position):
                # If there is an object at the current position, set the distance to the distance traveled so far
                distance = math.sqrt((current_position[0] - position[0]) ** 2 + (current_position[1] - position[1]) ** 2)
                object_found = True
            else:
                # If there is no object at the current position, update the position and continue searching
                current_position[0] += direction[0] * step_size
                current_position[1] += direction[1] * step_size
    
    # Return the distance to the nearest object
    return distance

def is_object_at_position(position):
    # This function should return True if there is an object at the given position, and False if there is not.
    # You can use any method you choose to determine if there is an object at the position, such as by checking against a list of known objects,
    # by using a collision detection algorithm, or by generating the environment procedurally.
    pass
