# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import TaxBasis1Choice

class TaxCalculationInformation9(base_types._BaseFieldType):

	__slots__ = ["_Bsis"]
	@property
	def Bsis(self):
		return self._Bsis

	@Bsis.setter
	def Bsis(self, value):
		self._Bsis = value if value is not None else base_types.UninitialisedField(self, 'Bsis', TaxBasis1Choice, False)

	@Bsis.deleter
	def Bsis(self):
		del self._Bsis
		self._Bsis = base_types.UninitialisedField(self, 'Bsis', TaxBasis1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Bsis', type=TaxBasis1Choice, min=1, max=1, mutex_group=None, array=False),
	))