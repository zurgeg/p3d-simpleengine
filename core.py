import json, sys
from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
class App(ShowBase):
    def __init__(self):
        print(f'Performing Pre-Script load tasks')
        import scripts
        do_init_showbase = scripts.pre_load(self)
        if do_init_showbase:
            ShowBase.__init__(self)
        lvl = json.load(open('level.json'))
        print(f'Loading models...')
        for i in lvl['models']:
            file = i['file']
            var = i['name']
            temp = Actor(file)
            temp.reparent_to(render)
            print(f'Loaded model {var} from file {file}')
            setattr(self, var, temp)
        
        print(f'All models loaded!')

        print(f'Loading scripts...')
        scripts.on_init(self)
        print(f'Loaded all scripts!')

        print(f'We are good to go!')
def run():
    App().run()

