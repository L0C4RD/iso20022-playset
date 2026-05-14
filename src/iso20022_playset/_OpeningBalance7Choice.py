# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._BalanceQuantity17Choice import BalanceQuantity17Choice

class OpeningBalance7Choice(base_types._BaseFieldType):

	__slots__ = ["_Frst", "_Intrmy"]
	@property
	def Frst(self):
		return self._Frst

	@Frst.setter
	def Frst(self, value):
		self._Frst = value if type(value) != base_types.auto else self.make_default("Frst")

	@Frst.deleter
	def Frst(self):
		del self._Frst
		self._Frst = None

	@property
	def Intrmy(self):
		return self._Intrmy

	@Intrmy.setter
	def Intrmy(self, value):
		self._Intrmy = value if type(value) != base_types.auto else self.make_default("Intrmy")

	@Intrmy.deleter
	def Intrmy(self):
		del self._Intrmy
		self._Intrmy = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Frst', type=BalanceQuantity17Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Intrmy', type=BalanceQuantity17Choice, min=0, max=1, mutex_group=1, array=False),
	))