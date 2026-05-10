from . import base_types
from ._SupplementaryData1 import SupplementaryData1
from ._PaymentContext30 import PaymentContext30
from ._NonFinancialRequestContentComponent5 import NonFinancialRequestContentComponent5
from ._CardPaymentEnvironment81 import CardPaymentEnvironment81

class NonFinancialRequestComponent5(base_types._BaseFieldType):

	__slots__ = ["_NonFinReqCntt", "_Envt", "_SplmtryData", "_Cntxt"]
	@property
	def NonFinReqCntt(self):
		return self._NonFinReqCntt

	@NonFinReqCntt.setter
	def NonFinReqCntt(self, value):
		self._NonFinReqCntt = value if type(value) != base_types.auto else self.make_default("NonFinReqCntt")

	@NonFinReqCntt.deleter
	def NonFinReqCntt(self):
		del self._NonFinReqCntt
		self._NonFinReqCntt = None

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
	def Cntxt(self):
		return self._Cntxt

	@Cntxt.setter
	def Cntxt(self, value):
		self._Cntxt = value if type(value) != base_types.auto else self.make_default("Cntxt")

	@Cntxt.deleter
	def Cntxt(self):
		del self._Cntxt
		self._Cntxt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NonFinReqCntt', type=NonFinancialRequestContentComponent5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Envt', type=CardPaymentEnvironment81, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Cntxt', type=PaymentContext30, min=1, max=1, mutex_group=None, array=False),
	))

