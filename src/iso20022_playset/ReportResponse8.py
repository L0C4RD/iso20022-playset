from . import base_types
from .RetailerService7Code import RetailerService7Code
from .ReportGetTotalsResponse2 import ReportGetTotalsResponse2
from .CardPaymentEnvironment81 import CardPaymentEnvironment81
from .SupplementaryData1 import SupplementaryData1
from .ResponseType11 import ResponseType11
from .PaymentContext30 import PaymentContext30
from .ReportTransactionResponse7 import ReportTransactionResponse7

class ReportResponse8(base_types._BaseFieldType):

	__slots__ = ["_RptTxRspn", "_SvcCntt", "_RptGetTtlsRspn", "_SplmtryData", "_Rspn", "_Envt", "_Cntxt"]
	@property
	def RptTxRspn(self):
		return self._RptTxRspn

	@RptTxRspn.setter
	def RptTxRspn(self, value):
		self._RptTxRspn = value if type(value) != auto else self.make_default("RptTxRspn")

	@RptTxRspn.deleter
	def RptTxRspn(self):
		del self._RptTxRspn
		self._RptTxRspn = None

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
	def RptGetTtlsRspn(self):
		return self._RptGetTtlsRspn

	@RptGetTtlsRspn.setter
	def RptGetTtlsRspn(self, value):
		self._RptGetTtlsRspn = value if type(value) != auto else self.make_default("RptGetTtlsRspn")

	@RptGetTtlsRspn.deleter
	def RptGetTtlsRspn(self):
		del self._RptGetTtlsRspn
		self._RptGetTtlsRspn = None

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
		base_types.FieldEntry(name='RptTxRspn', type=ReportTransactionResponse7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcCntt', type=RetailerService7Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptGetTtlsRspn', type=ReportGetTotalsResponse2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Rspn', type=ResponseType11, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Envt', type=CardPaymentEnvironment81, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cntxt', type=PaymentContext30, min=1, max=1, mutex_group=None, array=False),
	))

