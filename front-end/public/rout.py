import subprocess
from rssi import RSSI_Localizer
import math
import time


# def position3():
#         command = "iwconfig wlan0 | grep -i quality  "
#         str = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)

#         answer, error = str.communicate()
#         signalLevelInDb=int(answer[44:46])

#         exp = ((27.55 - (20 * math.log10(5805)) + abs(signalLevelInDb))/20.0)*7.8
#         if(exp<0):
#             exp*=-1
#         #*******************************
#         time.sleep(0.5)

#         str = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)

#         answer, error = str.communicate()
#         signalLevelInDb=int(answer[44:46])

#         exp1 = ((27.55 - (20 * math.log10(5805)) + abs(signalLevelInDb))/20.0)*7.8
#         if(exp1<0):
#             exp1*=-1
#         #*******************************
#         time.sleep(0.5)
#         str = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)

#         answer, error = str.communicate()
#         signalLevelInDb=int(answer[44:46])

#         exp2 = ((27.55 - (20 * math.log10(5805)) + abs(signalLevelInDb))/20.0)*7.8
#         if(exp2<0):
#             exp2*=-1
#         #*******************************
#         time.sleep(0.5)
#         str = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)

#         answer, error = str.communicate()
#         signalLevelInDb=int(answer[44:46])

#         exp3 = ((27.55 - (20 * math.log10(5805)) + abs(signalLevelInDb))/20.0)*7.8
#         if(exp3<0):
#             exp3*=-1
#         list.add(exp3)
#         #*******************************
#         str = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)

#         answer, error = str.communicate()
#         signalLevelInDb=int(answer[44:46])

#         exp4 = ((27.55 - (20 * math.log10(5805)) + abs(signalLevelInDb))/20.0)*7.8
#         if(exp4<0):
#             exp4*=-1
def position():
        time.sleep(0.5)
        command = "iwconfig wlan0 | grep -i quality  "
        str = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)

        answer, error = str.communicate()
        signalLevelInDb=int(answer[44:46])

        exp = ((27.55 - (20 * math.log10(5805)) + abs(signalLevelInDb))/20.0)*7.8
        if(exp<0):
            exp*=-1
        return(exp)

def averageposition():
        a=position()
        b=position()
        c=position()
        d=position()
        e=position()
        return((a+b+c+d+e)/5)

def position2():
        command = "iwconfig wlan0 | grep -i quality  "
        total = 0
        for x in range(5):
            if (x!=0):
                time.sleep(0.5)
            st = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)

            answer, error = st.communicate()
            signalLevelInDb=int(answer[44:46])

            exp = ((27.55 - (20 * math.log10(5805)) + abs(signalLevelInDb))/20.0)*7.8
            exp = int(exp)
            if(exp<0):
                exp*=-1
            total+=exp
        total/=5
        p = str(total)
        return(p)
        
print(position2())
        



    

