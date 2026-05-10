from . import base_types
from .SubBalanceQuantity5Choice import SubBalanceQuantity5Choice
from .SubBalanceType9Choice import SubBalanceType9Choice

class SubBalanceBreakdown1(base_types._BaseFieldType):

	__slots__ = ["_SubBalTp", "_Qty"]
	@property
	def SubBalTp(self):
		return self._SubBalTp

	@SubBalTp.setter
	def SubBalTp(self, value):
		self._SubBalTp = value if type(value) != base_types.auto else self.make_default("SubBalTp")

	@SubBalTp.deleter
	def SubBalTp(self):
		del self._SubBalTp
		self._SubBalTp = None

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
		base_types.FieldEntry(name='SubBalTp', type=SubBalanceType9Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=SubBalanceQuantity5Choice, min=1, max=1, mutex_group=None, array=False),
	))

