import os
from enum import Enum
from pathlib import Path
import re
import datetime as dtt



end_date = dtt.datetime.now().strftime("%Y-%m-%d")
print(end_date)
# cwd = Path.home()
# print(cwd)
# class Direction(Enum):
#     """
#     Direction of order/trade/position.
#     """
#     LONG = "多"
#     SHORT = "空"
#     NET = "净"

# dr = Direction('多')
# print(dr)
# SETTGING_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "VnTrader", "VT_setting.json")
# print(SETTGING_PATH)