# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PercentageRate
from . import SecuritiesTransactionPrice18Choice

class Rates3(base_types._BaseFieldType):

	__slots__ = ["_BuySellBck", "_Fltg", "_Fxd"]
	@property
	def BuySellBck(self):
		return self._BuySellBck

	@BuySellBck.setter
	def BuySellBck(self, value):
		self._BuySellBck = value if value is not None else base_types.UninitialisedField(self, 'BuySellBck', SecuritiesTransactionPrice18Choice, False)

	@BuySellBck.deleter
	def BuySellBck(self):
		del self._BuySellBck
		self._BuySellBck = base_types.UninitialisedField(self, 'BuySellBck', SecuritiesTransactionPrice18Choice, False)

	@property
	def Fltg(self):
		return self._Fltg

	@Fltg.setter
	def Fltg(self, value):
		self._Fltg = value if value is not None else base_types.UninitialisedField(self, 'Fltg', PercentageRate, False)

	@Fltg.deleter
	def Fltg(self):
		del self._Fltg
		self._Fltg = base_types.UninitialisedField(self, 'Fltg', PercentageRate, False)

	@property
	def Fxd(self):
		return self._Fxd

	@Fxd.setter
	def Fxd(self, value):
		self._Fxd = value if value is not None else base_types.UninitialisedField(self, 'Fxd', PercentageRate, False)

	@Fxd.deleter
	def Fxd(self):
		del self._Fxd
		self._Fxd = base_types.UninitialisedField(self, 'Fxd', PercentageRate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BuySellBck', type=SecuritiesTransactionPrice18Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Fltg', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Fxd', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
	))