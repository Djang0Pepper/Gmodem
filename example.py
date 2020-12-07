from Smodem import Godem
import time

def main():
	#~fredmodem = GSMModem('COM3')
	modem = Godem('/dev/serial0')

	#print("Echo = " + str(modem.getEcho())) #~fred
	#G_ECHO = modem.getEcho().decode()
	#print("Echo = " + str(G_ECHO))
	print("Echo = " + str(modem.getEcho()))

	G_CSQ = modem.getCSQ()
	print("CSQ = " + str(G_CSQ))

	time.sleep(1)

	modem.setGPSOn()

	while True:
		gps = modem.getGPSData()

		print("GPS Data = " + str(gps))

		time.sleep(60)


if __name__ == '__main__':
	main()