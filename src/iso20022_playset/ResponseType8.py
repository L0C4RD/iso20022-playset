from . import base_types
from .Max35Text import Max35Text

class ResponseType8(base_types._BaseFieldType):

	__slots__ = ["_AddtlRspnInf", "_RspndrId", "_RspnRsn", "_Cdfctn", "_Rspn"]
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
	def RspndrId(self):
		return self._RspndrId

	@RspndrId.setter
	def RspndrId(self, value):
		self._RspndrId = value if type(value) != base_types.auto else self.make_default("RspndrId")

	@RspndrId.deleter
	def RspndrId(self):
		del self._RspndrId
		self._RspndrId = None

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

	@property
	def Cdfctn(self):
		return self._Cdfctn

	@Cdfctn.setter
	def Cdfctn(self, value):
		self._Cdfctn = value if type(value) != base_types.auto else self.make_default("Cdfctn")

	@Cdfctn.deleter
	def Cdfctn(self):
		del self._Cdfctn
		self._Cdfctn = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlRspnInf', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspndrId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnRsn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cdfctn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rspn', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

