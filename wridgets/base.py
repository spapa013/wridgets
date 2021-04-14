from IPython.display import display, clear_output
import traceback

def default_feedback_action():
    print('Processing...')

def _action_wrapper(action=None, output=None, overwrite_previous_output=True, feedback=False, feedback_action=default_feedback_action, action_kws={}):
    if action is None:
        return
    
    if output is not None:
        with output:
            if overwrite_previous_output:
                clear_output()
            if feedback:
                feedback_action()
                clear_output(wait=True)
            try:
                action(**action_kws)
            except:
                traceback.print_exc()
    else:
        if feedback:
            feedback_action()
            clear_output(wait=True)
        try:
            action(**action_kws)    
        except:
            traceback.print_exc()


class Base:
    def __init__(self, on_interact=None, output=None, overwrite_previous_output=True, feedback=False, action_kws={}):
        self.on_interact = on_interact
        self.output = output
        self.overwrite_previous_output = overwrite_previous_output
        self.feedback = feedback
        self.action_kws = action_kws
        self.action_disabled = False
        self.widget = None
        

    def display(self):
        display(self.widget)
        if self.output is not None:
            display(self.output)


    def enable_action(self):
        self.action_disabled = False


    def disable_action(self):
        self.action_disabled = True


    def update_value(self, value, action=True):
        if action:
            self.widget.value = value 
        
        else:
            self.disable_action()
            self.widget.value = value
            self.enable_action()


    def _action_on_interact(self, b):
        if not self.action_disabled:
            _action_wrapper(action=self.on_interact, output=self.output, overwrite_previous_output=self.overwrite_previous_output, feedback=self.feedback, action_kws=self.action_kws)


class BooleanBase:
    def __init__(self, on_true=None, on_false=None, on_true_output=None, on_false_output=None, on_true_overwrite_previous_output=True, on_false_overwrite_previous_output=True, on_true_feedback=False, on_false_feedback=False, on_true_action_kws={}, on_false_action_kws={}):
        self.on_true = on_true
        self.on_false = on_false
        
        self.on_true_output = on_true_output
        self.on_false_output = on_false_output

        self.on_true_overwrite_previous_output = on_true_overwrite_previous_output
        self.on_false_overwrite_previous_output = on_false_overwrite_previous_output
        
        self.on_true_feedback = on_true_feedback
        self.on_false_feedback = on_false_feedback

        self.on_true_action_kws = on_true_action_kws
        self.on_false_action_kws = on_false_action_kws

        self.on_true_action_disabled = False
        self.on_false_action_disabled = False
                
        self.widget = None
    

    def display(self):
        display(self.widget)
        if self.on_true_output is not None:
            display(self.on_true_output)
        if self.on_false_output is not None:
            display(self.on_false_output)


    def enable_on_true_action(self):
        self.on_true_action_disabled = False


    def disable_on_true_action(self):
        self.on_true_action_disabled = True


    def enable_on_false_action(self):
        self.on_false_action_disabled = False


    def disable_on_false_action(self):
        self.on_false_action_disabled = True

    
    def update_value(self, value, action=True):
        if action:
            self.widget.value = value 
        
        else:
            self.disable_on_true_action()
            self.disable_on_false_action()
            self.widget.value = value
            self.enable_on_true_action()
            self.enable_on_false_action()


    def _action_on_interact(self, change):        
        if self.widget.value:
            if not self.on_true_action_disabled:
                _action_wrapper(action=self.on_true, output=self.on_true_output, overwrite_previous_output=self.on_true_overwrite_previous_output, feedback=self.on_true_feedback, action_kws=self.on_true_action_kws)

        if not self.widget.value:
            if not self.on_false_action_disabled:
                _action_wrapper(action=self.on_false, output=self.on_false_output, overwrite_previous_output=self.on_false_overwrite_previous_output, feedback=self.on_false_feedback, action_kws=self.on_false_action_kws)
