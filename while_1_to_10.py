#!/usr/bin/env Python3
from os import system


system("clear")

#DATA

start_n = int( input( "Enter start number:\n" )) 
end_n   = int( input( "Enter end number:\n" ))



#LOGIC

if ( start_n < end_n ):
 while ( start_n <= end_n ):
  print( start_n )
  start_n += 1

elif( start_n > end_n ):
 while ( end_n <= start_n ):
  print( start_n )
  start_n -= 1

elif( start_n == end_n ):
 print("Error. You entered the same numbers.\n")
