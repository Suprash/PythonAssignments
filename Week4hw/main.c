
#include <Python.h>

static PyObject* squ (PyObject* self, PyObject* args)
{
    int a,b;
    if (!PyArg_ParseTuple(args,"ii",&a))
    {
        return NULL;
    }
    return Py_BuildValue("i",a*a);
}

static PyMethodDef MyMethods[] =
{
    {"square",squ,METH_VARARGS,"Square of a Number"},
    {NULL,NULL,0,NULL}
};

static struct PyModuleDef  mymodule = 
{
    PyModuleDef_HEAD_INIT,"mymodule",NULL,-1,MyMethods
};

PyMODINIT_FUNC PyInit_mymodule(void)
{
    return PyModule_Create(&mymodule);
}