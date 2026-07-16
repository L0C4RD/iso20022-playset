# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max4AlphaNumericText
from . import SubBalanceQuantity2Choice

class SecuritiesPosition1(base_types._BaseFieldType):

	__slots__ = ["_Qty", "_Tp"]
	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if value is not None else base_types.UninitialisedField(self, 'Qty', SubBalanceQuantity2Choice, False)

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = base_types.UninitialisedField(self, 'Qty', SubBalanceQuantity2Choice, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', Max4AlphaNumericText, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', Max4AlphaNumericText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Qty', type=SubBalanceQuantity2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=Max4AlphaNumericText, min=1, max=1, mutex_group=None, array=False),
	))