# 1. Import the files
import  unittest
from tests.test_login import loginTest
from tests.test_contactUsForm import ContactForm


# 2. Create the object of the class using unitTest
cf = unittest.TestLoader().loadTestsFromTestCase(ContactForm)
lt = unittest.TestLoader().loadTestsFromTestCase(loginTest)

# 3. Create TestSuite
regressionTest = unittest.TestSuite([cf,lt])

# 4. Call the Test Runner method
unittest.TextTestRunner(verbosity=1).run(regressionTest)

