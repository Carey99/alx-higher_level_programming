#define PY_SSIZE_T_CLEAN
#include <Python.h>

static struct PyModuleDef module_def = {
	PyModuleDef_HEAD_INIT,
	"PyList",
	NULL,
	-1,
	PyListMethods
};
/**
 * print_python_list_info - Info about python lists
 * @p: Pointer to python list
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, alloc, i;
	PyObject *obj;

	size = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);
	for (i = 0; i < size; i++)
	{
		obj = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
	}
}
PyMODINIT_FUNC initPyList(void)
{
	return PyModule_Create(&module_def);
}
