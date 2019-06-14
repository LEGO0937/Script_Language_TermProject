#include "Python.h"

static PyObject *
make_url(PyObject *self, PyObject *args)// base_url, 서비스키, 시도, 군구, 자세한 항목
{
	char* str_main = "http://openapi.tour.go.kr/openapi/service/TourismResourceService/getTourResourceList?ServiceKey=qmAs0ut6m%2BwM%2FJwamfdK8RkKJz5yNmI4VrT6DEUuwmm%2FW7GMClJBCltEmgQEeSo7v1poVh0ZYPSbihUbMftNUQ%3D%3D&SIDO=";
	char* str1 = "&GUNGU=";
	char* str2 = "&RES_NM=";
	char* str_sido;
	char* str_gugun;
	char* str_name;

	//int len;
	if (!PyArg_ParseTuple(args, "sss", &str_sido, &str_gugun, &str_name))
		return NULL;



	strcat(str_main, str_sido);
	strcat(str_main, str1);
	strcat(str_main, str_gugun);
	strcat(str_main, str2);
	strcat(str_main, str_name);



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



//C:\Users\jung9\AppData\Local\Programs\Python\Python37\include
// http://openapi.tour.go.kr/openapi/service/TourismResourceService/getTourResourceList?ServiceKey=qmAs0ut6m%2BwM%2FJwamfdK8RkKJz5yNmI4VrT6DEUuwmm%2FW7GMClJBCltEmgQEeSo7v1poVh0ZYPSbihUbMftNUQ%3D%3D&SIDO=서울특별시&GUNGU=종로구&RES_NM=경복궁