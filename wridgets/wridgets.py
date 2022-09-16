import traceback
from functools import wraps

from IPython.display import FileLink, clear_output, display
from ipywidgets import VBox, HBox, Label, Layout, Style, Output, widgets, link


class Wridget:
    trait_names = (
        'on_interact',
        'on_interact_kws',
        'on_interact_disabled',
        'output',
        'clear_previous_output',
    )

    def __init__(self, on_interact=None, on_interact_kws=None, on_interact_disabled=None, output=None, clear_previous_output=None, **widget_kws):
        self._config = {}
        self.on_interact = on_interact
        self.on_interact_kws = on_interact_kws if on_interact_kws is not None else {}
        self.on_interact_disabled = on_interact_disabled if on_interact_disabled is not None else False
        self.output = output if output is not None else Output()
        self.clear_previous_output = clear_previous_output if clear_previous_output is not None else True
        self.widget = getattr(
            widgets, self.__class__.__name__)(**widget_kws)
        self.observe()

    def __init_subclass__(cls) -> None:
        for trait in cls.trait_names:
            cls._init_trait(trait)

    @classmethod
    def _init_trait(cls, trait):
        def getter_lda(self): return self._config.get(trait)
        setattr(cls, trait, property(getter_lda))
        def setter_lda(self, value): self._config.update({trait: value})
        setattr(cls, trait, getattr(cls, trait).setter(setter_lda))

    def display(self):
        display(self.widget)
        display(self.output)

    @property
    def config(self):
        self._config.update({k: v for k, v in self.widget.trait_values().items(
        ) if not k.startswith('_') and k not in ['keys', 'comm', 'log']})
        return self._config

    @staticmethod
    def _on_interact_wrapper(on_interact, output, clear_previous_output, on_interact_kws, is_disabled):
        if on_interact is None or is_disabled:
            return

        with output:
            if clear_previous_output:
                clear_output()
            try:
                on_interact(**on_interact_kws)
            except:
                traceback.print_exc()

    def observe(self):
        self.widget.observe(self._observe, names='value')

    def _observe(self, change):
        self._on_interact_wrapper(on_interact=self.on_interact, output=self.output,
                                  clear_previous_output=self.clear_previous_output, on_interact_kws=self.on_interact_kws, is_disabled=self.on_interact_disabled)

    def get(self, name):
        if name in self.trait_names:
            return getattr(self, name)
        elif name in self.widget.trait_names():
            return getattr(self.widget, name)

    def set(self, *args, **kwargs):
        if args:
            for arg in args:
                assert isinstance(arg, dict), 'args must be a dictionary'
                kwargs.update(arg)

        for name, value in kwargs.items():
            if name in self.trait_names:
                setattr(self, name, value)
            elif name in self.widget.trait_names():
                setattr(self.widget, name, value)


wridget_list = [
    'Audio',
    'Box',
    'BoundedFloatText',
    'BoundedIntText',
    'Button',
    'Checkbox',
    'ColorPicker',
    'ColorsInput',
    'Combobox',
    'Controller',
    'DatePicker',
    'DatetimePicker',
    'Dropdown',
    'FileUpload',
    'FloatLogSlider',
    'FloatProgress',
    'FloatRangeSlider',
    'FloatSlider',
    'FloatText',
    'FloatsInput',
    'HTML',
    'HTMLMath',
    'Image',
    'IntProgress',
    'IntRangeSlider',
    'IntSlider',
    'IntText',
    'IntsInput',
    'Label',
    'Password',
    'Play',
    'RadioButtons',
    'Select',
    'SelectMultiple',
    'SelectionRangeSlider',
    'SelectionSlider',
    'SliderStyle',
    'TagsInput',
    'Text',
    'Textarea',
    'TimePicker',
    'ToggleButton',
    'ToggleButtons',
    'ToggleButtonsStyle',
    'Valid',
    'ValueWidget',
    'Video',
]


class Button(Wridget):
    @wraps(Wridget.__init__, assigned=['__signature__'])
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.widget.add_traits(value=widgets.trait_types.traitlets.Any())
        self.set(value=kwargs.get('value'))

    def observe(self):
        self.widget.on_click(self._observe)


@wraps(Wridget.__init__, assigned=['__signature__'])
def _wridget_constructor(self, *args, **kwargs):
    Wridget.__init__(self, *args, **kwargs)


def _initialize_wridgets():
    for wridget in wridget_list:
        if wridget == 'Button':
            continue

        globals()[wridget] = type(wridget, (Wridget, ), {
            "__init__": _wridget_constructor,
        })


_initialize_wridgets()
