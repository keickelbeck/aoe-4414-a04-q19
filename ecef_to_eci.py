# ecef_to_eci.py
#
# Usage: python3 ecef_to_eci.py year month day hour minute second ecef_x_km ecef_y_km ecef_z_km
#  Converts the ECEF vector to the ECI vector

# Parameters:
#  year: year
#  month: month
#  day: day
#  hour: hour
#  minute: minute
#  second: second
#  ecef_x_km: x-component of ECEF vector in km
#  ecef_y_km: y-component of ECEF vector in km
#  ecef_z_km: z-component of ECEF vector in km

# Output:
#  Prints the ECI x-component (km), ECI y-component (km), and ECI z-component (km)
#
# Written by Kristin Eickelbeck
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
import math # math module
import sys # argv

# "constants"
w = 7.292115*(10**-5)

# initialize script arguments
year = float('nan') #year
month = float('nan') #month
day = float('nan') #day
hour = float('nan') #hour
minute = float('nan') #minute
second = float('nan') #second
ecef_x_km = float('nan') #x-component of ECEF vector in km
ecef_y_km = float('nan') #y-component of ECEF vector in km
ecef_z_km = float('nan') #z-component of ECEF vector in km

# parse script arguments

if len(sys.argv)==10:
  year = float(sys.argv[1])
  month = float(sys.argv[2])
  day = float(sys.argv[3])
  hour = float(sys.argv[4])
  minute = float(sys.argv[5])
  second = float(sys.argv[6])
  ecef_x_km = float(sys.argv[7])
  ecef_y_km = float(sys.argv[8])
  ecef_z_km = float(sys.argv[9])
else:
   print(\
    'Usage: '\
    'python3 ecef_to_eci.py year month day hour minute second ecef_x_km ecef_y_km ecef_z_km'\
   )
   exit()

# write script below this line

#Calculate fractional Julian date
JD = day - 32075 + (1461*(year+4800+ (month-14)//12)//4) + (367*(month - 2 - (month-14)//12 *12)//12)+ -3*((year+4900+(month-14)//12)/100)//4
JD_midnight = JD - 0.5
D_fractional = (second + 60 *(minute+60*hour))/86400
jd_frac = (JD_midnight + D_fractional)

#calculate GMST angle
T_UT1 = (jd_frac - 2451545.0)/36525
GMST_sec = 67310.54841 + (876600*60*60 + 8640184.812866)*T_UT1 + 0.093104*T_UT1**2 + -6.2*10**-6*T_UT1**3
GMST_rad = math.fmod(GMST_sec,86400)*w
GMST_rad = float("{:.6f}".format(GMST_rad))

eci_x_km = ecef_x_km*math.cos(GMST_rad) - ecef_y_km*math.sin(GMST_rad)
eci_y_km = ecef_x_km*math.sin(GMST_rad) + ecef_y_km*math.cos(GMST_rad)
eci_z_km = ecef_z_km

print(eci_x_km)
print(eci_y_km)
print(eci_z_km)

