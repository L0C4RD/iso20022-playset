import base_types
import SecuritiesSettlementSystemIdentification2
import DatePeriod2
import TransactionOperationType4Code
import ISODateTime
import ActiveCurrencyCode

class SettlementFailsReportHeader2(base_types._BaseFieldType):

	__slots__ = ["_CreDtTm", "_SctiesSttlmSys", "_RptgPrd", "_Ccy", "_RptSts"]
	@property
	def CreDtTm(self):
		return self._CreDtTm

	@CreDtTm.setter
	def CreDtTm(self, value):
		self._CreDtTm = value if type(value) != auto else self.make_default("CreDtTm")

	@CreDtTm.deleter
	def CreDtTm(self):
		del self._CreDtTm
		self._CreDtTm = None

	@property
	def SctiesSttlmSys(self):
		return self._SctiesSttlmSys

	@SctiesSttlmSys.setter
	def SctiesSttlmSys(self, value):
		self._SctiesSttlmSys = value if type(value) != auto else self.make_default("SctiesSttlmSys")

	@SctiesSttlmSys.deleter
	def SctiesSttlmSys(self):
		del self._SctiesSttlmSys
		self._SctiesSttlmSys = None

	@property
	def RptgPrd(self):
		return self._RptgPrd

	@RptgPrd.setter
	def RptgPrd(self, value):
		self._RptgPrd = value if type(value) != auto else self.make_default("RptgPrd")

	@RptgPrd.deleter
	def RptgPrd(self):
		del self._RptgPrd
		self._RptgPrd = None

	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if type(value) != auto else self.make_default("Ccy")

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = None

	@property
	def RptSts(self):
		return self._RptSts

	@RptSts.setter
	def RptSts(self, value):
		self._RptSts = value if type(value) != auto else self.make_default("RptSts")

	@RptSts.deleter
	def RptSts(self):
		del self._RptSts
		self._RptSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CreDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesSttlmSys', type=SecuritiesSettlementSystemIdentification2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgPrd', type=DatePeriod2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptSts', type=TransactionOperationType4Code, min=1, max=1, mutex_group=None, array=False),
	))

