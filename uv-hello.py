from fatuv import Loop
from fatuv import UV_RUN_DEFAULT

# loop = Loop()
loop = Loop.default_loop()

print 'Now quitting.'
loop.run(UV_RUN_DEFAULT)

