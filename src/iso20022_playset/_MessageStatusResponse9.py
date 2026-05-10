from . import base_types
from .SupplementaryData1 import SupplementaryData1
from .PaymentContext30 import PaymentContext30
from .ResponseType11 import ResponseType11
from .MessageStatusResponseData9 import MessageStatusResponseData9
from .CardPaymentEnvironment81 import CardPaymentEnvironment81

class MessageStatusResponse9(base_types._BaseFieldType):

	__slots__ = ["_MsgStsRspnData", "_Cntxt", "_SplmtryData", "_Envt", "_Rspn"]
	@property
	def MsgStsRspnData(self):
		return self._MsgStsRspnData

	@MsgStsRspnData.setter
	def MsgStsRspnData(self, value):
		self._MsgStsRspnData = value if type(value) != base_types.auto else self.make_default("MsgStsRspnData")

	@MsgStsRspnData.deleter
	def MsgStsRspnData(self):
		del self._MsgStsRspnData
		self._MsgStsRspnData = None

	@property
	def Cntxt(self):
		return self._Cntxt

	@Cntxt.setter
	def Cntxt(self, value):
		self._Cntxt = value if type(value) != base_types.auto else self.make_default("Cntxt")

	@Cntxt.deleter
	def Cntxt(self):
		del self._Cntxt
		self._Cntxt = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def Envt(self):
		return self._Envt

	@Envt.setter
	def Envt(self, value):
		self._Envt = value if type(value) != base_types.auto else self.make_default("Envt")

	@Envt.deleter
	def Envt(self):
		del self._Envt
		self._Envt = None

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
		base_types.FieldEntry(name='MsgStsRspnData', type=MessageStatusResponseData9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cntxt', type=PaymentContext30, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Envt', type=CardPaymentEnvironment81, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rspn', type=ResponseType11, min=1, max=1, mutex_group=None, array=False),
	))

