#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <structmember.h>
#include <string>

using namespace std;

struct PyHelloName {
  PyObject_HEAD
  string *name;
};

static PyObject *PyHelloName_set(PyHelloName *self, PyObject *args, PyObject *kwds) {
  static char *kwlist[] = {"name", NULL};
  const char *name = nullptr;

  if (!PyArg_ParseTupleAndKeywords(args, kwds, "s", kwlist, &name)) {
    PyErr_SetString(PyExc_RuntimeError, "PyHelloName_set: wrong arguments");
    return NULL;
  }
  self->name = new string();
  *self->name += string("Hello ") + string(name) + string("!");
  Py_RETURN_NONE;
}

static PyObject *PyHelloName_get(PyHelloName *self) {
  return PyUnicode_DecodeASCII(self->name->c_str(), self->name->size(), "ignore");
}

static PyMethodDef PyHelloName_methods[] = {
  {"set", (PyCFunction) PyHelloName_set, METH_VARARGS | METH_KEYWORDS, nullptr },
  {"get", (PyCFunction) PyHelloName_get, METH_NOARGS, nullptr },
  {NULL},
};

static void PyHelloName_dealloc(PyHelloName *self) {
  delete self->name;
}

static PyTypeObject PyHelloNameType = {
  .ob_base = PyVarObject_HEAD_INIT(NULL, 0)
  .tp_name = "native.HelloName",
  .tp_basicsize = sizeof(PyHelloName),
  .tp_itemsize = 0,
  .tp_dealloc = (destructor) PyHelloName_dealloc,
  .tp_flags = Py_TPFLAGS_DEFAULT,
  .tp_methods = PyHelloName_methods,
  .tp_new = PyType_GenericNew,
};

static PyModuleDef nativeModule = {
  .m_base = PyModuleDef_HEAD_INIT,
  .m_name = "native",
  .m_size = -1,
};

PyMODINIT_FUNC PyInit_native(void) {
  PyObject *m;
  if (PyType_Ready(&PyHelloNameType) < 0)
    return NULL;

  m = PyModule_Create(&nativeModule);
  if (m == NULL)
    return NULL;

  Py_INCREF(&PyHelloNameType);
  if (PyModule_AddObject(m, "HelloName", (PyObject *) &PyHelloNameType) < 0) {
    Py_DECREF(&PyHelloNameType);
    Py_DECREF(&m);
    return NULL;
  }
  return m;
}

