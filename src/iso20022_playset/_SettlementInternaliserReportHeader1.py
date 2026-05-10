from . import base_types
from ._ActiveCurrencyCode import ActiveCurrencyCode
from ._ISODate import ISODate
from ._ISODateTime import ISODateTime
from ._TransactionOperationType4Code import TransactionOperationType4Code

class SettlementInternaliserReportHeader1(base_types._BaseFieldType):

	__slots__ = ["_Ccy", "_CreDtTm", "_RptSts", "_RptgDt"]
	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if type(value) != base_types.auto else self.make_default("Ccy")

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = None

	@property
	def CreDtTm(self):
		return self._CreDtTm

	@CreDtTm.setter
	def CreDtTm(self, value):
		self._CreDtTm = value if type(value) != base_types.auto else self.make_default("CreDtTm")

	@CreDtTm.deleter
	def CreDtTm(self):
		del self._CreDtTm
		self._CreDtTm = None

	@property
	def RptSts(self):
		return self._RptSts

	@RptSts.setter
	def RptSts(self, value):
		self._RptSts = value if type(value) != base_types.auto else self.make_default("RptSts")

	@RptSts.deleter
	def RptSts(self):
		del self._RptSts
		self._RptSts = None

	@property
	def RptgDt(self):
		return self._RptgDt

	@RptgDt.setter
	def RptgDt(self, value):
		self._RptgDt = value if type(value) != base_types.auto else self.make_default("RptgDt")

	@RptgDt.deleter
	def RptgDt(self):
		del self._RptgDt
		self._RptgDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CreDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptSts', type=TransactionOperationType4Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
	))

