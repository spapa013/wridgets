from ipywidgets import widgets
from .base import Base, BooleanBase

class IntSlider(Base):
    def __init__(self, on_interact=None, output=None, map_value=None, overwrite_previous_output=True, feedback=False, run=True, *args, **kwargs):
        super().__init__(on_interact=on_interact, output=output, map_value=map_value, overwrite_previous_output=overwrite_previous_output, feedback=feedback)
        
        self.widget = widgets.IntSlider(*args, **kwargs)
        
        if run:
            self.run()
            
    def run(self):
        self.widget.observe(self._action_on_interact, names='value')

class FloatSlider(Base):
    def __init__(self, on_interact=None, output=None, map_value=None, overwrite_previous_output=True, feedback=False, run=True, *args, **kwargs):
        super().__init__(on_interact=on_interact, output=output, map_value=map_value, overwrite_previous_output=overwrite_previous_output, feedback=feedback)
        
        self.widget = widgets.FloatSlider(*args, **kwargs)
        
        if run:
            self.run()
            
    def run(self):
        self.widget.observe(self._action_on_interact, names='value')

class FloatLogSlider(Base):
    def __init__(self, on_interact=None, output=None, map_value=None, overwrite_previous_output=True, feedback=False, run=True, *args, **kwargs):
        super().__init__(on_interact=on_interact, output=output, map_value=map_value, overwrite_previous_output=overwrite_previous_output, feedback=feedback)
        
        self.widget = widgets.FloatLogSlider(*args, **kwargs)
        
        if run:
            self.run()
            
    def run(self):
        self.widget.observe(self._action_on_interact, names='value')

class IntRangeSlider(Base):
    def __init__(self, on_interact=None, output=None, map_value=None, overwrite_previous_output=True, feedback=False, run=True, *args, **kwargs):
        super().__init__(on_interact=on_interact, output=output, map_value=map_value, overwrite_previous_output=overwrite_previous_output, feedback=feedback)
        
        self.widget = widgets.IntRangeSlider(*args, **kwargs)
        
        if run:
            self.run()
            
    def run(self):
        self.widget.observe(self._action_on_interact, names='value')

class FloatRangeSlider(Base):
    def __init__(self, on_interact=None, output=None, map_value=None, overwrite_previous_output=True, feedback=False, run=True, *args, **kwargs):
        super().__init__(on_interact=on_interact, output=output, map_value=map_value, overwrite_previous_output=overwrite_previous_output, feedback=feedback)
        
        self.widget = widgets.FloatRangeSlider(*args, **kwargs)
        
        if run:
            self.run()
            
    def run(self):
        self.widget.observe(self._action_on_interact, names='value')

class IntProgress(Base):
    def __init__(self, on_interact=None, output=None, map_value=None, overwrite_previous_output=True, feedback=False, run=True, *args, **kwargs):
        super().__init__(on_interact=on_interact, output=output, map_value=map_value, overwrite_previous_output=overwrite_previous_output, feedback=feedback)
        
        self.widget = widgets.IntProgress(*args, **kwargs)
        
        if run:
            self.run()
            
    def run(self):
        self.widget.observe(self._action_on_interact, names='value')

class FloatProgress(Base):
    def __init__(self, on_interact=None, output=None, map_value=None, overwrite_previous_output=True, feedback=False, run=True, *args, **kwargs):
        super().__init__(on_interact=on_interact, output=output, map_value=map_value, overwrite_previous_output=overwrite_previous_output, feedback=feedback)
        
        self.widget = widgets.FloatProgress(*args, **kwargs)
        
        if run:
            self.run()
            
    def run(self):
        self.widget.observe(self._action_on_interact, names='value')

class BoundedIntText(Base):
    def __init__(self, on_interact=None, output=None, map_value=None, overwrite_previous_output=True, feedback=False, run=True, *args, **kwargs):
        super().__init__(on_interact=on_interact, output=output, map_value=map_value, overwrite_previous_output=overwrite_previous_output, feedback=feedback)
        
        self.widget = widgets.BoundedIntText(*args, **kwargs)
        
        if run:
            self.run()
            
    def run(self):
        self.widget.observe(self._action_on_interact, names='value')

class BoundedFloatText(Base):
    def __init__(self, on_interact=None, output=None, map_value=None, overwrite_previous_output=True, feedback=False, run=True, *args, **kwargs):
        super().__init__(on_interact=on_interact, output=output, map_value=map_value, overwrite_previous_output=overwrite_previous_output, feedback=feedback)
        
        self.widget = widgets.BoundedFloatText(*args, **kwargs)
        
        if run:
            self.run()
            
    def run(self):
        self.widget.observe(self._action_on_interact, names='value')

class IntText(Base):
    def __init__(self, on_interact=None, output=None, map_value=None, overwrite_previous_output=True, feedback=False, run=True, *args, **kwargs):
        super().__init__(on_interact=on_interact, output=output, map_value=map_value, overwrite_previous_output=overwrite_previous_output, feedback=feedback)
        
        self.widget = widgets.IntText(*args, **kwargs)
        
        if run:
            self.run()
            
    def run(self):
        self.widget.observe(self._action_on_interact, names='value')

class FloatText(Base):
    def __init__(self, on_interact=None, output=None, map_value=None, overwrite_previous_output=True, feedback=False, run=True, *args, **kwargs):
        super().__init__(on_interact=on_interact, output=output, map_value=map_value, overwrite_previous_output=overwrite_previous_output, feedback=feedback)
        
        self.widget = widgets.FloatText(*args, **kwargs)
        
        if run:
            self.run()
            
    def run(self):
        self.widget.observe(self._action_on_interact, names='value')

class ToggleButton(BooleanBase):
    def __init__(self, on_true=None, on_false=None, on_true_output=None, on_false_output=None, map_value=None, \
                 on_true_overwrite_previous_output=True, on_false_overwrite_previous_output=True, on_true_feedback=False, \
                 on_false_feedback=False, run=True, layout={'width':'max-content'}, indent=False, *args, **kwargs):
        super().__init__(on_true=on_true, on_false=on_false, on_true_output=on_true_output, on_false_output=on_false_output, map_value=map_value, \
                 on_true_overwrite_previous_output=on_true_overwrite_previous_output, on_false_overwrite_previous_output=on_false_overwrite_previous_output, on_true_feedback=on_true_feedback, \
                 on_false_feedback=on_false_feedback)
        
        self.widget = widgets.ToggleButton(layout=layout, indent=indent, *args, **kwargs)
        
        if run:
            self.run()

    def run(self):
        self.widget.observe(self._action_on_interact, names='value')

class Checkbox(BooleanBase):
    def __init__(self, on_true=None, on_false=None, on_true_output=None, on_false_output=None, map_value=None, \
                 on_true_overwrite_previous_output=True, on_false_overwrite_previous_output=True, on_true_feedback=False, \
                 on_false_feedback=False, run=True, layout={'width':'max-content'}, indent=False, *args, **kwargs):
        super().__init__(on_true=on_true, on_false=on_false, on_true_output=on_true_output, on_false_output=on_false_output, map_value=map_value, \
                 on_true_overwrite_previous_output=on_true_overwrite_previous_output, on_false_overwrite_previous_output=on_false_overwrite_previous_output, on_true_feedback=on_true_feedback, \
                 on_false_feedback=on_false_feedback)
        
        self.widget = widgets.Checkbox(layout=layout, indent=indent, *args, **kwargs)
        
        if run:
            self.run()

    def run(self):
        self.widget.observe(self._action_on_interact, names='value')

class Valid(BooleanBase):
    def __init__(self, on_true=None, on_false=None, on_true_output=None, on_false_output=None, map_value=None, \
                 on_true_overwrite_previous_output=True, on_false_overwrite_previous_output=True, on_true_feedback=False, \
                 on_false_feedback=False, run=True, layout={'width':'max-content'}, indent=False, *args, **kwargs):
        super().__init__(on_true=on_true, on_false=on_false, on_true_output=on_true_output, on_false_output=on_false_output, map_value=map_value, \
                 on_true_overwrite_previous_output=on_true_overwrite_previous_output, on_false_overwrite_previous_output=on_false_overwrite_previous_output, on_true_feedback=on_true_feedback, \
                 on_false_feedback=on_false_feedback)
        
        self.widget = widgets.Valid(layout=layout, indent=indent, *args, **kwargs)
        
        if run:
            self.run()

    def run(self):
        self.widget.observe(self._action_on_interact, names='value')

class Dropdown(Base):
    def __init__(self, on_interact=None, output=None, map_value=None, overwrite_previous_output=True, feedback=False, run=True, *args, **kwargs):
        super().__init__(on_interact=on_interact, output=output, map_value=map_value, overwrite_previous_output=overwrite_previous_output, feedback=feedback)
        
        self.widget = widgets.Dropdown(*args, **kwargs)
        
        if run:
            self.run()
            
    def run(self):
        self.widget.observe(self._action_on_interact, names='value')

class RadioButtons(Base):
    def __init__(self, on_interact=None, output=None, map_value=None, overwrite_previous_output=True, feedback=False, run=True, *args, **kwargs):
        super().__init__(on_interact=on_interact, output=output, map_value=map_value, overwrite_previous_output=overwrite_previous_output, feedback=feedback)
        
        self.widget = widgets.RadioButtons(*args, **kwargs)
        
        if run:
            self.run()
            
    def run(self):
        self.widget.observe(self._action_on_interact, names='value')

class Select(Base):
    def __init__(self, on_interact=None, output=None, map_value=None, overwrite_previous_output=True, feedback=False, run=True, *args, **kwargs):
        super().__init__(on_interact=on_interact, output=output, map_value=map_value, overwrite_previous_output=overwrite_previous_output, feedback=feedback)
        
        self.widget = widgets.Select(*args, **kwargs)
        
        if run:
            self.run()
            
    def run(self):
        self.widget.observe(self._action_on_interact, names='value')

class SelectionSlider(Base):
    def __init__(self, on_interact=None, output=None, map_value=None, overwrite_previous_output=True, feedback=False, run=True, *args, **kwargs):
        super().__init__(on_interact=on_interact, output=output, map_value=map_value, overwrite_previous_output=overwrite_previous_output, feedback=feedback)
        
        self.widget = widgets.SelectionSlider(*args, **kwargs)
        
        if run:
            self.run()
            
    def run(self):
        self.widget.observe(self._action_on_interact, names='value')

class SelectionRangeSlider(Base):
    def __init__(self, on_interact=None, output=None, map_value=None, overwrite_previous_output=True, feedback=False, run=True, *args, **kwargs):
        super().__init__(on_interact=on_interact, output=output, map_value=map_value, overwrite_previous_output=overwrite_previous_output, feedback=feedback)
        
        self.widget = widgets.SelectionRangeSlider(*args, **kwargs)
        
        if run:
            self.run()
            
    def run(self):
        self.widget.observe(self._action_on_interact, names='value')

class ToggleButtons(Base):
    def __init__(self, on_interact=None, output=None, map_value=None, overwrite_previous_output=True, feedback=False, run=True, *args, **kwargs):
        super().__init__(on_interact=on_interact, output=output, map_value=map_value, overwrite_previous_output=overwrite_previous_output, feedback=feedback)
        
        self.widget = widgets.ToggleButtons(*args, **kwargs)
        
        if run:
            self.run()
            
    def run(self):
        self.widget.observe(self._action_on_interact, names='value')

class SelectMultiple(Base):
    def __init__(self, on_interact=None, output=None, map_value=None, overwrite_previous_output=True, feedback=False, run=True, *args, **kwargs):
        super().__init__(on_interact=on_interact, output=output, map_value=map_value, overwrite_previous_output=overwrite_previous_output, feedback=feedback)
        
        self.widget = widgets.SelectMultiple(*args, **kwargs)
        
        if run:
            self.run()
            
    def run(self):
        self.widget.observe(self._action_on_interact, names='value')

class Text(Base):
    def __init__(self, on_interact=None, output=None, map_value=None, overwrite_previous_output=True, feedback=False, run=True, *args, **kwargs):
        super().__init__(on_interact=on_interact, output=output, map_value=map_value, overwrite_previous_output=overwrite_previous_output, feedback=feedback)
        
        self.widget = widgets.Text(*args, **kwargs)
        
        if run:
            self.run()
            
    def run(self):
        self.widget.observe(self._action_on_interact, names='value')

class Textarea(Base):
    def __init__(self, on_interact=None, output=None, map_value=None, overwrite_previous_output=True, feedback=False, run=True, *args, **kwargs):
        super().__init__(on_interact=on_interact, output=output, map_value=map_value, overwrite_previous_output=overwrite_previous_output, feedback=feedback)
        
        self.widget = widgets.Textarea(*args, **kwargs)
        
        if run:
            self.run()
            
    def run(self):
        self.widget.observe(self._action_on_interact, names='value')

class Combobox(Base):
    def __init__(self, on_interact=None, output=None, map_value=None, overwrite_previous_output=True, feedback=False, run=True, *args, **kwargs):
        super().__init__(on_interact=on_interact, output=output, map_value=map_value, overwrite_previous_output=overwrite_previous_output, feedback=feedback)
        
        self.widget = widgets.Combobox(*args, **kwargs)
        
        if run:
            self.run()
            
    def run(self):
        self.widget.observe(self._action_on_interact, names='value')

class Password(Base):
    def __init__(self, on_interact=None, output=None, map_value=None, overwrite_previous_output=True, feedback=False, run=True, *args, **kwargs):
        super().__init__(on_interact=on_interact, output=output, map_value=map_value, overwrite_previous_output=overwrite_previous_output, feedback=feedback)
        
        self.widget = widgets.Password(*args, **kwargs)
        
        if run:
            self.run()
            
    def run(self):
        self.widget.observe(self._action_on_interact, names='value')

class Play(Base):
    def __init__(self, on_interact=None, output=None, map_value=None, overwrite_previous_output=True, feedback=False, run=True, *args, **kwargs):
        super().__init__(on_interact=on_interact, output=output, map_value=map_value, overwrite_previous_output=overwrite_previous_output, feedback=feedback)
        
        self.widget = widgets.Play(*args, **kwargs)
        
        if run:
            self.run()
            
    def run(self):
        self.widget.observe(self._action_on_interact, names='value')

class DatePicker(Base):
    def __init__(self, on_interact=None, output=None, map_value=None, overwrite_previous_output=True, feedback=False, run=True, *args, **kwargs):
        super().__init__(on_interact=on_interact, output=output, map_value=map_value, overwrite_previous_output=overwrite_previous_output, feedback=feedback)
        
        self.widget = widgets.DatePicker(*args, **kwargs)
        
        if run:
            self.run()
            
    def run(self):
        self.widget.observe(self._action_on_interact, names='value')

class ColorPicker(Base):
    def __init__(self, on_interact=None, output=None, map_value=None, overwrite_previous_output=True, feedback=False, run=True, *args, **kwargs):
        super().__init__(on_interact=on_interact, output=output, map_value=map_value, overwrite_previous_output=overwrite_previous_output, feedback=feedback)
        
        self.widget = widgets.ColorPicker(*args, **kwargs)
        
        if run:
            self.run()
            
    def run(self):
        self.widget.observe(self._action_on_interact, names='value')

class FileUpload(Base):
    def __init__(self, on_interact=None, output=None, map_value=None, overwrite_previous_output=True, feedback=False, run=True, *args, **kwargs):
        super().__init__(on_interact=on_interact, output=output, map_value=map_value, overwrite_previous_output=overwrite_previous_output, feedback=feedback)
        
        self.widget = widgets.FileUpload(*args, **kwargs)
        
        if run:
            self.run()
            
    def run(self):
        self.widget.observe(self._action_on_interact, names='value')

class Image(Base):
    def __init__(self, on_interact=None, output=None, map_value=None, overwrite_previous_output=True, feedback=False, run=True, *args, **kwargs):
        super().__init__(on_interact=on_interact, output=output, map_value=map_value, overwrite_previous_output=overwrite_previous_output, feedback=feedback)
        
        self.widget = widgets.Image(*args, **kwargs)
        
        if run:
            self.run()
            
    def run(self):
        self.widget.observe(self._action_on_interact, names='value')

class Button(Base):
    def __init__(self, on_interact=None, output=None, overwrite_previous_output=True, feedback=False, run=True, *args, **kwargs):
        super().__init__(on_interact=on_interact, output=output, overwrite_previous_output=overwrite_previous_output, feedback=feedback)
        
        self.widget = widgets.Button(*args, **kwargs)
        
        if run:
            self.run()
            
    def run(self):
        self.widget.on_click(self._action_on_interact)