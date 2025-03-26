import bpy
import functools

#stats:
#max speed: 54 m/s or about .018518/iteration. False. .9m per iteration :/. 
#frame rate: 60f/s or about .016666 iterations per second.

# if we change the base iteration to 1m per second, will my laptop explode?
# It ran Bioshock infinite on Ultra @ around 30 frames so it should be okay
#It would be pointless cuz why would we iterate above the machine's refresh rate?
#Need to see if we can get blender find the refresh rate and make that the locked_frames variable 

actual_velocity = 9.8000000

locked_frames = 60.000000
max_speed = 54.000000/locked_frames
velocity = actual_velocity/locked_frames
frames = 1.000000/locked_frames
speed = 0

def delete():
    bpy.ops.object.delete(use_global=False, confirm=False)
      
def select(item):
            D.objects[item].select_set(True)
   
def create(item):
    item = item.lower()
    match item:
        case "cube":
            bpy.ops.mesh.primitive_cube_add(size = 2, enter_editmode = False, align = 'WORLD', location = (0, 0, 0), scale = (1, 1, 1))
        case "plane":
            bpy.ops.mesh.primitive_plane_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        case "sphere":
            bpy.ops.mesh.primitive_uv_sphere_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        case "cylinder":
            bpy.ops.mesh.primitive_cylinder_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        case "cone":
            bpy.ops.mesh.primitive_cone_add(enter_editmode=FALSE, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        case "torus":
            bpy.ops.mesh.primitive_torus_add(align='WORLD', location=(0, 0, 0), rotation=(0, 0, 0))
        case "earth":
            bpy.ops.mesh.primitive_uv_sphere_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1274.2, 1274.2, 1274.2))

        case default:
            bpy.ops.mesh.primitive_monkey_add(size =2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))

def move(direction):
    direction = direction.lower()
    match direction:
        case 'up':
            bpy.ops.transform.translate(value=(0, 0, 1), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
        case 'down':
            bpy.ops.transform.translate(value=(0, 0, -1), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
        case 'right':
            bpy.ops.transform.translate(value=(0, 1, 0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
        case 'left':
            bpy.ops.transform.translate(value=(0, -1, 0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
        case 'foreward':
            bpy.ops.transform.translate(value=(1, 0, 0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
        case 'back':
            bpy.ops.transform.translate(value=(-1, 0, 0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
        case 'up':
            bpy.ops.transform.translate(value=(0, 0, 1), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
        case default:
            bpy.ops.transform.translate(value=(0, 0, 0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)

def move_x(speed):
    #six decimal places btw
    bpy.ops.transform.translate(value=(speed, 0.000000, 0.000000), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)

def move_neg_x(speed):
    speed = speed * -1
    bpy.ops.transform.translate(value=(speed, 0.000000, 0.000000), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)

def move_y(speed):
    #six decimal places btw
    bpy.ops.transform.translate(value=(0.000000, speed, 0.000000), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)

def move_neg_y(speed):
    speed = speed * -1
    bpy.ops.transform.translate(value=(0, speed, 0.000000), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)

def move_z(speed):
    #six decimal places btw
    bpy.ops.transform.translate(value=(0.000000, 0.000000, speed), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)

def move_neg_z(speed):
    speed = speed * -1
    bpy.ops.transform.translate(value=(0.000000, 0.000000, speed), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)

def delete():
    bpy.ops.object.delete(use_global=False, confirm=False)
      
def select(item):
            bpy.data.objects[item].select_set(True)
   
def create(item):
    item = item.lower()
    match item:
        case "cube":
            bpy.ops.mesh.primitive_cube_add(size = 2, enter_editmode = False, align = 'WORLD', location = (0, 0, 0), scale = (1, 1, 1))
        case "plane":
            bpy.ops.mesh.primitive_plane_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        case "sphere":
            bpy.ops.mesh.primitive_uv_sphere_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        case "cylinder":
            bpy.ops.mesh.primitive_cylinder_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        case "cone":
            bpy.ops.mesh.primitive_cone_add(enter_editmode=FALSE, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        case "torus":
            bpy.ops.mesh.primitive_torus_add(align='WORLD', location=(0, 0, 0), rotation=(0, 0, 0))
        case "earth":
            bpy.ops.mesh.primitive_uv_sphere_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1274.2, 1274.2, 1274.2))
        case default:
            bpy.ops.mesh.primitive_monkey_add(size =2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))

def move(direction):
    direction = direction.lower()
    match direction:
        case 'up':
            bpy.ops.transform.translate(value=(0, 0, 1), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
        case 'down':
            bpy.ops.transform.translate(value=(0, 0, -1), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
        case 'right':
            bpy.ops.transform.translate(value=(0, 1, 0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
        case 'left':
            bpy.ops.transform.translate(value=(0, -1, 0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
        case 'foreward':
            bpy.ops.transform.translate(value=(1, 0, 0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
        case 'back':
            bpy.ops.transform.translate(value=(-1, 0, 0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
        case 'up':
            bpy.ops.transform.translate(value=(0, 0, 1), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
        case default:
            bpy.ops.transform.translate(value=(0, 0, 0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)

def move_x(speed):
    #six decimal places btw
    bpy.ops.transform.translate(value=(speed, 0.000000, 0.000000), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)

def move_neg_x(speed):
    speed = speed * -1
    bpy.ops.transform.translate(value=(speed, 0.000000, 0.000000), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)

def move_y(speed):
    #six decimal places btw
    bpy.ops.transform.translate(value=(0.000000, speed, 0.000000), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)

def move_neg_y(speed):
    speed = speed * -1
    bpy.ops.transform.translate(value=(0, speed, 0.000000), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)

def move_z(speed):
    #six decimal places btw
    bpy.ops.transform.translate(value=(0.000000, 0.000000, speed), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)

def move_neg_z(speed):
    speed = speed * -1
    bpy.ops.transform.translate(value=(0.000000, 0.000000, speed), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)

def distance(item, dir):
    match dir:
         case 'x':
             return bpy.data.objects[item].location[0]
         case 'y':
             return bpy.data.objects[item].location[1]
         case 'z':
             return bpy.data.objects[item].location[2]
         case default:
             return bpy.data.objects[item].location

def grav_x(item, speed):
    if bpy.data.objects[item].location[0] > 0:
        move_neg_x(speed)

def grav_neg_x(item, speed):
    if bpy.data.objects[item].location[0] < 0:
        speed = speed * -1
        move_x(speed)

def grav_y(item, speed):
    if bpy.data.objects[item].location[1] > 0:
        move_neg_y(speed)

def grav_neg_y(item, speed):
    if bpy.data.objects[item].location[1] < 0:
        speed = speed * -1
        move_y(speed)
        
def grav_z(item, speed):
    if bpy.data.objects[item].location[2] > 0:
        move_neg_z(speed)

def grav_neg_z(item, speed):
    if bpy.data.objects[item].location[2] < 0:
        speed = speed * -1
        move_z(speed)

def find_distance(x, y, z):
    count = 0
    distance = 0
    parameters = [x, y, z]
    for input in parameters:
        if input > 0:
            distance = distance + input
            count += 1
        elif input < 0:
            temp = 0
            temp = input * -1
            distance = distance + temp
            count += 1
    return distance

def find_ratio(x, y, z):
    distance = find_distance(x, y, z)
    parameters = [x, y, z]
    new_parameters = []
    for input in parameters:
        ratio = 0
        if input > 0:
            ratio = input/distance[count]
            new_parameters.append(ratio)
        elif input < 0:
            input = input * -1
            ratio = input/distance[count]
            new_list.append(ratio)
    return ratio_parameters

def find_speed(max, vel):
    global speed
    vel = vel/60.000000
    if speed < max:
        speed = speed + vel
        return speed
    else:
        return speed
    
def angry(x, y, z):
    if x <= 1 and x >= -1:
        if x > .0000001:
            x -= 1
        elif x < 0:
            x  += .0000001
    if y <= 1 and y >= -1:
        if y > .0000001:
            y -= 1
        elif y < 0:
            y  += .0000001
    if z <= 1 and z >= -1:
        if z > .0000001:
            z -= 1
        elif z < 0:
            z  += .0000001
        

def gravity(item):
    global max_speed
    global max_pull
    global velocity
    global frames
    speed = 0
    x = round(bpy.data.objects[item].location[0])
    y = round(bpy.data.objects[item].location[1])
    z = round(bpy.data.objects[item].location[2])
    global find_distance
    total_distance = find_distance(x, y, z)
    speed = find_speed(max_speed, velocity)
    x_ratio = x/total_distance
    y_ratio = y/total_distance
    z_ratio = z/total_distance
    x_speed = x_ratio*speed
    y_speed = y_ratio*speed
    z_speed = z_ratio*speed
    grav_x(item, x_speed)
    grav_neg_x(item, x_speed)
    grav_y(item, y_speed)
    grav_neg_y(item, y_speed)
    grav_z(item, z_speed)
    grav_neg_z(item, z_speed)
    angry(x, y, z)
    return frames

#gravity('Cube')

bpy.app.timers.register(functools.partial(gravity, 'Cube'))

#Need to fix a few things.
#1: it takes longer than normal (by almost a factor of 2) for objects to reach 0
# the way things are working now.