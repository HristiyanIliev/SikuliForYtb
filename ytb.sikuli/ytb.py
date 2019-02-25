import os, time

picsFolder = os.environ['PIC']

def open_start_menu():
	# test function
    click(picsFolder + 'startMenu.png')

class YoutubeUnpauser:
	__timesUnpaused = 0
	''' TODO: Functionality to progressively reduce the time threshold for new look ups
		for example storing the exact time of the last successful find & click operation
		and returning a time.sleep(value) for the while loop based on that. For example:
		__sleepThresholdAfterFindFailed = int ( 300 / ( currentTime() - __timeOfLastSuccess ) in seconds )  
	'''
	def __init__(self):
		print "Created a YoutubeUnpauser instance."

	def findContinueButton(self):
		print "Looking for Youtube window message box"
		try:
			# look for the image
			msgBox = find(picsFolder + 'videoPaused_messageBox.png')
			found = msgBox.find(picsFolder + 'videoPaused_OK_button.png')
			click (found)
			self.__timesUnpaused += 1
			print "Times Unpaused: " + str(self.__timesUnpaused)
			return 5 # for the while loop time.sleep()
		except FindFailed as ff_err:
			# video is still playing therefore do nothing
			print ff_err
			return 2 # for the while loop time.sleep()


y = YoutubeUnpauser()

while True:
	time.sleep( y.findContinueButton() )  # the window will show once per minute at most
	continue