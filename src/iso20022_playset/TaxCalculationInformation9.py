from . import base_types
from .TaxBasis1Choice import TaxBasis1Choice

class TaxCalculationInformation9(base_types._BaseFieldType):

	__slots__ = ["_Bsis"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Bsis', type=TaxBasis1Choice, min=1, max=1, mutex_group=None, array=False),
	))

