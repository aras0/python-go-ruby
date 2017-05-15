from __future__ import unicode_literals

from rpn_project import router, static, main

application = router.Router()

application.add_exact('/', main.in_run)
application.add_prefix('/static/', static.static_app)
application.add_prefix('/out', main.out_run)
