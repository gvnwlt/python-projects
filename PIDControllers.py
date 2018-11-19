# PID Controller Course


# Control power output (speed/throttle); throttle regulates how much speed/acceleration should be provided
# instead of a human regulating a throttle to achieve and maintain a certain speed, a controller (PID system) monitors the 
# output (speed) and adjusts the throttle where necessary to get to said speed. Too much throttle generates too much speed (overshoot target speed)
# and needs to be regulated, such that the throttle is applied to reach the target speed without overshooting. So throttle is input, and speed is output.  



def greeter():
   print 'Starting PID System'

greeter()

