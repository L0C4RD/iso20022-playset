from . import base_types
from .CardPaymentEnvironment81 import CardPaymentEnvironment81
from .LoginResponse7 import LoginResponse7
from .SupplementaryData1 import SupplementaryData1
from .PaymentContext30 import PaymentContext30
from .ResponseType11 import ResponseType11
from .RetailerService5Code import RetailerService5Code
from .DiagnosisResponse7 import DiagnosisResponse7

class SessionManagementResponse8(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_LgnRspn", "_DgnssRspn", "_Rspn", "_Envt", "_SvcCntt", "_Cntxt"]
	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def LgnRspn(self):
		return self._LgnRspn

	@LgnRspn.setter
	def LgnRspn(self, value):
		self._LgnRspn = value if type(value) != auto else self.make_default("LgnRspn")

	@LgnRspn.deleter
	def LgnRspn(self):
		del self._LgnRspn
		self._LgnRspn = None

	@property
	def DgnssRspn(self):
		return self._DgnssRspn

	@DgnssRspn.setter
	def DgnssRspn(self, value):
		self._DgnssRspn = value if type(value) != auto else self.make_default("DgnssRspn")

	@DgnssRspn.deleter
	def DgnssRspn(self):
		del self._DgnssRspn
		self._DgnssRspn = None

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
	def Envt(self):
		return self._Envt

	@Envt.setter
	def Envt(self, value):
		self._Envt = value if type(value) != auto else self.make_default("Envt")

	@Envt.deleter
	def Envt(self):
		del self._Envt
		self._Envt = None

	@property
	def SvcCntt(self):
		return self._SvcCntt

	@SvcCntt.setter
	def SvcCntt(self, value):
		self._SvcCntt = value if type(value) != auto else self.make_default("SvcCntt")

	@SvcCntt.deleter
	def SvcCntt(self):
		del self._SvcCntt
		self._SvcCntt = None

	@property
	def Cntxt(self):
		return self._Cntxt

	@Cntxt.setter
	def Cntxt(self, value):
		self._Cntxt = value if type(value) != auto else self.make_default("Cntxt")

	@Cntxt.deleter
	def Cntxt(self):
		del self._Cntxt
		self._Cntxt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LgnRspn', type=LoginResponse7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DgnssRspn', type=DiagnosisResponse7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rspn', type=ResponseType11, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Envt', type=CardPaymentEnvironment81, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcCntt', type=RetailerService5Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cntxt', type=PaymentContext30, min=1, max=1, mutex_group=None, array=False),
	))

