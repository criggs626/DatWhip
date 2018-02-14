import rospy as rp
from ackermann_msgs.msg import AckermannDriveStamped, AckermannDrive

def driveTest():	
	rp.init_node("pleaseWork",anonymous = False)
	pub=rp.Publisher("/vesc/ackermann_cmd_mux/input/navigation",AckermannDriveStamped,queue_size=10)
	rate=rp.Rate(60)
	drive_msg_stamped = AckermannDriveStamped()
	drive_msg = AckermannDrive()
       	drive_msg.speed = 2.0
        drive_msg.steering_angle = 0.2
        drive_msg.acceleration = 0
        drive_msg.jerk = 0
        drive_msg.steering_angle_velocity = 0
	drive_msg_stamped.drive = drive_msg
	for i in range(0,400):
		pub.publish(drive_msg_stamped)
		rate.sleep()

if __name__ =="__main__":
	try:
		driveTest()
	except rp.ROSInterruptException:
		pass

