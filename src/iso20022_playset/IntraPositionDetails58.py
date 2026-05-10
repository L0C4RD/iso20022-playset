from . import base_types
import Max350Text
import DateAndDateTime2Choice
import FinancialInstrumentQuantity33Choice
import SecuritiesSubBalanceTypeAndQuantityBreakdown5
import PriorityNumeric4Choice
import GenericIdentification37

class IntraPositionDetails58(base_types._BaseFieldType):

	__slots__ = ["_SctiesSubBalId", "_InstrPrcgAddtlDtls", "_Prty", "_BalFr", "_BalTo", "_SttlmQty", "_SttlmDt"]
	@property
	def SctiesSubBalId(self):
		return self._SctiesSubBalId

	@SctiesSubBalId.setter
	def SctiesSubBalId(self, value):
		self._SctiesSubBalId = value if type(value) != auto else self.make_default("SctiesSubBalId")

	@SctiesSubBalId.deleter
	def SctiesSubBalId(self):
		del self._SctiesSubBalId
		self._SctiesSubBalId = None

	@property
	def InstrPrcgAddtlDtls(self):
		return self._InstrPrcgAddtlDtls

	@InstrPrcgAddtlDtls.setter
	def InstrPrcgAddtlDtls(self, value):
		self._InstrPrcgAddtlDtls = value if type(value) != auto else self.make_default("InstrPrcgAddtlDtls")

	@InstrPrcgAddtlDtls.deleter
	def InstrPrcgAddtlDtls(self):
		del self._InstrPrcgAddtlDtls
		self._InstrPrcgAddtlDtls = None

	@property
	def Prty(self):
		return self._Prty

	@Prty.setter
	def Prty(self, value):
		self._Prty = value if type(value) != auto else self.make_default("Prty")

	@Prty.deleter
	def Prty(self):
		del self._Prty
		self._Prty = None

	@property
	def BalFr(self):
		return self._BalFr

	@BalFr.setter
	def BalFr(self, value):
		self._BalFr = value if type(value) != auto else self.make_default("BalFr")

	@BalFr.deleter
	def BalFr(self):
		del self._BalFr
		self._BalFr = None

	@property
	def BalTo(self):
		return self._BalTo

	@BalTo.setter
	def BalTo(self, value):
		self._BalTo = value if type(value) != auto else self.make_default("BalTo")

	@BalTo.deleter
	def BalTo(self):
		del self._BalTo
		self._BalTo = None

	@property
	def SttlmQty(self):
		return self._SttlmQty

	@SttlmQty.setter
	def SttlmQty(self, value):
		self._SttlmQty = value if type(value) != auto else self.make_default("SttlmQty")

	@SttlmQty.deleter
	def SttlmQty(self):
		del self._SttlmQty
		self._SttlmQty = None

	@property
	def SttlmDt(self):
		return self._SttlmDt

	@SttlmDt.setter
	def SttlmDt(self, value):
		self._SttlmDt = value if type(value) != auto else self.make_default("SttlmDt")

	@SttlmDt.deleter
	def SttlmDt(self):
		del self._SttlmDt
		self._SttlmDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SctiesSubBalId', type=GenericIdentification37, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrPrcgAddtlDtls', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prty', type=PriorityNumeric4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalFr', type=SecuritiesSubBalanceTypeAndQuantityBreakdown5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalTo', type=SecuritiesSubBalanceTypeAndQuantityBreakdown5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmQty', type=FinancialInstrumentQuantity33Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmDt', type=DateAndDateTime2Choice, min=1, max=1, mutex_group=None, array=False),
	))

