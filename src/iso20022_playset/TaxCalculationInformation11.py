from . import base_types
from .TaxBasis1Choice import TaxBasis1Choice
from .ActiveCurrencyAndAmount import ActiveCurrencyAndAmount

class TaxCalculationInformation11(base_types._BaseFieldType):

	__slots__ = ["_Bsis", "_TaxblAmt"]
	@property
	def Bsis(self):
		return self._Bsis

	@Bsis.setter
	def Bsis(self, value):
		self._Bsis = value if type(value) != auto else self.make_default("Bsis")

	@Bsis.deleter
	def Bsis(self):
		del self._Bsis
		self._Bsis = None

	@property
	def TaxblAmt(self):
		return self._TaxblAmt

	@TaxblAmt.setter
	def TaxblAmt(self, value):
		self._TaxblAmt = value if type(value) != auto else self.make_default("TaxblAmt")

	@TaxblAmt.deleter
	def TaxblAmt(self):
		del self._TaxblAmt
		self._TaxblAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Bsis', type=TaxBasis1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxblAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))

