from . import base_types
from .ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount
from .GenericIdentification178 import GenericIdentification178
from .ValuationsDetails2 import ValuationsDetails2
from .ForeignExchangeTerms19 import ForeignExchangeTerms19
from .CashAccountIdentification5Choice import CashAccountIdentification5Choice

class CashBalance15(base_types._BaseFieldType):

	__slots__ = ["_CshAcct", "_FXDtls", "_ValtnDtls", "_Amt", "_TxLotNb"]
	@property
	def CshAcct(self):
		return self._CshAcct

	@CshAcct.setter
	def CshAcct(self, value):
		self._CshAcct = value if type(value) != base_types.auto else self.make_default("CshAcct")

	@CshAcct.deleter
	def CshAcct(self):
		del self._CshAcct
		self._CshAcct = None

	@property
	def FXDtls(self):
		return self._FXDtls

	@FXDtls.setter
	def FXDtls(self, value):
		self._FXDtls = value if type(value) != base_types.auto else self.make_default("FXDtls")

	@FXDtls.deleter
	def FXDtls(self):
		del self._FXDtls
		self._FXDtls = None

	@property
	def ValtnDtls(self):
		return self._ValtnDtls

	@ValtnDtls.setter
	def ValtnDtls(self, value):
		self._ValtnDtls = value if type(value) != base_types.auto else self.make_default("ValtnDtls")

	@ValtnDtls.deleter
	def ValtnDtls(self):
		del self._ValtnDtls
		self._ValtnDtls = None

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
	def TxLotNb(self):
		return self._TxLotNb

	@TxLotNb.setter
	def TxLotNb(self, value):
		self._TxLotNb = value if type(value) != base_types.auto else self.make_default("TxLotNb")

	@TxLotNb.deleter
	def TxLotNb(self):
		del self._TxLotNb
		self._TxLotNb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshAcct', type=CashAccountIdentification5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FXDtls', type=ForeignExchangeTerms19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValtnDtls', type=ValuationsDetails2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=ActiveOrHistoricCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxLotNb', type=GenericIdentification178, min=0, max=None, mutex_group=None, array=True),
	))

