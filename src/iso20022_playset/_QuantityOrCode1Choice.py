# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrumentQuantity18Choice
from . import Quantity1Code

class QuantityOrCode1Choice(base_types._BaseFieldType):

	__slots__ = ["_Cd", "_Qty"]
	@property
	def Cd(self):
		return self._Cd

	@Cd.setter
	def Cd(self, value):
		self._Cd = value if value is not None else base_types.UninitialisedField(self, 'Cd', Quantity1Code, False)

	@Cd.deleter
	def Cd(self):
		del self._Cd
		self._Cd = base_types.UninitialisedField(self, 'Cd', Quantity1Code, False)

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if value is not None else base_types.UninitialisedField(self, 'Qty', FinancialInstrumentQuantity18Choice, False)

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = base_types.UninitialisedField(self, 'Qty', FinancialInstrumentQuantity18Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cd', type=Quantity1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Qty', type=FinancialInstrumentQuantity18Choice, min=0, max=1, mutex_group=1, array=False),
	))