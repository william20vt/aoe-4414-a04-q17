# ymdhms_to_jd.py
#
# Usage: python3 ymdhms_to_jd.py I J K Hour Minute Second
#  Converts date to fractional julian date using the ACM letters to the edditor fortran equation and other conversions
# Parameters:
#  I:year
#  J=month
#  K=day
#  Hour
#  Minute
#  Second
#  ...
# Output:
#  A fractional julian date
#
# Written by William Sosnowski
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import sys # argv
import math

# "constants"
# e.g., R_E_KM = 6378.137

# helper functions

## function description
# def calc_something(param1, param2):
#   pass

# initialize script arguments
I=float('nan')
J=float('nan')
K=float('nan')
Hour=float('nan')
Minute=float('nan')
Second=float('nan')

# parse script arguments
if len(sys.argv)==7:
  I = float(sys.argv[1])
  J  = float(sys.argv[2])
  K = float(sys.argv[3])
  Hour = float(sys.argv[4])
  Minute = float(sys.argv[5])
  Second = float(sys.argv[6])


else:
  print(\
  'Usage: '\
  'python3 ymdhms_to_jd.py  Year Month Day Hour Minute Seconds'\
  )
  exit()


#converting hour min and sec to portion of the day (k) value

#K=K+(Hour/24)+(Minute/1440)+(Second/86400)
K = K + (Hour/24.0) + (Minute/1440.0) + (Second/86400.0)

if J <= 2:  # Adjust for January and February
    I = I-1
    J = J+12

#JD=K-32075+1461*(I+4800+(J-14)/12)/4+
#     367*(J-2-(J-14)/144)/12-
#     3*((I+4900+(J-14)/12)/100)/4
#off by 0.5 to 1.5
#JD = K - 32075 + math.floor(1461*(I+4800+(J-14)/12)/4)+\
 #    math.floor(367*(J-2-12*((J-14)/12))/12)-\
 #    math.floor(3*((I+4900+(J-14)/12)/100)/4)
 #also off, forgot to account for the fact that fortrane uses integers
JD = (K - 32075 + 
      math.floor(1461*(I+4800 +(J-14)//12)/4)+ 
      math.floor(367*(J-2-12*((J-14)//12))/12)- 
      math.floor(3*((I+4900+(J-14)//12)//100)/4))

jd_frac=JD-2.5


print(jd_frac)
