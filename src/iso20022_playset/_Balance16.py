from . import base_types
from ._BalanceQuantity13Choice import BalanceQuantity13Choice
from ._ShortLong1Code import ShortLong1Code

class Balance16(base_types._BaseFieldType):

	__slots__ = ["_ShrtLngInd", "_Qty"]
	@property
	def ShrtLngInd(self):
		return self._ShrtLngInd

	@ShrtLngInd.setter
	def ShrtLngInd(self, value):
		self._ShrtLngInd = value if type(value) != base_types.auto else self.make_default("ShrtLngInd")

	@ShrtLngInd.deleter
	def ShrtLngInd(self):
		del self._ShrtLngInd
		self._ShrtLngInd = None

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if type(value) != base_types.auto else self.make_default("Qty")

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ShrtLngInd', type=ShortLong1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=BalanceQuantity13Choice, min=1, max=1, mutex_group=None, array=False),
	))

