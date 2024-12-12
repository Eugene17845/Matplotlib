import inspect
class Info:
    def __init__(self,obj):
        self.obj = obj

    def introspection_info(self, obj):
        pass

a = Info(42)

print({'type': type(a), 'attributes': getattr(a, 'obj'),'methods': dir(__builtins__), 'module': inspect.getmodule(a)})
