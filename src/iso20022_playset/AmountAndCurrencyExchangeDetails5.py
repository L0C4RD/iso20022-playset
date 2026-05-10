import base_types
import CurrencyExchange24
import ActiveOrHistoricCurrencyAndAmount

class AmountAndCurrencyExchangeDetails5(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_CcyXchg"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	@property
	def CcyXchg(self):
		return self._CcyXchg

	@CcyXchg.setter
	def CcyXchg(self, value):
		self._CcyXchg = value if type(value) != auto else self.make_default("CcyXchg")

	@CcyXchg.deleter
	def CcyXchg(self):
		del self._CcyXchg
		self._CcyXchg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveOrHistoricCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CcyXchg', type=CurrencyExchange24, min=0, max=1, mutex_group=None, array=False),
	))

