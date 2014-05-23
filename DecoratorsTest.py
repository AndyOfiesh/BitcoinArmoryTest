################################################################################
#
# Copyright (C) 2011-2014, Armory Technologies, Inc.                         
# Distributed under the GNU Affero General Public License (AGPL v3)
# See LICENSE or http://www.gnu.org/licenses/agpl.html
#
################################################################################
#
# Project:    Armory
# Author:     Andy Ofiesh
# Website:    www.bitcoinarmory.com
# Orig Date:  2 January, 2014
#
################################################################################
from test.Tiab import TiabTest
import unittest
from armoryengine.Decorators import EmailOutput


# NOT a real unit test. To verify this test properly
# uncomment the decorator and specify the email arguments
# The email arguments should never be pushed to the repo
# Run the test and check your email
class EmailOutputTest(TiabTest):

   def testEmailOutput(self):
      actualResult = someStringOutputFunction("World!")
      expectedResult = "Hello World!"
      self.assertEqual(actualResult, expectedResult)
      
# @EmailOutput(<Sending Email>, <Sending Email Password>, <List of To Addresses>, <Email Subject>)
def someStringOutputFunction(inputString):
   return "Hello " + inputString

if __name__ == "__main__":
   #import sys;sys.argv = ['', 'Test.testName']
   unittest.main()
