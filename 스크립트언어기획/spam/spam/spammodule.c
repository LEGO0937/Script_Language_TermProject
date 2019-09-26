#include "Python.h"

static PyObject *
make_url(PyObject *self, PyObject *args)// base_url, 서비스키, 시도, 군구, 자세한 항목
{
	char* str_main;
	char* str1;
	char* str2;
	char* str3;
	char* str4;

	//int len;
	if (!PyArg_ParseTuple(args, "sssss", &str_main, &str1, &str2, &str3, &str4))
		return NULL;



	strcat(str_main, str1);
	strcat(str_main, str2);
	strcat(str_main, str3);
	strcat(str_main, str4);



	//len = strlen(str);
	return Py_BuildValue("s", str_main);
}


static PyMethodDef Make_Url[] = { {
		"make_url", make_url, METH_VARARGS, "make url with some words." },{ NULL, NULL, 0, NULL } };


static struct PyModuleDef spammodule = {
	PyModuleDef_HEAD_INIT,
	"make_url",
	"It is test module.",
	-1, Make_Url
};

PyMODINIT_FUNC
PyInit_spam(void)
{
	return PyModule_Create(&spammodule);
}



