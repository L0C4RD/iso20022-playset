from . import base_types
from .ReconciliationRequestData1 import ReconciliationRequestData1
from .PaymentContext30 import PaymentContext30
from .CardPaymentEnvironment81 import CardPaymentEnvironment81
from .SupplementaryData1 import SupplementaryData1

class ReconciliationRequest8(base_types._BaseFieldType):

	__slots__ = ["_RcncltnReqData", "_SplmtryData", "_Envt", "_Cntxt"]
	@property
	def RcncltnReqData(self):
		return self._RcncltnReqData

	@RcncltnReqData.setter
	def RcncltnReqData(self, value):
		self._RcncltnReqData = value if type(value) != auto else self.make_default("RcncltnReqData")

	@RcncltnReqData.deleter
	def RcncltnReqData(self):
		del self._RcncltnReqData
		self._RcncltnReqData = None

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
		base_types.FieldEntry(name='RcncltnReqData', type=ReconciliationRequestData1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Envt', type=CardPaymentEnvironment81, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cntxt', type=PaymentContext30, min=1, max=1, mutex_group=None, array=False),
	))

