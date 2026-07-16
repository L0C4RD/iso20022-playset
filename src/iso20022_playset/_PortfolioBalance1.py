# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BalanceDetails5
from . import BalanceDetails6

class PortfolioBalance1(base_types._BaseFieldType):

	__slots__ = ["_DtldBal", "_SummryBal"]
	@property
	def DtldBal(self):
		return self._DtldBal

	@DtldBal.setter
	def DtldBal(self, value):
		self._DtldBal = value if value is not None else base_types.UninitialisedField(self, 'DtldBal', BalanceDetails6, True)

	@DtldBal.deleter
	def DtldBal(self):
		del self._DtldBal
		self._DtldBal = base_types.UninitialisedField(self, 'DtldBal', BalanceDetails6, True)

	@property
	def SummryBal(self):
		return self._SummryBal

	@SummryBal.setter
	def SummryBal(self, value):
		self._SummryBal = value if value is not None else base_types.UninitialisedField(self, 'SummryBal', BalanceDetails5, True)

	@SummryBal.deleter
	def SummryBal(self):
		del self._SummryBal
		self._SummryBal = base_types.UninitialisedField(self, 'SummryBal', BalanceDetails5, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DtldBal', type=BalanceDetails6, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='SummryBal', type=BalanceDetails5, min=1, max=None, mutex_group=1, array=True),
	))