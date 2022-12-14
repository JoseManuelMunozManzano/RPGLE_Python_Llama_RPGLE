# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Script : callRpgEx1.py
# Author: Mike Larsen
# Date written: 03/21/20
# Purpose: Use itoolkit to call an Rpg program.  Pass first name to the 
#          Rpg program and it passes back a last name. This demonstrates
#          how to pass a parameter to Rpg and receive one back.  It will 
#          also show how to parse the Json response from calling the
#          Rpg program.
#
# ====================================================================*
# Date      Programmer  Description                                   *
#---------------------------------------------------------------------*
# 03/21/20  M.Larsen    Original code.                                *
#                                                                     *
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  * 

from itoolkit import *
from itoolkit.transport import DirectTransport

# assign modules to a local name

itransport = DirectTransport()
itool = iToolKit()

itool.add(iCmd('addlible', 'addlible mllib'))

itool.add( 
          iPgm('my_results','Mlr100Tk')
          .addParm(iData('InFirstName','10a','Mike'))
          .addParm(iData('OutLastName','10a',' ')) 
         )
         
itool.call(itransport)

# results are returned as a dictionary formatted as Json

mypgm_results = itool.dict_out('my_results')

# print the entire contents of the results dictionary.
# the Json returned from a successful call will look like this:
#
# {
#   "InFirstName": "Mike",
#   "OutLastName": "Larsen",
#   "success": "+++ success  Mlr100Tk"
# }

print(mypgm_results)

if 'success' in mypgm_results:
    print('Success!')
else:
    print('Errors occurred.')
    
# parse the Json response from the dictionary

print('\n')
print("Parameter passed TO Rpg: ", mypgm_results['InFirstName'])
print("Parameter passed FROM Rpg: ", mypgm_results['OutLastName'])
print("Status of the program call: ", mypgm_results['success'])
