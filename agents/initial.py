import time

from modules.publish import Publish
from modules.reply import Reply

ENERGY = 1000
NAME = "AGENT0"

# def Start():
#     print('Publishing...')
#     try:
#         while True:
#             # Reply(Response)
#             Publish(NAME, {"energy": ENERGY})
#             time.sleep(1)
#     except:
#         Done()

# # TODO: move reply/publish into separate processes
# # def Response(request):
# #     if isinstance(request, object) & isinstance(request.get("energy"), int):
# #         # print(request.get("energy"))
# #         if request.get("energy") < ENERGY:
# #             return {"energy": request.get("energy")}
# #     else:
# #         return {"energy": 0}


# Start()

Publish(NAME, {"energy": ENERGY})