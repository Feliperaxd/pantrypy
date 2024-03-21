# -----------------------------------------------------------------------------
# PantryPy
# Copyright (c) 2023 Felipe Amaral dos Santos
# Licensed under the MIT License (see LICENSE file)
# -----------------------------------------------------------------------------

from colorama import Fore, init, Style
import inspect
import textwrap
from typing import Any, List


__all__ = [
    'Utils'
]

class Utils:
    """
    Class with various useful features, focusing on internal library usage.

    Methods:
    - get_class_parameters: To get the parameter names inside init.
    - get_class_parameters_values: to get the parameter values inside init.
    - warn_something: To warn something.
    """

    @staticmethod
    def get_class_parameters(
        class_instance: Any
    ) -> List[Any]:
        """ 
        To get the names of the class parameters.
        
        Parameters:
        - class_instance (Any): Must be the instance of the target class.
        
        Returns:
        - Returns a list with the name of all attributes passed as parameters by init.
        """

        signature = inspect.signature(class_instance.__init__)
        return [x for x in signature.parameters]
    
    @staticmethod
    def get_class_parameters_values(
        class_instance: Any
    ) -> List[Any]:
        """ 
        To get the values of the class parameters.
        
        Parameters:
        - class_instance (Any): Must be the instance of the target class.
        
        Returns:
        - Returns a list with the values of all attributes passed as parameters by init.
        """

        parameters = Utils.get_class_parameters(class_instance)
        return [getattr(class_instance, parameter) for parameter in parameters]

    @staticmethod
    def warn_something(
        message: str
    ) -> None:
        """
        Used this function to warn something with beautiful colors.
        The file and line where it was called will be displayed together in the warning.
        
        Parameters:
        - message (str): Message that will be displayed.
        """

        current_frame = inspect.currentframe().f_back.f_back
        frame_info = inspect.getframeinfo(current_frame)

        message = '\n '.join(
            textwrap.wrap(
                text=message,
                width=77
            )
        )
        local = '\n '.join(
            textwrap.wrap(
                text=f'{frame_info.filename} - L{frame_info.lineno}',
                width=70
            )
        )

        init() # Colorama init
        print(
            f"{Fore.LIGHTYELLOW_EX}{'-' * 36}WARNING{'-' * 36}{Style.RESET_ALL}\n",
            f"{Fore.MAGENTA}{message}{Style.RESET_ALL}\n",
            f"{Fore.BLUE}local:{Style.RESET_ALL} {Fore.GREEN}{local}{Style.RESET_ALL}"
        )
