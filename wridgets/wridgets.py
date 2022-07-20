from functools import wraps
from .base import BooleanBase, StandardBase

standard_widgets = ['Audio'
                    'HTML',
                    'BoundedFloatText',
                    'BoundedIntText',
                    'Button',
                    'ColorPicker',
                    'Combobox',
                    'DatePicker',
                    'Dropdown',
                    'FileUpload',
                    'FloatLogSlider',
                    'FloatProgress',
                    'FloatRangeSlider',
                    'FloatSlider',
                    'FloatText',
                    'HTMLMath',
                    'Image',
                    'IntProgress',
                    'IntRangeSlider',
                    'IntSlider',
                    'IntText',
                    'Password',
                    'Play',
                    'RadioButtons',
                    'Select',
                    'SelectionRangeSlider',
                    'SelectionSlider',
                    'SelectMultiple',
                    'Text',
                    'Textarea',
                    'ToggleButtons']


boolean_widgets = ['ToggleButton', 
                    'Checkbox', 
                    'Valid']


@wraps(StandardBase.__init__, assigned=['__signature__'])
def _standard_base_constructor(self, *args, **kwargs):
    StandardBase.__init__(self, *args, **kwargs)


@wraps(BooleanBase.__init__, assigned=['__signature__'])
def _boolean_base_constructor(self, *args, **kwargs):
    BooleanBase.__init__(self, *args, **kwargs)


def _button_observe(self):
    self.widget.on_click(self._observe)

def _initialize_widgets():
    for widget in standard_widgets:
        if widget == 'Button':
            _attrs = {
            "__init__": _standard_base_constructor,
            "observe": _button_observe
        }
        else:
            _attrs = {
            "__init__": _standard_base_constructor,
        }
        globals()[widget] = type(widget, (StandardBase, ), _attrs)

    for widget in boolean_widgets:
        globals()[widget] = type(widget, (BooleanBase, ), {
            "__init__": _boolean_base_constructor,
        })

_initialize_widgets()