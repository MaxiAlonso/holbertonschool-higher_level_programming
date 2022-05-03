#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: = pointer to PyObject
 **/
void print_python_list_info(PyObject *p)
{
	int size = PyList_Size(p);
	int alloc = ((PyListObject *)p)->allocated;
	int i = 0;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	while (i < size)
	{
		printf("Element %d: %s\n", i, PyList_GetItem(p, i)->obj_type->tp_name);
		i++;
	}

}
