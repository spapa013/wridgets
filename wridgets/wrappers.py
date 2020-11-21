from ipywidgets import widgets, HBox, VBox, Label, Layout
from IPython.display import HTML, display, clear_output
import traceback

def _action_wrapper(action=None, output=None, overwrite_output=True, feedback_output=None):
    if action is None:
        return

    if feedback_output is not None:
        display(feedback_output)
        with feedback_output:
            print('Processing...')
    
    if output is not None:
        with output:
            if overwrite_output:
                clear_output()
            try:
                action()
                del feedback_output
            except:
                traceback.print_exc()
                del feedback_output
    else:
        try:
            action()
            del feedback_output
            
        except:
            traceback.print_exc()
            del feedback_output


class Button:
    def __init__(self, on_click=None, output=None, overwrite_output=True, run=True, feedback=True, *args, **kwargs):
        self.on_click = on_click
        self.output = output
        self.overwrite_output = overwrite_output
        self.feedback_output = widgets.Output() if feedback else None
        self.button = widgets.Button(*args, **kwargs)
        if run:
            self.run()
    
    def _on_button_click(self, b):
        _action_wrapper(self.on_click, self.output, self.overwrite_output, self.feedback_output)

    def display(self):
        display(self.button)
        if self.output is not None:
            display(self.output)

    def run(self):
        self.button.on_click(self._on_button_click)


class Checkbox:
    def __init__(self, on_check=None, on_uncheck=None, on_check_output=None, on_uncheck_output=None, on_check_overwrite_output=True,on_uncheck_overwrite_output=True,\
                 layout={'width':'max-content'}, indent=False, run=True, feedback=True, *args, **kwargs):
        self.on_check = on_check
        self.on_check_output = on_check_output
        self.on_check_overwrite_output = on_check_overwrite_output
        self.on_uncheck = on_uncheck
        self.on_uncheck_output = on_uncheck_output
        self.on_uncheck_overwrite_output = on_uncheck_overwrite_output
        self.feedback_output = widgets.Output() if feedback else None
        self.checkbox = widgets.Checkbox(layout=layout, indent=indent, *args, **kwargs)
        if run:
            self.run()

    def _on_change(self, change):        
        if self.checkbox.value:
            _action_wrapper(self.on_check, self.on_check_output, self.on_check_overwrite_output, self.feedback_output)
            
        if not self.checkbox.value:
            _action_wrapper(self.on_uncheck, self.on_uncheck_output, self.on_uncheck_overwrite_output, self.feedback_output)
    
    def display(self):
        display(self.checkbox)
        if self.output is not None:
            display(self.output)

    def run(self):
        self.checkbox.observe(self._on_change, names='value')