# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyCode
from . import DatePeriod2
from . import ISODateTime
from . import SecuritiesSettlementSystemIdentification2
from . import TransactionOperationType4Code

class SettlementFailsReportHeader2(base_types._BaseFieldType):

	__slots__ = ["_Ccy", "_CreDtTm", "_RptSts", "_RptgPrd", "_SctiesSttlmSys"]
	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if value is not None else base_types.UninitialisedField(self, 'Ccy', ActiveCurrencyCode, False)

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = base_types.UninitialisedField(self, 'Ccy', ActiveCurrencyCode, False)

	@property
	def CreDtTm(self):
		return self._CreDtTm

	@CreDtTm.setter
	def CreDtTm(self, value):
		self._CreDtTm = value if value is not None else base_types.UninitialisedField(self, 'CreDtTm', ISODateTime, False)

	@CreDtTm.deleter
	def CreDtTm(self):
		del self._CreDtTm
		self._CreDtTm = base_types.UninitialisedField(self, 'CreDtTm', ISODateTime, False)

	@property
	def RptSts(self):
		return self._RptSts

	@RptSts.setter
	def RptSts(self, value):
		self._RptSts = value if value is not None else base_types.UninitialisedField(self, 'RptSts', TransactionOperationType4Code, False)

	@RptSts.deleter
	def RptSts(self):
		del self._RptSts
		self._RptSts = base_types.UninitialisedField(self, 'RptSts', TransactionOperationType4Code, False)

	@property
	def RptgPrd(self):
		return self._RptgPrd

	@RptgPrd.setter
	def RptgPrd(self, value):
		self._RptgPrd = value if value is not None else base_types.UninitialisedField(self, 'RptgPrd', DatePeriod2, False)

	@RptgPrd.deleter
	def RptgPrd(self):
		del self._RptgPrd
		self._RptgPrd = base_types.UninitialisedField(self, 'RptgPrd', DatePeriod2, False)

	@property
	def SctiesSttlmSys(self):
		return self._SctiesSttlmSys

	@SctiesSttlmSys.setter
	def SctiesSttlmSys(self, value):
		self._SctiesSttlmSys = value if value is not None else base_types.UninitialisedField(self, 'SctiesSttlmSys', SecuritiesSettlementSystemIdentification2, False)

	@SctiesSttlmSys.deleter
	def SctiesSttlmSys(self):
		del self._SctiesSttlmSys
		self._SctiesSttlmSys = base_types.UninitialisedField(self, 'SctiesSttlmSys', SecuritiesSettlementSystemIdentification2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CreDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptSts', type=TransactionOperationType4Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgPrd', type=DatePeriod2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesSttlmSys', type=SecuritiesSettlementSystemIdentification2, min=1, max=1, mutex_group=None, array=False),
	))