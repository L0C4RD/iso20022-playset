import base_types
import Max35Text
import ImpliedCurrencyAndAmount
import SaleItemRebate1

class LoyaltyRebates1(base_types._BaseFieldType):

	__slots__ = ["_TtlRbt", "_SaleItmRbt", "_RbtLabl"]
	@property
	def TtlRbt(self):
		return self._TtlRbt

	@TtlRbt.setter
	def TtlRbt(self, value):
		self._TtlRbt = value if type(value) != auto else self.make_default("TtlRbt")

	@TtlRbt.deleter
	def TtlRbt(self):
		del self._TtlRbt
		self._TtlRbt = None

	@property
	def SaleItmRbt(self):
		return self._SaleItmRbt

	@SaleItmRbt.setter
	def SaleItmRbt(self, value):
		self._SaleItmRbt = value if type(value) != auto else self.make_default("SaleItmRbt")

	@SaleItmRbt.deleter
	def SaleItmRbt(self):
		del self._SaleItmRbt
		self._SaleItmRbt = None

	@property
	def RbtLabl(self):
		return self._RbtLabl

	@RbtLabl.setter
	def RbtLabl(self, value):
		self._RbtLabl = value if type(value) != auto else self.make_default("RbtLabl")

	@RbtLabl.deleter
	def RbtLabl(self):
		del self._RbtLabl
		self._RbtLabl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TtlRbt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleItmRbt', type=SaleItemRebate1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RbtLabl', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

