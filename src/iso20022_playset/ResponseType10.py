from . import base_types
from .Max35Text import Max35Text
from .Max140Text import Max140Text
from .Response9Code import Response9Code

class ResponseType10(base_types._BaseFieldType):

	__slots__ = ["_RspnRsn", "_AddtlRspnInf", "_Rspn"]
	@property
	def RspnRsn(self):
		return self._RspnRsn

	@RspnRsn.setter
	def RspnRsn(self, value):
		self._RspnRsn = value if type(value) != auto else self.make_default("RspnRsn")

	@RspnRsn.deleter
	def RspnRsn(self):
		del self._RspnRsn
		self._RspnRsn = None

	@property
	def AddtlRspnInf(self):
		return self._AddtlRspnInf

	@AddtlRspnInf.setter
	def AddtlRspnInf(self, value):
		self._AddtlRspnInf = value if type(value) != auto else self.make_default("AddtlRspnInf")

	@AddtlRspnInf.deleter
	def AddtlRspnInf(self):
		del self._AddtlRspnInf
		self._AddtlRspnInf = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='RspnRsn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlRspnInf', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rspn', type=Response9Code, min=1, max=1, mutex_group=None, array=False),
	))

