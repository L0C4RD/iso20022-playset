# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BalanceQuantity17Choice

class OpeningBalance7Choice(base_types._BaseFieldType):

	__slots__ = ["_Frst", "_Intrmy"]
	@property
	def Frst(self):
		return self._Frst

	@Frst.setter
	def Frst(self, value):
		self._Frst = value if value is not None else base_types.UninitialisedField(self, 'Frst', BalanceQuantity17Choice, False)

	@Frst.deleter
	def Frst(self):
		del self._Frst
		self._Frst = base_types.UninitialisedField(self, 'Frst', BalanceQuantity17Choice, False)

	@property
	def Intrmy(self):
		return self._Intrmy

	@Intrmy.setter
	def Intrmy(self, value):
		self._Intrmy = value if value is not None else base_types.UninitialisedField(self, 'Intrmy', BalanceQuantity17Choice, False)

	@Intrmy.deleter
	def Intrmy(self):
		del self._Intrmy
		self._Intrmy = base_types.UninitialisedField(self, 'Intrmy', BalanceQuantity17Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Frst', type=BalanceQuantity17Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Intrmy', type=BalanceQuantity17Choice, min=0, max=1, mutex_group=1, array=False),
	))