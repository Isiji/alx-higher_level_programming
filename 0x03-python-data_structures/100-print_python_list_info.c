#include <stdlib.h>
#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info -  function that prints some basic
 * @p: python list
 */
void print_python_list_info(PyObject *p)
{
	int number;

	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
}
