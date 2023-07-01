import time



def unicicle_to_differential(robot, v, w):
    # v = translational velocity (m/s)
    # w = angular velocity (RAD/s)

    R = robot.wheel_radius
    L = robot.base_length

    v_l = ((2.0 * v) - (w * L)) / (2.0 * R)
    v_r = ((2.0 * v) + (w * L)) / (2.0 * R)

    return v_l, v_r


command = [(10, 10), 10]


# desired frequency in Hz
frequency = 10

# compute the time duration between iterations
interval = 1 / frequency
while True:

    start_time = time.perf_counter()

    if command:

        # read unicicle
        v = command[0]
        w = command[1]

        # convert from unicicle to differential drive model
        vl, vr = unicicle_to_differential(v, w)

        robot.update_motors(vl, vr)


    elapsed_time = time.perf_counter() - start_time
    sleep_time = interval - elapsed_time

    #if sleep_time > 0:
    #   time.sleep(sleep_time)
    time.sleep(sleep_time)
