# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._BalanceQuantity14Choice import BalanceQuantity14Choice

class ClosingBalance6Choice(base_types._BaseFieldType):

	__slots__ = ["_Fnl", "_Intrmy"]
	@property
	def Fnl(self):
		return self._Fnl

	@Fnl.setter
	def Fnl(self, value):
		self._Fnl = value if type(value) != base_types.auto else self.make_default("Fnl")

	@Fnl.deleter
	def Fnl(self):
		del self._Fnl
		self._Fnl = None

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
		base_types.FieldEntry(name='Fnl', type=BalanceQuantity14Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Intrmy', type=BalanceQuantity14Choice, min=0, max=1, mutex_group=1, array=False),
	))