# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SubBalanceQuantity5Choice
from . import SubBalanceType9Choice

class SubBalanceBreakdown1(base_types._BaseFieldType):

	__slots__ = ["_Qty", "_SubBalTp"]
	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if value is not None else base_types.UninitialisedField(self, 'Qty', SubBalanceQuantity5Choice, False)

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = base_types.UninitialisedField(self, 'Qty', SubBalanceQuantity5Choice, False)

	@property
	def SubBalTp(self):
		return self._SubBalTp

	@SubBalTp.setter
	def SubBalTp(self, value):
		self._SubBalTp = value if value is not None else base_types.UninitialisedField(self, 'SubBalTp', SubBalanceType9Choice, False)

	@SubBalTp.deleter
	def SubBalTp(self):
		del self._SubBalTp
		self._SubBalTp = base_types.UninitialisedField(self, 'SubBalTp', SubBalanceType9Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Qty', type=SubBalanceQuantity5Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubBalTp', type=SubBalanceType9Choice, min=1, max=1, mutex_group=None, array=False),
	))