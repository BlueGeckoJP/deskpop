#include <Python.h>
#include <kx11extras.h>
#include <netwm_def.h>
#include <pybind11/pybind11.h>

void set_window_below(long id) {
    KX11Extras::setState(id, NET::KeepBelow);
}

PYBIND11_MODULE(set_window_below, m) {
    m.def("set_window_below", &set_window_below, "set window below");
}
