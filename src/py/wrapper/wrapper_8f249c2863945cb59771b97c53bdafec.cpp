#include "_stl.h"



namespace autowig
{

}

#if defined(_MSC_VER)
    #if (_MSC_VER == 1900)
namespace boost
{
    template <> struct ::std::binary_function< unsigned long int, unsigned long int, bool > const volatile * get_pointer<struct ::std::binary_function< unsigned long int, unsigned long int, bool > const volatile >(struct ::std::binary_function< unsigned long int, unsigned long int, bool > const volatile *c) { return c; }
}
    #endif
#endif



void wrapper_8f249c2863945cb59771b97c53bdafec()
{

    std::string name_a5e4e9231d6351ccb0e06756b389f0af = boost::python::extract< std::string >(boost::python::scope().attr("__name__") + ".std");
    boost::python::object module_a5e4e9231d6351ccb0e06756b389f0af(boost::python::handle<  >(boost::python::borrowed(PyImport_AddModule(name_a5e4e9231d6351ccb0e06756b389f0af.c_str()))));
    boost::python::scope().attr("std") = module_a5e4e9231d6351ccb0e06756b389f0af;
    boost::python::scope scope_a5e4e9231d6351ccb0e06756b389f0af = module_a5e4e9231d6351ccb0e06756b389f0af;
    boost::python::class_< struct ::std::binary_function< unsigned long int, unsigned long int, bool >, autowig::Held< struct ::std::binary_function< unsigned long int, unsigned long int, bool > >::Type > class_8f249c2863945cb59771b97c53bdafec("_BinaryFunction_8f249c2863945cb59771b97c53bdafec", "", boost::python::no_init);
    class_8f249c2863945cb59771b97c53bdafec.def(boost::python::init<  >(""));
    class_8f249c2863945cb59771b97c53bdafec.def(boost::python::init< struct ::std::binary_function< unsigned long int, unsigned long int, bool > const & >(""));

}