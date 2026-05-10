import base_types
import ActiveOrHistoricCurrencyAndAmountRange2
import ImpliedCurrencyAndAmountRange1

class ActiveOrHistoricAmountRange2Choice(base_types._BaseFieldType):

	__slots__ = ["_ImpldCcyAndAmtRg", "_CcyAndAmtRg"]
	@property
	def ImpldCcyAndAmtRg(self):
		return self._ImpldCcyAndAmtRg

	@ImpldCcyAndAmtRg.setter
	def ImpldCcyAndAmtRg(self, value):
		self._ImpldCcyAndAmtRg = value if type(value) != auto else self.make_default("ImpldCcyAndAmtRg")

	@ImpldCcyAndAmtRg.deleter
	def ImpldCcyAndAmtRg(self):
		del self._ImpldCcyAndAmtRg
		self._ImpldCcyAndAmtRg = None

	@property
	def CcyAndAmtRg(self):
		return self._CcyAndAmtRg

	@CcyAndAmtRg.setter
	def CcyAndAmtRg(self, value):
		self._CcyAndAmtRg = value if type(value) != auto else self.make_default("CcyAndAmtRg")

	@CcyAndAmtRg.deleter
	def CcyAndAmtRg(self):
		del self._CcyAndAmtRg
		self._CcyAndAmtRg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ImpldCcyAndAmtRg', type=ImpliedCurrencyAndAmountRange1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CcyAndAmtRg', type=ActiveOrHistoricCurrencyAndAmountRange2, min=0, max=1, mutex_group=1, array=False),
	))

