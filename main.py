# -*- coding:utf-8 -*-

import firestoreManage
import dataWrangling
from datetime import datetime


# Example usage
datetime_string = "2024-08-16 06:06:04.705000+00:00"
formatted_datetime = dataWrangling.convert_datetime_string(datetime_string)
print(formatted_datetime)  # Output: 16/08/2024 - 06:06:04