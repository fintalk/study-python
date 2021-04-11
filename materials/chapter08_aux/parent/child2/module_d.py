import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../child'))
#print(sys.path)
import module_c

module_c.i_am_c()

