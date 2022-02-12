from TC_CheckLogin import UserLogin
from TC_RegisterNewUser import RegisterUser
import unittest

registerTestCase = unittest.TestLoader().loadTestsFromTestCase(RegisterUser)
loginTestCase = unittest.TestLoader().loadTestsFromTestCase(UserLogin)

functionalTestSuite = unittest.TestSuite([registerTestCase, loginTestCase])
unittest.TextTestRunner().run(functionalTestSuite)
