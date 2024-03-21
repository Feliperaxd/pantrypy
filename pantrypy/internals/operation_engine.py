# -----------------------------------------------------------------------------
# PantryPy
# Copyright (c) 2023 Felipe Amaral dos Santos
# Licensed under the MIT License (see LICENSE file)
# -----------------------------------------------------------------------------

from .utils import Utils
from typing import Any, Iterable, Tuple, Union


__all__ = [
    'Operations'
]

class Operations:
    """
    Used to perform operations in various formats, focused on internal use!

    Methods:
    - operate_any_for_any:
    - operate_all_for_all: To practice an operation between two iterables.
    - operate_one_for_all: Use to perform operations using the same value on all 
    other values of an iterable object.
    - operate_one_for_one: Use to perform arithmetic or comparative operations.
    """


    @staticmethod
    def operate_any_for_any(
        object_a: Any, 
        object_b: Any,
        operator: str
    ) -> Union[Tuple[Union[bool, float, int]], Union[bool, float, int]]:
        """
        Used to perform operations between an iterable object and a non-iterable one, 
        between two non-iterable objects, or between two iterable objects. 
        Strings will not be considered iterable here; 
        use '.split' if you want to operate on strings as iterables.

        Parameters:
        - object_a (Any): The iterable or non-iterable object that will be used 
        in the operation.
        - object_b (Any): The iterable or non-iterable object that will be used 
        in the operation.
        - operator (str): Operator used in arithmetic or comparison operations.
        
        Returns:
        - If 'object_a' or 'object_b' is an iterable object, it returns a tuple with 
        the results of each operation.
        - If 'object_a' and 'object_b' are non-iterable objects, it returns a single 
        value with the result of the operation.
        """

        # Strings are also iterable, but should not be considered here!
        obj_a_is_iter = (
            hasattr(object_a, '__iter__') and 
            not isinstance(object_a, str)
        )
        obj_b_is_iter = (
            hasattr(object_b, '__iter__') and 
            not isinstance(object_b, str)
        )        

        if obj_a_is_iter and obj_b_is_iter:
            return Operations.operate_all_for_all(
                object_a=object_a,
                object_b=object_b,
                operator=operator
            ) 
        elif not obj_a_is_iter and not obj_b_is_iter:
            return Operations.operate_one_for_one(
                object_a=object_a,
                object_b=object_b,
                operator=operator
            )
        else:
            return Operations.operate_one_for_all(
                object_a=object_a,
                object_b=object_b,
                operator=operator
            )

    @staticmethod
    def operate_all_for_all(
        object_a: Iterable[Any], 
        object_b: Iterable[Any],
        operator: str
    ) -> Tuple[Union[bool, float, int]]:
        """
        Used to iterate and perform operations between two iterable objects!
        
        Parameters:
        - object_a (Iterable[Any]): Items that will be operated!
        - object_b (Iterable[Any]): Items that will be operated!
        - operator (str): Operator used in arithmetic or comparison operations.

        Returns:
        - A tuple containing the result of the operations performed at each index.
        """
        
        output = []
        for left_value, right_value in zip(object_a, object_b):
            output.append(
                Operations.operate_one_for_one(
                    left_value=left_value,
                    right_value=right_value,
                    operator=operator
                )
            ) 
        return tuple(output)
    
    @staticmethod
    def operate_one_for_all(
        object_a: Union[Iterable[Any], Any], 
        object_b: Union[Iterable[Any], Any],
        operator: str
    ) -> Tuple[Union[bool, float, int]]:
        """
        Use to perform operations using the same value on all other values of an 
        iterable object.
        Changing the order of input for the single object and iterable object can 
        result in different outcomes.

        Parameters:
        - object_a (Union[Iterable[Any], Any]): A single value to operate on the 
        other object, or the object that will be operated.
        - object_b (Union[Iterable[Any], Any]): A single value to operate on the 
        other object, or the object that will be operated.
        - operator (str): Operator used in arithmetic or comparison operations.

        Returns:
        - A tuple containing the result of the operations performed at each index.
        """

        # Strings are also iterable, but should not be considered here!
        obj_a_is_iter = (
            hasattr(object_a, '__iter__') and 
            not isinstance(object_a, str)
        )
        obj_b_is_iter = (
            hasattr(object_b, '__iter__') and 
            not isinstance(object_b, str)
        )
        
        if not obj_a_is_iter and not obj_b_is_iter:
            raise TypeError(
                "Expected iterable object in the 'object_a' or 'object_b' parameter."
            )
        elif obj_a_is_iter and obj_b_is_iter:
            raise TypeError(
                "Expected non-iterable object in the 'object_a' or 'object_b' parameter."
            )

        if obj_a_is_iter: 
            all_values = object_a
        elif obj_b_is_iter:
            all_values = object_b

        output = []
        for value in all_values:
            if obj_a_is_iter:
                left_value, right_value = value, object_b 
            elif obj_b_is_iter:
                left_value, right_value = object_a, value
            
            output.append(
                Operations.operate_one_for_one(
                    left_value=left_value,
                    right_value=right_value,
                    operator=operator
                )
            ) 
        return tuple(output)
    
    @staticmethod
    def operate_one_for_one(
        left_value: Any,
        right_value: Any,
        operator: str
    ) -> Union[bool, float, int]:
        """
        Use to perform arithmetic or comparative operations.

        Parameters:
        - left_value (Any): The left value at the time of the operation.
        - right_value (Any): The right value at the time of the operation.
        - operator (str): Operator used in the operation, accepts arithmetic and 
        comparison operators.

        Returns:
        - The result of the operation.
        """

        # To prevent 'eval' from identifying what is inside the 
        # 'left_value' or 'right_value' as a variable.
        if isinstance(left_value, str):
            left_value = f'"{left_value}"'
        if isinstance(right_value, str):
            right_value = f'"{right_value}"'

        output = (
            eval(f'{left_value}{operator}{right_value}')
        )
        return output
    
    @staticmethod
    def operate_with_class_parameters(
        object_a: Any,
        object_b: Any,
        operator: str
    ) -> Tuple[bool, float, int]:
        """
        To operate in the 'operate_any_for_any' method but using the class parameters 
        as values.
        
        Parameters:
        - object_a (Any): The iterable, non-iterable or any other object that will be 
        used in the operation.
        - object_b (Any): The iterable, non-iterable or any other object that will be
        used in the operation.
        - operator (str): Operator used in arithmetic or comparison operations.

        Returns:
        - A tuple containing the result of the operations performed at each index.
        """

        if not isinstance(object_a, (complex, float, int, list, str, tuple)):
            object_a = Utils.get_class_parameters_values(object_a)
        if not isinstance(object_b, (complex, float, int, list, str, tuple)):
            object_b = Utils.get_class_parameters_values(object_b)
        
        output = Operations.operate_any_for_any(
            object_a=object_a,
            object_b=object_b,
            operator=operator
        )
        return output
    