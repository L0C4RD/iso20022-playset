# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrumentQuantity1

class OpeningBalance3Choice(base_types._BaseFieldType):

	__slots__ = ["_FrstOpngBal", "_IntrmyOpngBal"]
	@property
	def FrstOpngBal(self):
		return self._FrstOpngBal

	@FrstOpngBal.setter
	def FrstOpngBal(self, value):
		self._FrstOpngBal = value if value is not None else base_types.UninitialisedField(self, 'FrstOpngBal', FinancialInstrumentQuantity1, False)

	@FrstOpngBal.deleter
	def FrstOpngBal(self):
		del self._FrstOpngBal
		self._FrstOpngBal = base_types.UninitialisedField(self, 'FrstOpngBal', FinancialInstrumentQuantity1, False)

	@property
	def IntrmyOpngBal(self):
		return self._IntrmyOpngBal

	@IntrmyOpngBal.setter
	def IntrmyOpngBal(self, value):
		self._IntrmyOpngBal = value if value is not None else base_types.UninitialisedField(self, 'IntrmyOpngBal', FinancialInstrumentQuantity1, False)

	@IntrmyOpngBal.deleter
	def IntrmyOpngBal(self):
		del self._IntrmyOpngBal
		self._IntrmyOpngBal = base_types.UninitialisedField(self, 'IntrmyOpngBal', FinancialInstrumentQuantity1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FrstOpngBal', type=FinancialInstrumentQuantity1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IntrmyOpngBal', type=FinancialInstrumentQuantity1, min=0, max=1, mutex_group=1, array=False),
	))