from . import base_types
from ._ActiveCurrencyAnd24Amount import ActiveCurrencyAnd24Amount
from ._AmountAndDirection102 import AmountAndDirection102
from ._EndOfDayRequirement1 import EndOfDayRequirement1
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._Fraction5DecimalNumber import Fraction5DecimalNumber
from ._NonNegativeFraction5DecimalNumber import NonNegativeFraction5DecimalNumber
from ._Max256Text import Max256Text

class Position1(base_types._BaseFieldType):

	__slots__ = ["_NetDltaEqvtVal", "_GrssDltaEqvtQty", "_GrssMktVal", "_RskRqrmnt", "_GrssNtnl", "_PdctId", "_GrssDltaEqvtVal", "_NetDltaEqvtQty", "_NetNtnl"]
	@property
	def GrssDltaEqvtQty(self):
		return self._GrssDltaEqvtQty

	@GrssDltaEqvtQty.setter
	def GrssDltaEqvtQty(self, value):
		self._GrssDltaEqvtQty = value if type(value) != base_types.auto else self.make_default("GrssDltaEqvtQty")

	@GrssDltaEqvtQty.deleter
	def GrssDltaEqvtQty(self):
		del self._GrssDltaEqvtQty
		self._GrssDltaEqvtQty = None

	@property
	def GrssDltaEqvtVal(self):
		return self._GrssDltaEqvtVal

	@GrssDltaEqvtVal.setter
	def GrssDltaEqvtVal(self, value):
		self._GrssDltaEqvtVal = value if type(value) != base_types.auto else self.make_default("GrssDltaEqvtVal")

	@GrssDltaEqvtVal.deleter
	def GrssDltaEqvtVal(self):
		del self._GrssDltaEqvtVal
		self._GrssDltaEqvtVal = None

	@property
	def GrssMktVal(self):
		return self._GrssMktVal

	@GrssMktVal.setter
	def GrssMktVal(self, value):
		self._GrssMktVal = value if type(value) != base_types.auto else self.make_default("GrssMktVal")

	@GrssMktVal.deleter
	def GrssMktVal(self):
		del self._GrssMktVal
		self._GrssMktVal = None

	@property
	def GrssNtnl(self):
		return self._GrssNtnl

	@GrssNtnl.setter
	def GrssNtnl(self, value):
		self._GrssNtnl = value if type(value) != base_types.auto else self.make_default("GrssNtnl")

	@GrssNtnl.deleter
	def GrssNtnl(self):
		del self._GrssNtnl
		self._GrssNtnl = None

	@property
	def NetDltaEqvtQty(self):
		return self._NetDltaEqvtQty

	@NetDltaEqvtQty.setter
	def NetDltaEqvtQty(self, value):
		self._NetDltaEqvtQty = value if type(value) != base_types.auto else self.make_default("NetDltaEqvtQty")

	@NetDltaEqvtQty.deleter
	def NetDltaEqvtQty(self):
		del self._NetDltaEqvtQty
		self._NetDltaEqvtQty = None

	@property
	def NetDltaEqvtVal(self):
		return self._NetDltaEqvtVal

	@NetDltaEqvtVal.setter
	def NetDltaEqvtVal(self, value):
		self._NetDltaEqvtVal = value if type(value) != base_types.auto else self.make_default("NetDltaEqvtVal")

	@NetDltaEqvtVal.deleter
	def NetDltaEqvtVal(self):
		del self._NetDltaEqvtVal
		self._NetDltaEqvtVal = None

	@property
	def NetNtnl(self):
		return self._NetNtnl

	@NetNtnl.setter
	def NetNtnl(self, value):
		self._NetNtnl = value if type(value) != base_types.auto else self.make_default("NetNtnl")

	@NetNtnl.deleter
	def NetNtnl(self):
		del self._NetNtnl
		self._NetNtnl = None

	@property
	def PdctId(self):
		return self._PdctId

	@PdctId.setter
	def PdctId(self, value):
		self._PdctId = value if type(value) != base_types.auto else self.make_default("PdctId")

	@PdctId.deleter
	def PdctId(self):
		del self._PdctId
		self._PdctId = None

	@property
	def RskRqrmnt(self):
		return self._RskRqrmnt

	@RskRqrmnt.setter
	def RskRqrmnt(self, value):
		self._RskRqrmnt = value if type(value) != base_types.auto else self.make_default("RskRqrmnt")

	@RskRqrmnt.deleter
	def RskRqrmnt(self):
		del self._RskRqrmnt
		self._RskRqrmnt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='GrssDltaEqvtQty', type=NonNegativeFraction5DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrssDltaEqvtVal', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrssMktVal', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrssNtnl', type=ActiveCurrencyAnd24Amount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetDltaEqvtQty', type=Fraction5DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetDltaEqvtVal', type=AmountAndDirection102, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetNtnl', type=AmountAndDirection102, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctId', type=Max256Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RskRqrmnt', type=EndOfDayRequirement1, min=0, max=1, mutex_group=None, array=False),
	))

