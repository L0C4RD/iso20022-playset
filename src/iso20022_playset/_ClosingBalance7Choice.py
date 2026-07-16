# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BalanceQuantity17Choice

class ClosingBalance7Choice(base_types._BaseFieldType):

	__slots__ = ["_Fnl", "_Intrmy"]
	@property
	def Fnl(self):
		return self._Fnl

	@Fnl.setter
	def Fnl(self, value):
		self._Fnl = value if value is not None else base_types.UninitialisedField(self, 'Fnl', BalanceQuantity17Choice, False)

	@Fnl.deleter
	def Fnl(self):
		del self._Fnl
		self._Fnl = base_types.UninitialisedField(self, 'Fnl', BalanceQuantity17Choice, False)

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
		base_types.FieldEntry(name='Fnl', type=BalanceQuantity17Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Intrmy', type=BalanceQuantity17Choice, min=0, max=1, mutex_group=1, array=False),
	))