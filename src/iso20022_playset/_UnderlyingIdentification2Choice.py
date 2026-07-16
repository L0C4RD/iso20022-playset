# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrumentIdentification7Choice
from . import SwapLegIdentification2

class UnderlyingIdentification2Choice(base_types._BaseFieldType):

	__slots__ = ["_Othr", "_Swp"]
	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if value is not None else base_types.UninitialisedField(self, 'Othr', FinancialInstrumentIdentification7Choice, False)

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = base_types.UninitialisedField(self, 'Othr', FinancialInstrumentIdentification7Choice, False)

	@property
	def Swp(self):
		return self._Swp

	@Swp.setter
	def Swp(self, value):
		self._Swp = value if value is not None else base_types.UninitialisedField(self, 'Swp', SwapLegIdentification2, False)

	@Swp.deleter
	def Swp(self):
		del self._Swp
		self._Swp = base_types.UninitialisedField(self, 'Swp', SwapLegIdentification2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Othr', type=FinancialInstrumentIdentification7Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Swp', type=SwapLegIdentification2, min=0, max=1, mutex_group=1, array=False),
	))