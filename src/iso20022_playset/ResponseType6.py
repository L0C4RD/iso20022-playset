from . import base_types
from .ResultDetail3Code import ResultDetail3Code
from .Max140Text import Max140Text
from .Response2Code import Response2Code

class ResponseType6(base_types._BaseFieldType):

	__slots__ = ["_RspnDtl", "_Rspn", "_AddtlRspn"]
	@property
	def RspnDtl(self):
		return self._RspnDtl

	@RspnDtl.setter
	def RspnDtl(self, value):
		self._RspnDtl = value if type(value) != auto else self.make_default("RspnDtl")

	@RspnDtl.deleter
	def RspnDtl(self):
		del self._RspnDtl
		self._RspnDtl = None

	@property
	def Rspn(self):
		return self._Rspn

	@Rspn.setter
	def Rspn(self, value):
		self._Rspn = value if type(value) != auto else self.make_default("Rspn")

	@Rspn.deleter
	def Rspn(self):
		del self._Rspn
		self._Rspn = None

	@property
	def AddtlRspn(self):
		return self._AddtlRspn

	@AddtlRspn.setter
	def AddtlRspn(self, value):
		self._AddtlRspn = value if type(value) != auto else self.make_default("AddtlRspn")

	@AddtlRspn.deleter
	def AddtlRspn(self):
		del self._AddtlRspn
		self._AddtlRspn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RspnDtl', type=ResultDetail3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rspn', type=Response2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlRspn', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
	))

