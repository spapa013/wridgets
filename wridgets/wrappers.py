from ipywidgets import widgets, HBox, VBox, Label, Layout
from IPython.display import HTML, display, clear_output
import traceback

def _action_wrapper(action=None, output=None, overwrite_output=True, print_processing=True):
    if not action:
        return
    
    feedback_out = widgets.Output()
    if print_processing:
        display(feedback_out)
        with feedback_out:
            print('Processing...')
    
    if output:
        with output:
            if overwrite_output:
                clear_output()
            try:
                action()
                feedback_out.clear_output()
            except:
                traceback.print_exc()
                feedback_out.clear_output()
    else:
        try:
            action()
            feedback_out.clear_output()
            
        except:
            traceback.print_exc()
            feedback_out.clear_output()


class Button:
    def __init__(self, on_click=None, output=None, overwrite_output=True, run=True, print_processing=True, *args, **kwargs):
        self.on_click = on_click
        self.output = output
        self.overwrite_output = overwrite_output
        self.print_processing = print_processing
        self.button = widgets.Button(*args, **kwargs)
        if run:
            self.run()
    
    def _on_button_click(self, b):
        _action_wrapper(self.on_click, self.output, self.overwrite_output, self.print_processing)

    def run(self):
        self.button.on_click(self._on_button_click)


class Checkbox:
    def __init__(self, on_check=None, on_uncheck=None, on_check_output=None, on_uncheck_output=None, on_check_overwrite_output=True,on_uncheck_overwrite_output=True,\
                 layout={'width':'max-content'}, indent=False, run=True, print_processing=True, *args, **kwargs):
        self.on_check = on_check
        self.on_check_output = on_check_output
        self.on_check_overwrite_output = on_check_overwrite_output
        self.on_uncheck = on_uncheck
        self.on_uncheck_output = on_uncheck_output
        self.on_uncheck_overwrite_output = on_uncheck_overwrite_output
        self.print_processing = print_processing
        self.checkbox = widgets.Checkbox(layout=layout, indent=indent, *args, **kwargs)
        if run:
            self.run()

    def _on_change(self, change):        
        if self.checkbox.value:
            _action_wrapper(self.on_check, self.on_check_output, self.on_check_overwrite_output, self.print_processing)
            
        if not self.checkbox.value:
            _action_wrapper(self.on_uncheck, self.on_uncheck_output, self.on_uncheck_overwrite_output, self.print_processing)
            
    def run(self):
        self.checkbox.observe(self._on_change, names='value')