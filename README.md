# Attendance-System
This is a simple and basic  project to take  the attendence using face recognition.


Documentation

Getting Started:
1.Overview
2.Libraries
3.Working
Overview:
Our project used computer vison to detect, identify and register the respective attendee. 
Libraries:
	*dlib (for face recognition)
	*Tkinker (for front-end and UI)
	*OpenCV (for using the web cam)
	*NumPy (for editing the image)
	*OS (to convert. Move, and change file type of the file)
	*Pillow (to import images for Tkinker)
	*time (to get system time)
	*Datetime (to get current system date)




Working:
It just takes an image assigned by the user and moves the file to the folder (ImageAttendence). And when the user calls to take the attendance. Frist the program recognizes the faces of the attendees and the user can press space and stop the cam. The program saves it in the file required and the user can later get the attendance on a certain day by entering the date and later can retrieve the attendance from the files.

