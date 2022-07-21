import functools
import traceback
from hashlib import md5

from . import wridgets as wr
from .utils import wrap


class App:
    # convert stores into class property methods
    @classmethod
    def set_store(cls, store, default=None):
        _store = ''.join(['_', store])
        setattr(cls, _store, default)
        getter = lambda cls: getattr(cls, _store)
        setattr(cls, store, property(getter))

    def display(self):
        wr.display(
            self.app
        )
    
    def with_output(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            with self.output:
                self.output.clear_output()
                try:
                    return func(self, *args, **kwargs)
                except Exception as e:
                    tb = traceback.format_exc()  
                    wr.display(
                        wr.HBox([
                            wr.Button(
                                on_interact=self._output.clear_output, 
                                button_style='info', 
                                description='Clear Output'
                            ).widget,
                            wr.Button(
                                on_interact=self.print_traceback,
                                action_kws=dict(tb=tb),
                                output=self.output,
                                button_style='info',
                                description='Traceback'
                            ).widget
                        ])
                    )
                    print(e)
        return wrapper
    
    @with_output
    def print_traceback(self, tb):
        wr.display(wr.Button(
            on_interact=self._output.clear_output, 
            button_style='info', 
            description='Clear Output'
        ).widget)
        print(tb)
    
    def __new__(cls, *args, **kwargs):
        obj = object.__new__(cls)
        obj.app = wr.VBox()
        return obj
    
    def __init_subclass__(cls):        
        # automatically assign output to methods
        base_method_list = [func for func in dir(App) if callable(getattr(App, func))]
        method_list = [func for func in dir(cls) if callable(getattr(cls, func)) and func not in base_method_list]
        for method in method_list:
            setattr(cls, method, cls.with_output(getattr(cls, method)))
        
        # set stores
        if hasattr(cls, 'stores'):
            for row in cls.stores:
                row = wrap(row)
                if len(row)==1:
                    cls.set_store(store=row[0])
                elif len(row)==2:
                    cls.set_store(store=row[0], default=row[1])
        
        cls.make = cls._build(cls._make(cls.make))
    
    def __init__(self, **kwargs):
        self._base = None 
        self._output = wr.Output()
        self._app_layout = []
        self.children = AppGroup()
        
        self.set_config(**kwargs)
        self.base = kwargs.get('base')
        self.make(**self.config)

    def _make(self, func):
        @functools.wraps(func)
        def wrapper(self, **kwargs):
            self.set_config(**kwargs)
            func(self, **kwargs)
        return wrapper

    def make(self, **kwargs):
        pass

    def update(self, **kwargs):
        self.set_config(update=True, **kwargs)
        self.make(**self.config)
    
    @property
    def app_layout(self):
        return self._app_layout
    
    @property
    def output(self):
        return self._output
    
    def clear_output(self):
        self.output.clear_output()
    
    @property
    def config(self):
        return self._config
    
    @property
    def base(self):
        return self._base
    
    @base.setter
    def base(self, app):
        if app is not None:
            self.children = app.children
            self._app_layout = app.app_layout
            self._base = app
            self.build()

    @property
    def name(self):
        return self.config.get('name')

    @property
    def propagate(self):
        return self.config.get('propagate')

    def message(self, msg:str):
        with self.output:
            self.clear_output()
            (wr.Label(label=msg, fontsize=0.5) + 
            Button(description='Clear', button_style='warning', on_interact=self.clear_output)
            ).display()

    def set_config(self, update=False, **kwargs):
        kwargs.setdefault('name', self.__class__.__name__)
        kwargs.setdefault('output', self.output)
        kwargs.setdefault('display_output', True)
        kwargs.setdefault('propagate', False)
        if not update:
            self._config = kwargs
        else:
            self._config.update(kwargs)
    
    def _build(func):
        @functools.wraps(func)
        def wrapper(self, **kwargs):
            func(self, **kwargs)
            self.build()
        return wrapper
    
    def build(self):
        if self.config.get('display_output'):
            self.app.children = [wr.HBox(row) for row in self.app_layout] + [self.output]
        else:
            self.app.children = [wr.HBox(row) for row in self.app_layout]
    
    @property
    def model_id(self):
        if not isinstance(self, Wridget):
            ids = []
            for _, value in self.children:
                model_id = getattr(value, 'model_id', None)
                model_id = value.wridget.widget.model_id if model_id is None else model_id
                ids.append(model_id)
            encoded = ''.join(ids).encode()
            dhash = md5()
            dhash.update(encoded)
            return dhash.hexdigest()
        else:
            return self.wridget.widget.model_id

    def _union(self, other):
        if isinstance(other, App):
            obj = App()
            obj.children = self.children + other.children
            for source in [self, other]:
                if source.propagate:
                    setattr(obj.children, source.name, source)
            return obj
        else:
            raise TypeError(f'Cannot add type {type(self)} to type {type(other)}.')
    
    def _horizontal_app_layout(self, other):
        return [
            [
                self.app, other.app
            ]
        ]
    
    def _vertical_app_layout(self, other):
        return [
            [
                self.app
            ],
            [
                other.app
            ]
        ]
    
    def __add__(self, other):
        obj = self._union(other)
        obj._app_layout = self._horizontal_app_layout(other)
        obj.build()
        return obj
    
    def __sub__(self, other):
        obj = self._union(other)
        obj._app_layout = self._vertical_app_layout(other)
        obj.build()
        return obj
    
    def __iter__(self):
        yield from self.children.__iter__()
    
    def _subset(self, include=None, exclude=None):
        widgets = {}
        for name, value in self.children:
            if isinstance(value, Wridget):
                widgets[name] = value
        
        subset = set(widgets.keys())
        if include is not None:
            subset = set(widgets.keys()).intersection(wrap(include))
        if exclude is not None:
            subset = set(widgets.keys()).difference(wrap(exclude))
        return {k: v for k, v in widgets.items() if k in subset}

    def get(self, name, include=None, exclude=None):
        widgets = self._subset(include=include, exclude=exclude)
        return {k: getattr(v.wridget.widget, name) for k, v in widgets.items()}

    def get1(self, name, include=None, exclude=None):
        d = list(self.get(name=name, include=include, exclude=exclude).values())
        assert len(d) == 1, f'get1 must return one value'
        return d[0]

    def set(self, name, value, include=None, exclude=None):
        widgets = self._subset(include=include, exclude=exclude)
        for v in widgets.values():
            setattr(v.wridget.widget, name, value)

    def run(self, name, include=None, exclude=None, *args, **kwargs):
        widgets = self._subset(include=include, exclude=exclude)
        for v in widgets.values():
            getattr(v.wridget.widget, name).run(*args, **kwargs)


class AppGroup:
    def __init__(self, *args, **kwargs):
        for value in args:
            self.__setattr__(value.name, value)
            
        for name, value in kwargs.items():
            self.__setattr__(name, value)
            
    def __setattr__(self, name, value):
        cont = False
        new_model_id = getattr(value, 'model_id', None)
        if new_model_id is not None:
            original = getattr(self, name, None)
            if original is not None:
                original_model_id = getattr(original, 'model_id', None)
                if original_model_id is not None and original_model_id == new_model_id:
                    self.__dict__[name] = value
                else:
                    cont = True
            else:
                cont = True
        else:
            cont = True

        if cont:
            i = 1
            base = name
            while hasattr(self, name):
                i += 1
                name = base
                name += str(i)
            if getattr(value, 'name', name) != name:
                value.set_config(name=name, update=True)
            self.__dict__[name] = value
    
    def __iter__(self):
        yield from self.__dict__.items()
        
    def __add__(self, other):
        if isinstance(other, AppGroup):
            obj = AppGroup()
            for source in [self, other]:
                for name, value in source:
                    setattr(obj, name, value)
            return obj
        else:
            raise TypeError(f'Cannot add type {type(self)} to type {type(other)}.')

    def __repr__(self):
        return str(tuple([a for a, _ in self if not a.startswith('_')]))
        

class Wridget:
    def __init_subclass__(cls) -> None:
        assert hasattr(cls, '_widget_types'), 'Subclasses of wridget must specify _widget_types'

    def _set_wridget(self, **kwargs):
        assert kwargs.get('widget_type') in self._widget_types, f'Allowed types are {self._widget_types}'
        try:
            delattr(self.children, self.config.get('name'))
        except:
            pass
        setattr(self.children, self.config.get('name'), self)
        self.wridget = getattr(wr, kwargs.get('widget_type'))(**kwargs)
        self._app_layout = [
                [
                    self.wridget.widget
                ]
        ]


class Label(App, Wridget):
    _widget_types = 'HTML',
    def make(self, **kwargs):
        kwargs.setdefault('widget_type', 'HTML')
        kwargs.setdefault('label', '')
        kwargs.setdefault('fontsize', 1)
        kwargs['value'] = f"<font size='+{kwargs.get('fontsize')}'>{kwargs.get('label')}</font>"
        self.set_config(**kwargs, update=True)
        self._set_wridget(**kwargs)


class Button(App, Wridget):
    _widget_types = 'Button',
    def make(self, **kwargs):
        kwargs.setdefault('widget_type', 'Button')
        kwargs.setdefault('value', None)
        kwargs.setdefault('layout', {'width': 'auto'})
        self.set_config(**kwargs, update=True)
        self._set_wridget(**kwargs)


class Field(App, Wridget):
    _widget_types = ('Text', 'Textarea', 'IntText', 'FloatText', 'BoundedIntText', 'BoundedFloatText')
    def make(self, **kwargs):
        kwargs.setdefault('widget_type', 'Text')
        kwargs.setdefault('continuous_update', False)
        kwargs.setdefault('layout', {'width': 'auto'})
        self.set_config(**kwargs, update=True)
        self._set_wridget(**kwargs)


class SelectButtons(App, Wridget):
    _widget_types = 'ToggleButtons', 'RadioButtons'
    def make(self, **kwargs):
        kwargs.setdefault('widget_type', 'ToggleButtons')
        kwargs.setdefault('options', ())
        kwargs.setdefault('style', {'button_width': 'auto'})
        self.set_config(**kwargs, update=True)
        self._set_wridget(**kwargs)


class ToggleButton(App, Wridget):
    _widget_types = 'ToggleButton',
    def make(self, **kwargs):
        kwargs.setdefault('widget_type', 'ToggleButton')
        kwargs.setdefault('style', {'button_width': 'auto'})
        self.set_config(**kwargs, update=True)
        self._set_wridget(**kwargs)


class Dropdown(App, Wridget):
    _widget_types = 'Dropdown',
    def make(self, **kwargs):
        kwargs.setdefault('widget_type', 'Dropdown')
        kwargs.setdefault('layout',  {'width': 'auto'})
        self.set_config(**kwargs, update=True)
        self._set_wridget(**kwargs)


class Link(App, Wridget):
    _widget_types = 'HTML'
    def make(self, **kwargs):
        kwargs.setdefault('widget_type', 'HTML')
        kwargs.setdefault('src', '')
        kwargs.setdefault('text', kwargs.get('src'))
        kwargs.setdefault('fontsize', 1)
        kwargs.setdefault('link_color', 'blue')
        kwargs.setdefault('link_background_color', 'transparent')
        kwargs.setdefault('link_text_decoration', 'underline')
        kwargs.setdefault('visited_color', 'purple')
        kwargs.setdefault('visited_background_color', 'transparent')
        kwargs.setdefault('visited_text_decoration', 'underline')
        kwargs['value'] = f"""
            <style>
            a:link {{
            color: {kwargs.get('link_color')};
            background-color: {kwargs.get('link_background_color')};
            text-decoration: {kwargs.get('link_text_decoration')};
            }}

            a:visited {{
            color: {kwargs.get('visited_color')};
            background-color: {kwargs.get('visited_background_color')};
            text-decoration: {kwargs.get('visited_text_decoration')};
            }}
            </style>
            <font size='+{kwargs.get('fontsize')}'>
            <a href={kwargs.get('src')} target='_blank'>{kwargs.get('text')}</a>
            </font>
            """
        self.set_config(**kwargs, update=True)
        self._set_wridget(**kwargs)
