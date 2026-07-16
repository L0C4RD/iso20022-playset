# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CardPaymentEnvironment82
from . import PaymentContext30
from . import ReportGetTotalsRequest1
from . import ReportTransactionRequest1
from . import RetailerService6Code
from . import SupplementaryData1

class ReportRequest9(base_types._BaseFieldType):

	__slots__ = ["_Cntxt", "_Envt", "_RptGetTtlsReq", "_RptTxReq", "_SplmtryData", "_SvcCntt"]
	@property
	def Cntxt(self):
		return self._Cntxt

	@Cntxt.setter
	def Cntxt(self, value):
		self._Cntxt = value if value is not None else base_types.UninitialisedField(self, 'Cntxt', PaymentContext30, False)

	@Cntxt.deleter
	def Cntxt(self):
		del self._Cntxt
		self._Cntxt = base_types.UninitialisedField(self, 'Cntxt', PaymentContext30, False)

	@property
	def Envt(self):
		return self._Envt

	@Envt.setter
	def Envt(self, value):
		self._Envt = value if value is not None else base_types.UninitialisedField(self, 'Envt', CardPaymentEnvironment82, False)

	@Envt.deleter
	def Envt(self):
		del self._Envt
		self._Envt = base_types.UninitialisedField(self, 'Envt', CardPaymentEnvironment82, False)

	@property
	def RptGetTtlsReq(self):
		return self._RptGetTtlsReq

	@RptGetTtlsReq.setter
	def RptGetTtlsReq(self, value):
		self._RptGetTtlsReq = value if value is not None else base_types.UninitialisedField(self, 'RptGetTtlsReq', ReportGetTotalsRequest1, False)

	@RptGetTtlsReq.deleter
	def RptGetTtlsReq(self):
		del self._RptGetTtlsReq
		self._RptGetTtlsReq = base_types.UninitialisedField(self, 'RptGetTtlsReq', ReportGetTotalsRequest1, False)

	@property
	def RptTxReq(self):
		return self._RptTxReq

	@RptTxReq.setter
	def RptTxReq(self, value):
		self._RptTxReq = value if value is not None else base_types.UninitialisedField(self, 'RptTxReq', ReportTransactionRequest1, False)

	@RptTxReq.deleter
	def RptTxReq(self):
		del self._RptTxReq
		self._RptTxReq = base_types.UninitialisedField(self, 'RptTxReq', ReportTransactionRequest1, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@property
	def SvcCntt(self):
		return self._SvcCntt

	@SvcCntt.setter
	def SvcCntt(self, value):
		self._SvcCntt = value if value is not None else base_types.UninitialisedField(self, 'SvcCntt', RetailerService6Code, False)

	@SvcCntt.deleter
	def SvcCntt(self):
		del self._SvcCntt
		self._SvcCntt = base_types.UninitialisedField(self, 'SvcCntt', RetailerService6Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cntxt', type=PaymentContext30, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Envt', type=CardPaymentEnvironment82, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptGetTtlsReq', type=ReportGetTotalsRequest1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptTxReq', type=ReportTransactionRequest1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SvcCntt', type=RetailerService6Code, min=1, max=1, mutex_group=None, array=False),
	))