from . import base_types
from ._Max35Text import Max35Text
from ._Max140Text import Max140Text
from ._Response9Code import Response9Code

class ResponseType10(base_types._BaseFieldType):

	__slots__ = ["_Rspn", "_AddtlRspnInf", "_RspnRsn"]
	@property
	def Rspn(self):
		return self._Rspn

	@Rspn.setter
	def Rspn(self, value):
		self._Rspn = value if type(value) != base_types.auto else self.make_default("Rspn")

	@Rspn.deleter
	def Rspn(self):
		del self._Rspn
		self._Rspn = None

	@property
	def AddtlRspnInf(self):
		return self._AddtlRspnInf

	@AddtlRspnInf.setter
	def AddtlRspnInf(self, value):
		self._AddtlRspnInf = value if type(value) != base_types.auto else self.make_default("AddtlRspnInf")

	@AddtlRspnInf.deleter
	def AddtlRspnInf(self):
		del self._AddtlRspnInf
		self._AddtlRspnInf = None

	@property
	def RspnRsn(self):
		return self._RspnRsn

	@RspnRsn.setter
	def RspnRsn(self, value):
		self._RspnRsn = value if type(value) != base_types.auto else self.make_default("RspnRsn")

	@RspnRsn.deleter
	def RspnRsn(self):
		del self._RspnRsn
		self._RspnRsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rspn', type=Response9Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlRspnInf', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnRsn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

