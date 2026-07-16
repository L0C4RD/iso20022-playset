# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrumentQuantity1

class ClosingBalance3Choice(base_types._BaseFieldType):

	__slots__ = ["_FnlClsgBal", "_IntrmyClsgBal"]
	@property
	def FnlClsgBal(self):
		return self._FnlClsgBal

	@FnlClsgBal.setter
	def FnlClsgBal(self, value):
		self._FnlClsgBal = value if value is not None else base_types.UninitialisedField(self, 'FnlClsgBal', FinancialInstrumentQuantity1, False)

	@FnlClsgBal.deleter
	def FnlClsgBal(self):
		del self._FnlClsgBal
		self._FnlClsgBal = base_types.UninitialisedField(self, 'FnlClsgBal', FinancialInstrumentQuantity1, False)

	@property
	def IntrmyClsgBal(self):
		return self._IntrmyClsgBal

	@IntrmyClsgBal.setter
	def IntrmyClsgBal(self, value):
		self._IntrmyClsgBal = value if value is not None else base_types.UninitialisedField(self, 'IntrmyClsgBal', FinancialInstrumentQuantity1, False)

	@IntrmyClsgBal.deleter
	def IntrmyClsgBal(self):
		del self._IntrmyClsgBal
		self._IntrmyClsgBal = base_types.UninitialisedField(self, 'IntrmyClsgBal', FinancialInstrumentQuantity1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FnlClsgBal', type=FinancialInstrumentQuantity1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IntrmyClsgBal', type=FinancialInstrumentQuantity1, min=0, max=1, mutex_group=1, array=False),
	))