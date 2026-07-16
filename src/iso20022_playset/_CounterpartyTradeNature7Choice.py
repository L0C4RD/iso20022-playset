# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialPartyClassification1
from . import FinancialPartyClassification2

class CounterpartyTradeNature7Choice(base_types._BaseFieldType):

	__slots__ = ["_FI", "_NFI"]
	@property
	def FI(self):
		return self._FI

	@FI.setter
	def FI(self, value):
		self._FI = value if value is not None else base_types.UninitialisedField(self, 'FI', FinancialPartyClassification1, False)

	@FI.deleter
	def FI(self):
		del self._FI
		self._FI = base_types.UninitialisedField(self, 'FI', FinancialPartyClassification1, False)

	@property
	def NFI(self):
		return self._NFI

	@NFI.setter
	def NFI(self, value):
		self._NFI = value if value is not None else base_types.UninitialisedField(self, 'NFI', FinancialPartyClassification2, True)

	@NFI.deleter
	def NFI(self):
		del self._NFI
		self._NFI = base_types.UninitialisedField(self, 'NFI', FinancialPartyClassification2, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FI', type=FinancialPartyClassification1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NFI', type=FinancialPartyClassification2, min=1, max=None, mutex_group=1, array=True),
	))