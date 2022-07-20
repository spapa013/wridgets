import ipywidgets as widgets
from IPython.display import display, clear_output
import traceback


class Base:
    @staticmethod
    def _on_interact_wrapper(on_interact, output, overwrite_previous_output, on_interact_kws, is_disabled):
        if on_interact is None or is_disabled:
            return
        def run():
            try:
                on_interact(**on_interact_kws)
            except:
                traceback.print_exc()
        if output is not None:
            with output:
                if overwrite_previous_output:
                    clear_output()
                run()
        else:
            run()

    def observe(self):
        self.widget.observe(self._observe, names='value')


class StandardBase(Base):
    def __init__(self, on_interact=None, output=None, overwrite_previous_output=True, on_interact_kws=None, observe=True, *args, **kwargs):
        self.on_interact = on_interact
        self.output = output
        self.overwrite_previous_output = overwrite_previous_output
        self.on_interact_kws = {} if on_interact_kws is None else on_interact_kws
        self.on_interact_disabled = False
        self.widget = getattr(widgets, self.__class__.__name__)(*args, **kwargs)
        if observe:
            self.observe()

    def display(self):
        display(self.widget)
        if self.output is not None:
            display(self.output)

    def enable_on_interact(self):
        self.on_interact_disabled = False

    def disable_on_interact(self):
        self.on_interact_disabled = True

    def update_value(self, value, on_interact_disabled=False):
        if not on_interact_disabled:
            self.widget.value = value

        else:
            self.disable_on_interact()
            self.widget.value = value
            self.enable_on_interact()

    def _observe(self, change):
        self._on_interact_wrapper(on_interact=self.on_interact, output=self.output,
                        overwrite_previous_output=self.overwrite_previous_output, on_interact_kws=self.on_interact_kws, is_disabled=self.on_interact_disabled)


class BooleanBase(Base):
    def __init__(self, on_true=None, on_false=None, on_true_output=None, on_false_output=None, on_true_overwrite_previous_output=True, on_false_overwrite_previous_output=True, on_true_on_interact_kws=None, on_false_on_interact_kws=None, observe=True, *args, **kwargs):
        self.on_true = on_true
        self.on_false = on_false
        self.on_true_output = on_true_output
        self.on_false_output = on_false_output
        self.on_true_overwrite_previous_output = on_true_overwrite_previous_output
        self.on_false_overwrite_previous_output = on_false_overwrite_previous_output
        self.on_true_on_interact_kws = {} if on_true_on_interact_kws is None else on_true_on_interact_kws
        self.on_false_on_interact_kws = {} if on_false_on_interact_kws is None else on_false_on_interact_kws
        self.on_true_on_interact_disabled = False
        self.on_false_on_interact_disabled = False
        self.widget = getattr(widgets, self.__class__.__name__)(*args, **kwargs)
        if observe:
            self.observe()

    def display(self):
        display(self.widget)
        if self.on_true_output is not None:
            display(self.on_true_output)
        if self.on_false_output is not None:
            display(self.on_false_output)

    def enable_on_true_on_interact(self):
        self.on_true_on_interact_disabled = False

    def disable_on_true_on_interact(self):
        self.on_true_on_interact_disabled = True

    def enable_on_false_on_interact(self):
        self.on_false_on_interact_disabled = False

    def disable_on_false_on_interact(self):
        self.on_false_on_interact_disabled = True

    def update_value(self, value, on_interact_disabled=False):
        if not on_interact_disabled:
            self.widget.value = value

        else:
            self.disable_on_true_on_interact()
            self.disable_on_false_on_interact()
            self.widget.value = value
            self.enable_on_true_on_interact()
            self.enable_on_false_on_interact()

    def _observe(self, change):
        if self.widget.value:
            self._on_interact_wrapper(on_interact=self.on_true, output=self.on_true_output,
                                    overwrite_previous_output=self.on_true_overwrite_previous_output, on_interact_kws=self.on_true_on_interact_kws, is_disabled=self.on_true_on_interact_disabled)

        if not self.widget.value:
            self._on_interact_wrapper(on_interact=self.on_false, output=self.on_false_output,
                                        overwrite_previous_output=self.on_false_overwrite_previous_output, on_interact_kws=self.on_false_on_interact_kws, is_disabled=self.on_false_on_interact_disabled)
