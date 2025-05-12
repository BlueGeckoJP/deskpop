#!/bin/bash

if pkg-config --exists KF6WindowSystem; then
  echo "KDE Frameworks 6 found"
  KF_CFLAGS=$(pkg-config --cflags KF6WindowSystem)
  KF_LIBS=$(pkg-config --libs KF6WindowSystem)
else
  echo "Error: KWindowSystem not found"
  exit 1
fi

PYBIND_INCLUDES=$(python3 -m pybind11 --includes)
PYTHON_EXT=$(python3-config --extension-suffix)

echo "Compiling.."
g++ -O3 -Wall -shared --std=c++17 -fPIC \
  $PYBIND_INCLUDES $KF_CFLAGS \
  set_window_below.cpp \
  -o ../../set_window_below$PYTHON_EXT \
  $KF_LIBS

if [ $? -eq 0 ]; then
  echo "Compilation successful!"
  echo "Python module created: ../../set_window_below$PYTHON_EXT"
else
  echo "Compilation failed!"
fi