
# a simple [comp] consists of: [A] [type comparison] [B]
# if ([comp] ([AND/OR] [comp])*) {
#   [target if true]
# }
# else {
#   [target if false]
# }

from string import Template

# import the constants trings from the asm files
from utils.asm_constants import comparisons, if_options

# the class will recive an array of comparisons [comp] ORDERED from outside to inside
# the class will recive an array of [AND/OR] or rather [||/&&]

class ASM_COMPLEX_IF():
    comp_list = []
    and_or_list = []
    formed_code = ''