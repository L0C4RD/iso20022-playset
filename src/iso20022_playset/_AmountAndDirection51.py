from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._CreditDebitCode import CreditDebitCode
from ._ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount

class AmountAndDirection51(base_types._BaseFieldType):

	__slots__ = ["_OrgnlCcyAndOrdrdAmt", "_CdtDbtInd", "_Amt"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != base_types.auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	@property
	def CdtDbtInd(self):
		return self._CdtDbtInd

	@CdtDbtInd.setter
	def CdtDbtInd(self, value):
		self._CdtDbtInd = value if type(value) != base_types.auto else self.make_default("CdtDbtInd")

	@CdtDbtInd.deleter
	def CdtDbtInd(self):
		del self._CdtDbtInd
		self._CdtDbtInd = None

	@property
	def OrgnlCcyAndOrdrdAmt(self):
		return self._OrgnlCcyAndOrdrdAmt

	@OrgnlCcyAndOrdrdAmt.setter
	def OrgnlCcyAndOrdrdAmt(self, value):
		self._OrgnlCcyAndOrdrdAmt = value if type(value) != base_types.auto else self.make_default("OrgnlCcyAndOrdrdAmt")

	@OrgnlCcyAndOrdrdAmt.deleter
	def OrgnlCcyAndOrdrdAmt(self):
		del self._OrgnlCcyAndOrdrdAmt
		self._OrgnlCcyAndOrdrdAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlCcyAndOrdrdAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))

