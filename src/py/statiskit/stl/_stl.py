__all__ = []


# Import Boost.Python module
from . import __stl


# Group template specializations
__stl.statiskit.stl._Generator = (__stl.statiskit.stl._Generator_10b14312eeb655268489cd34090870cf, __stl.statiskit.stl._Generator_3b59a0980c80518c808634f7a84dc3cd, __stl.statiskit.stl._Generator_745e4933f5b250d9bc5232fe864d0cf7, __stl.statiskit.stl._Generator_74bc331707c1505eb2f807cae7c32bbb, __stl.statiskit.stl._Generator_e76a1308464d5a9a837d9a61f942fae7)
__stl.std._BasicString = (__stl.std._BasicString_448c20257e485acda59dc59305fceb58)
__stl.std._Set = (__stl.std._Set_476c1c1f206251dba7af53c48f3f6e42, __stl.std._Set_6436891c9b6854f494789a812891cbe5, __stl.std._Set_858bbf0613575e2ebe4b0e5902107ad6, __stl.std._Set_882a8dd1e64a51b4a9da29ab852a852e)
__stl.std._BinaryFunction = (__stl.std._BinaryFunction_8f249c2863945cb59771b97c53bdafec)
__stl.std._UnorderedSet = (__stl.std._UnorderedSet_d48105936d4f5d09a78d2aa9f878fdb8)
__stl.std._Vector = (__stl.std._Vector_107131f9768c56e794a9b0de728d1738, __stl.std._Vector_6b9ae5eac40858c9a0f5e6e21c15d1d3, __stl.std._Vector_c047f2c3135554ceb57f166fd404cfc8, __stl.std._Vector_dc5522842bc75d8b9ac7b46020c60854)
__stl.std._EqualTo = (__stl.std._EqualTo_d0ba0922f2505f7b8e291326cad79af5)

# Define aliases
__stl.std._Set_6436891c9b6854f494789a812891cbe5.KeyType = __stl.std._BasicString_448c20257e485acda59dc59305fceb58
__stl.std._Set_6436891c9b6854f494789a812891cbe5.ValueType = __stl.std._BasicString_448c20257e485acda59dc59305fceb58
__stl.std._UnorderedSet_d48105936d4f5d09a78d2aa9f878fdb8.KeyEqual = __stl.std._EqualTo_d0ba0922f2505f7b8e291326cad79af5
__stl.statiskit.stl.VectorInt = __stl.std._Vector_6b9ae5eac40858c9a0f5e6e21c15d1d3
__stl.statiskit.stl.SetLessIntGenerator = __stl.statiskit.stl._Generator_e76a1308464d5a9a837d9a61f942fae7
__stl.statiskit.stl.SetLessIndexGenerator = __stl.statiskit.stl._Generator_10b14312eeb655268489cd34090870cf
__stl.statiskit.stl.SetLessIndex = __stl.std._Set_476c1c1f206251dba7af53c48f3f6e42
__stl.statiskit.stl.SetLessStringGenerator = __stl.statiskit.stl._Generator_745e4933f5b250d9bc5232fe864d0cf7
__stl.statiskit.stl.SetIndex = __stl.std._UnorderedSet_d48105936d4f5d09a78d2aa9f878fdb8
__stl.statiskit.stl.SetLessString = __stl.std._Set_6436891c9b6854f494789a812891cbe5
__stl.statiskit.stl.VectorString = __stl.std._Vector_c047f2c3135554ceb57f166fd404cfc8
__stl.statiskit.stl.SetLessDouble = __stl.std._Set_858bbf0613575e2ebe4b0e5902107ad6
__stl.statiskit.stl.VectorIndex = __stl.std._Vector_dc5522842bc75d8b9ac7b46020c60854
__stl.statiskit.stl.SetLessInt = __stl.std._Set_882a8dd1e64a51b4a9da29ab852a852e
__stl.statiskit.stl.SetLessDoubleGenerator = __stl.statiskit.stl._Generator_74bc331707c1505eb2f807cae7c32bbb
__stl.statiskit.stl.VectorDouble = __stl.std._Vector_107131f9768c56e794a9b0de728d1738
__stl.statiskit.stl.String = __stl.std._BasicString_448c20257e485acda59dc59305fceb58
__stl.statiskit.stl.SetIndexGenerator = __stl.statiskit.stl._Generator_3b59a0980c80518c808634f7a84dc3cd
__stl.statiskit.Indices = __stl.std._Set_476c1c1f206251dba7af53c48f3f6e42
__stl.std._Vector_c047f2c3135554ceb57f166fd404cfc8.ValueType = __stl.std._BasicString_448c20257e485acda59dc59305fceb58
