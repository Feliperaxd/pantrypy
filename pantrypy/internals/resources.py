# -----------------------------------------------------------------------------
# PantryPy
# Copyright (c) 2023 Felipe Amaral dos Santos
# Licensed under the MIT License (see LICENSE file)
# -----------------------------------------------------------------------------

from .operation_engine import Operations
from typing import Any, Tuple
from .utils import Utils


__all__ = [
    'ArithmeticsResources',
    'ComparisonsResources',
    'FormattingResources',
    'IndexableResources',
    'IterableResources'
]

class ArithmeticsResources:
    """
    A class that provides the capability for comparative operations between 
    objects. Objects inheriting from this class can perform operations between 
    their attributes, which were passed through the constructor.
    The result of these operations will be of the same type as the object.
    
    Methods:
    - __add__: Addition operation with the left value.
    - __floordiv__: Floor division operation with the left value.
    - __mod__: Modulo operation with the left value.
    - __mul__: Multiplication operation with the left value.
    - __pow__: Power operation with the left value.
    - __sub__: Subtraction operation with the left value.
    - __truediv__: True division operation with the left value.
    
    - __radd__: Addition operation with the right value.
    - __rfloordiv__: Floor division operation with the right value.
    - __rmod__: Modulo operation with the right value.
    - __rmul__: Multiplication operation with the right value.
    - __rpow__: Power operation with the right value.
    - __rsub__: Subtraction operation with the right value.
    - __rtruediv__: True division operation with the right value.

    Usage:
    class MyObject(ArithmeticsResources):

        def __init__(self, value_a, value_b):
            self.value_a = value_a
            self.value_b = value_b

    out = MyObject(10, 20) + MyObject(20, 20)
    print(out.value_a, out.value_b)

    >>> 30 40
    """


    def __add__(
        self: Any, 
        other: Any
    ) -> Any:  
        
        output = Operations.operate_with_class_parameters(
            object_a=self,
            object_b=other,
            operator='+'
        )
        return type(self)(*output)
    
    def __floordiv__(
        self: Any, 
        other: Any
    ) -> Any:  
        
        output = Operations.operate_with_class_parameters(
            object_a=self,
            object_b=other,
            operator='//'
        )
        return type(self)(*output)
    
    def __mod__(
        self: Any, 
        other: Any
    ) -> Any:  
        
        output = Operations.operate_with_class_parameters(
            object_a=self,
            object_b=other,
            operator='%'
        )
        return type(self)(*output)

    def __mul__(
        self: Any, 
        other: Any
    ) -> Any:  
        
        output = Operations.operate_with_class_parameters(
            object_a=self,
            object_b=other,
            operator='*'
        )
        return type(self)(*output)
    
    def __pow__(
        self: Any, 
        other: Any
    ) -> Any:  
        
        output = Operations.operate_with_class_parameters(
            object_a=self,
            object_b=other,
            operator='**'
        )
        return type(self)(*output)   

    def __sub__(
        self: Any, 
        other: Any
    ) -> Any:  
        
        output = Operations.operate_with_class_parameters(
            object_a=self,
            object_b=other,
            operator='-'
        )
        return type(self)(*output)

    def __truediv__(
        self: Any, 
        other: Any
    ) -> Any:  

        output = Operations.operate_with_class_parameters(
            object_a=self, 
            object_b=other, 
            operator='/'
        )
        return type(self)(*output)
        
    def __radd__(
        self: Any, 
        other: Any
    ) -> Any:  
        
        output = Operations.operate_with_class_parameters(
            object_a=other,
            object_b=self,
            operator='+'
        )
        return type(self)(*output)
    
    def __rfloordiv__(
        self: Any, 
        other: Any
    ) -> Any:  
        
        output = Operations.operate_with_class_parameters(
            object_a=other,
            object_b=self,
            operator='//'
        )
        return type(self)(*output)
    
    def __rmod__(
        self: Any, 
        other: Any
    ) -> Any:  
        
        output = Operations.operate_with_class_parameters(
            object_a=other,
            object_b=self,
            operator='%'
        )
        return type(self)(*output)

    def __rmul__(
        self: Any, 
        other: Any
    ) -> Any:  
        
        output = Operations.operate_with_class_parameters(
            object_a=other,
            object_b=self,
            operator='*'
        )
        return type(self)(*output)
    
    def __rpow__(
        self: Any, 
        other: Any
    ) -> Any:  
        
        output = Operations.operate_with_class_parameters(
            object_a=other,
            object_b=self,
            operator='**'
        )
        return type(self)(*output)   

    def __rsub__(
        self: Any, 
        other: Any
    ) -> Any:  
        
        output = Operations.operate_with_class_parameters(
            object_a=other,
            object_b=self,
            operator='-'
        )
        return type(self)(*output)

    def __rtruediv__(
        self: Any, 
        other: Any
    ) -> Any:  

        output = Operations.operate_with_class_parameters(
            object_a=other, 
            object_b=self, 
            operator='/'
        )
        return type(self)(*output)


class ComparisonsResources:
    """
    A class that provides the capability for comparative operations between 
    objects. Objects inheriting from this class can perform operations between 
    their attributes, which were passed through the constructor.
    The result of these comparisons will be a tuple with boolean values 
    representing the comparison in the order of parameter definition.
    
    Methods:
    - __eq__: Equality comparison.
    - __ge__: Greater than or equal to comparison.
    - __gt__: Greater than comparison.
    - __le__: Less than or equal to comparison.
    - __lt__: Less than comparison.
    - __ne__: Inequality comparison.
    
    Usage:
    class MyObject(ComparisonsResources):

        def __init__(self, value_a, value_b):
            self.value_a = value_a
            self.value_b = value_b

    out = MyObject('foo', 20) == MyObject('bar', 20)
    print(out)

    >>> (False, True)
    """

    
    def __eq__(
        self: Any,
        other: Any
    ) -> Tuple[bool]:
        
        return Operations.operate_with_class_parameters(
            object_a=self,
            object_b=other,
            operator='=='
        )

    def __ge__(
        self: Any,
        other: Any
    ) -> Tuple[bool]:
        
        return Operations.operate_with_class_parameters(
            object_a=self,
            object_b=other,
            operator='>='
        )

    def __gt__(
        self: Any,
        other: Any
    ) -> Tuple[bool]:
        
        return Operations.operate_with_class_parameters(
            object_a=self,
            object_b=other,
            operator='>'
        )

    def __le__(
        self: Any,
        other: Any
    ) -> Tuple[bool]:
        
        return Operations.operate_with_class_parameters(
            object_a=self,
            object_b=other,
            operator='<='
        )

    def __lt__(
        self: Any,
        other: Any
    ) -> Tuple[bool]:
        
        return Operations.operate_with_class_parameters(
            object_a=self,
            object_b=other,
            operator='<'
        )

    def __ne__(
        self: Any,
        other: Any
    ) -> Tuple[bool]:
        
        return Operations.operate_with_class_parameters(
            object_a=self,
            object_b=other,
            operator='!='
        )


class FormattingResources:
    """
    Class used to return the 'formatted' attribute when the object is 
    converted to string.
    The object that inherits from this class must have a 
    'self.formatted' attribute.
    
    Methods:
    - __str__: To return the formatted attribute

    Usage:
    class MyObject(FormattingResources):

    def __init__(self, value_a):
        self.formatted = f'value_a is {value_a}'

    out = MyObject(20)
    print(out)

    >>> value_a is 20
    """

    
    def __str__(
        self: Any
    ) -> str:

        if hasattr(self, 'formatted'):        
            return str(self.formatted)
    
        else:
            Utils.warn_something(
                "'self.formatted' is required to inherit 'FormattingResources'."
            )
            return self.__repr__()
        

class IndexableResources:
    """
    Class used to make an object indexable, using attributes passed as 
    parameters as items

    Methods:
    - __delitem__: To delete the item leaving it as none
    - __getitem__: To return the item referring to the index.
    - __len__: To return the length.
    - __setitem__: To replace the value of an attribute using the index.

    Usage:
    class MyObject(IndexableResources):

        def __init__(self, value_a, value_b):
            self.value_a = value_a
            self.value_b = value_b

    out = MyObject('foo', 20)
    print(out[0], out[1])

    >>> foo 20
    """


    def __delitem__(
        self: Any,
        index: int
    ) -> None:
        
        setattr(self, self._parameters[index], None)
    
    def __getitem__(
        self: Any, 
        index: int
    ) -> Any:

        self._parameters = Utils.get_class_parameters(self)
        out = getattr(self, self._parameters[index])
        return out  

    def __len__(
        self: Any
    ) -> Any:
        return len(self._parameters)

    def __setitem__(
        self: Any, 
        index: int, 
        value: Any
    ) -> None:
        
        setattr(self, self._parameters[index], value)


class IterableResources:
    """
    Class used to make an object iterable, iterating through attributes 
    passed as parameters.

    Methods:
    - __iter__: To iterate the object.
    - __next__: To return the next item in the iteration.

    Usage:
    class MyObject(IterableResources):

        def __init__(self, value_a, value_b):
            self.value_a = value_a
            self.value_b = value_b

    for i in MyObject('foo', 20):
        print(i)

    >>> foo
    >>> 20
    """


    def __iter__(
        self: Any
    ) -> Any:

        self._parameters = Utils.get_class_parameters(self)
        self._index = 0
        return self

    def __next__(
        self: Any
    ) -> Any:
        
        if self._index < len(self._parameters):
            out = getattr(self, self._parameters[self._index])
            self._index += 1
            return out
        
        else:
            raise StopIteration
