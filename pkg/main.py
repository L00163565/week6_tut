"""
# File : main.py
# Created : 03-11-2021 10:56
# Author : Snehal Shirsath
# Python Version : 3.9.7
# File Version : v1.0.0
# Description :
"""


from question1_pkg.student_class import Student
from question1_pkg.room_class import Room
from question1_pkg.module_class import Module

if __name__ == "__main__":
    std = Student()
    std.student_info()
    room = Room()
    room.Room_info()
    module = Module()
    module.module_info()