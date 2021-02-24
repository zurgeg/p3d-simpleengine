import sys
class PluginTest:
    def __init__(self, app):
        self.app = app
        self.app.taskMgr.add(self.test, 'test')
    def test(self, task):
        print('Hi!')
        return task.cont
class RPPlugin:
    def __init__(self, app):
        self.app = app
        sys.path.insert(0, "./")
        sys.path.insert(0, "./RenderPipeline")
        from rpcore import RenderPipeline

        self.render_pipeline = RenderPipeline()
        self.render_pipeline.create(app)
        from rpcore.util.movement_controller import MovementController
        self.controller = MovementController(app)
        self.controller.setup()
def on_init(app):
    pass
def pre_load(app):
    rp_plugin = RPPlugin(app)
    return False # Don't init showbase

