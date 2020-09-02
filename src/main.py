import settings

import mouse

settings.init()

mouse_id = None

while mouse_id != 0:
    mouse_id = mouse.create()

mouse.index()