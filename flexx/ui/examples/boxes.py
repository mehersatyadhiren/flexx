# doc-export: Boxes
"""
Example that puts box and fix mode HVLayout's side-by-side. You can see how
box mode takes the natural size of content into account, making it
more suited for low-level layout. For higher level layout (e.g. the two
main panels in this example) the fix or split mode is more appropriate.
"""

from flexx import ui, app


class Panel(ui.Label):
    CSS = '.flx-Panel {background: #44aaaa; color: #FFF; padding: 1px;}'


class Boxes(ui.Widget):
    
    def init(self):
        
        with ui.HSplit():
            
            with ui.VBox(flex=1):
                
                ui.Label(text='<b>Box mode</b> (aware of natural size)')
                ui.Label(text='flex: 1, sub-flexes: 0, 0, 0')
                with ui.HBox(flex=1):
                    Panel(text='A', flex=0)
                    Panel(text='B', flex=0)
                    Panel(text='C is a bit longer', flex=0)
                ui.Label(text='flex: 0, sub-flexes: 1, 1, 1')
                with ui.HBox(flex=0):
                    Panel(text='A', flex=1)
                    Panel(text='B', flex=1)
                    Panel(text='C is a bit longer', flex=1)
                ui.Label(text='flex: 1, sub-flexes: 1, 0, 2')
                with ui.HBox(flex=1):
                    Panel(text='A', flex=1)
                    Panel(text='B', flex=0)
                    Panel(text='C is a bit longer', flex=2)
                ui.Label(text='flex: 2, sub-flexes: 1, 2, 3')
                with ui.HBox(flex=2):
                    Panel(text='A', flex=1)
                    Panel(text='B', flex=2)
                    Panel(text='C is a bit longer', flex=3)
            
            with ui.VBox(flex=1):
                
                ui.Label(text='<b>Fix mode</b> (high level layout)')
                ui.Label(text='flex: 1, sub-flexes: 0, 0, 0')
                with ui.HFix(flex=1):
                    Panel(text='A', flex=0)
                    Panel(text='B', flex=0)
                    Panel(text='C is a bit longer', flex=0)
                ui.Label(text='flex: 0 (collapses), sub-flexes: 1, 1, 1')
                with ui.HFix(flex=0):
                    Panel(text='A', flex=1, style='min-height:5px;')
                    Panel(text='B', flex=1)
                    Panel(text='C is a bit longer', flex=1)
                ui.Label(text='flex: 1, sub-flexes: 1, 0, 2')
                with ui.HFix(flex=1):
                    Panel(text='A', flex=1)
                    Panel(text='B', flex=0)
                    Panel(text='C is a bit longer', flex=2)
                ui.Label(text='flex: 2, sub-flexes: 1, 2, 3')
                with ui.HFix(flex=2):
                    Panel(text='A', flex=1)
                    Panel(text='B', flex=2)
                    Panel(text='C is a bit longer', flex=3)


if __name__ == '__main__':
    m = app.launch(Boxes)
    app.run()
