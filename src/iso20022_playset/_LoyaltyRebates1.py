# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ImpliedCurrencyAndAmount
from . import Max35Text
from . import SaleItemRebate1

class LoyaltyRebates1(base_types._BaseFieldType):

	__slots__ = ["_RbtLabl", "_SaleItmRbt", "_TtlRbt"]
	@property
	def RbtLabl(self):
		return self._RbtLabl

	@RbtLabl.setter
	def RbtLabl(self, value):
		self._RbtLabl = value if value is not None else base_types.UninitialisedField(self, 'RbtLabl', Max35Text, False)

	@RbtLabl.deleter
	def RbtLabl(self):
		del self._RbtLabl
		self._RbtLabl = base_types.UninitialisedField(self, 'RbtLabl', Max35Text, False)

	@property
	def SaleItmRbt(self):
		return self._SaleItmRbt

	@SaleItmRbt.setter
	def SaleItmRbt(self, value):
		self._SaleItmRbt = value if value is not None else base_types.UninitialisedField(self, 'SaleItmRbt', SaleItemRebate1, True)

	@SaleItmRbt.deleter
	def SaleItmRbt(self):
		del self._SaleItmRbt
		self._SaleItmRbt = base_types.UninitialisedField(self, 'SaleItmRbt', SaleItemRebate1, True)

	@property
	def TtlRbt(self):
		return self._TtlRbt

	@TtlRbt.setter
	def TtlRbt(self, value):
		self._TtlRbt = value if value is not None else base_types.UninitialisedField(self, 'TtlRbt', ImpliedCurrencyAndAmount, False)

	@TtlRbt.deleter
	def TtlRbt(self):
		del self._TtlRbt
		self._TtlRbt = base_types.UninitialisedField(self, 'TtlRbt', ImpliedCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='RbtLabl', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleItmRbt', type=SaleItemRebate1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlRbt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))