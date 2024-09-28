# PagesManager
# Copyright (C) 2024 CycleBai
# 
# This code is offered under the following two licenses:
# 
# 1. **GNU General Public License (GNU GPL)**
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.
# 2. **Commercial License**
#   - If you intend to use this code for commercial purposes or need to use 
#     it in a way that does not comply with the GNU GPL, please contact 
#     zeeker-dev@proton.me to obtain a commercial license.
#   - The fees and terms for the commercial license will be discussed and 
#     determined with CycleBai.
# 

import SeniorOS.lib.log_manager as LogManager
import gc,sys

Log = LogManager.Log

class Main:
    def __init__(self) -> None:
        pass
    @staticmethod
    def Import(moduleLoc: str, funcName: str, log = True, *argument) -> bool:
        gc.collect()
        if log:Log.Info(moduleLoc + " " + funcName + "(func)")
        try:
            gc.collect()
            getattr(__import__(moduleLoc, globals(), locals(), [funcName]), funcName)(*argument)
            gc.collect()
        except Exception as e:
            Log.Error(moduleLoc + " > ERROR LOG THROWN:")
            print("--------------------------------------------------")
            sys.print_exception(e)
            print("--------------------------------------------------")
            return False
        else:
            gc.collect()
            return True