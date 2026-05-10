from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._TaxBasis1Choice import TaxBasis1Choice

class TaxCalculationInformation10(base_types._BaseFieldType):

	__slots__ = ["_TaxblAmt", "_Bsis"]
	@property
	def TaxblAmt(self):
		return self._TaxblAmt

	@TaxblAmt.setter
	def TaxblAmt(self, value):
		self._TaxblAmt = value if type(value) != base_types.auto else self.make_default("TaxblAmt")

	@TaxblAmt.deleter
	def TaxblAmt(self):
		del self._TaxblAmt
		self._TaxblAmt = None

	@property
	def Bsis(self):
		return self._Bsis

	@Bsis.setter
	def Bsis(self, value):
		self._Bsis = value if type(value) != base_types.auto else self.make_default("Bsis")

	@Bsis.deleter
	def Bsis(self):
		del self._Bsis
		self._Bsis = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TaxblAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Bsis', type=TaxBasis1Choice, min=0, max=1, mutex_group=None, array=False),
	))

