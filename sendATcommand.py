# By Sandro Ormeno
import serial
import time

phone = serial.Serial("/dev/ttyAMA0", 9600, timeout=1)

def sim800_responde(expected_answer, time_out):
    abort = 0
    while True:
        response = phone.readline()
        print  response
        if (expected_answer in response) or (abort >= time_out):
        #if (expected_answer in response) or (delta >= time_out):
            break
        time.sleep(1)
        abort = abort + 1



#import time

# abort_after = 5 * 60
# start = time.time()

# while True:
  # delta = time.time() - start
  # if delta >= abort_after:
    # break



def web():


    phone.write('AT+CFUN=0\r')
    #sim800_responde(expected_answer = "OK")
    sim800_responde("OK", 15)


    phone.write('AT+CFUN=1\r')
    sim800_responde("Call Ready", 45)

    
    phone.write('AT+CSQ\r')
    sim800_responde("OK", 15)


    phone.write('AT+SAPBR=3,1,"APN","internet.movistar.ve"\r')
    sim800_responde("OK",15)

    phone.write('AT+SAPBR=1,1\r')
    sim800_responde("OK",180)


    phone.write('AT+SAPBR=2,1\r')
    sim800_responde("OK", 15)


    phone.write('AT+HTTPINIT\r')
    sim800_responde("OK", 15)

    phone.write('AT+HTTPPARA="CID",1\r')
    sim800_responde("OK", 15)

    phone.write('AT+HTTPPARA="URL","http://sandro.awardspace.info/php/hola.php?Tu_nombre=Renzo"\r')
    sim800_responde("OK", 15)

    phone.write('AT+HTTPACTION=0\r')
    sim800_responde("+HTTPACTION: 0,200,", 180)
    
    phone.write('AT+HTTPREAD\r')
    sim800_responde("OK", 15)

    phone.write('AT+HTTPTERM\r')
    sim800_responde("OK", 15)

    phone.write('AT+SAPBR=0,1\r')
    sim800_responde("OK", 15)
    
    

# import time

# abort_after = 5 * 60
# start = time.time()

# while True:
  # delta = time.time() - start
  # if delta >= abort_after:
    # break



web()
