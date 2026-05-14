# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CardPaymentEnvironment81 import CardPaymentEnvironment81
from ._PaymentContext30 import PaymentContext30
from ._ReportGetTotalsRequest1 import ReportGetTotalsRequest1
from ._ReportTransactionRequest1 import ReportTransactionRequest1
from ._RetailerService6Code import RetailerService6Code
from ._SupplementaryData1 import SupplementaryData1

class ReportRequest8(base_types._BaseFieldType):

	__slots__ = ["_Cntxt", "_Envt", "_RptGetTtlsReq", "_RptTxReq", "_SplmtryData", "_SvcCntt"]
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
	def RptGetTtlsReq(self):
		return self._RptGetTtlsReq

	@RptGetTtlsReq.setter
	def RptGetTtlsReq(self, value):
		self._RptGetTtlsReq = value if type(value) != base_types.auto else self.make_default("RptGetTtlsReq")

	@RptGetTtlsReq.deleter
	def RptGetTtlsReq(self):
		del self._RptGetTtlsReq
		self._RptGetTtlsReq = None

	@property
	def RptTxReq(self):
		return self._RptTxReq

	@RptTxReq.setter
	def RptTxReq(self, value):
		self._RptTxReq = value if type(value) != base_types.auto else self.make_default("RptTxReq")

	@RptTxReq.deleter
	def RptTxReq(self):
		del self._RptTxReq
		self._RptTxReq = None

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
	def SvcCntt(self):
		return self._SvcCntt

	@SvcCntt.setter
	def SvcCntt(self, value):
		self._SvcCntt = value if type(value) != base_types.auto else self.make_default("SvcCntt")

	@SvcCntt.deleter
	def SvcCntt(self):
		del self._SvcCntt
		self._SvcCntt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cntxt', type=PaymentContext30, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Envt', type=CardPaymentEnvironment81, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptGetTtlsReq', type=ReportGetTotalsRequest1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptTxReq', type=ReportTransactionRequest1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SvcCntt', type=RetailerService6Code, min=1, max=1, mutex_group=None, array=False),
	))