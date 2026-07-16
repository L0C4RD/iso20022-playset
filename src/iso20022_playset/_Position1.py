# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAnd24Amount
from . import ActiveCurrencyAndAmount
from . import AmountAndDirection102
from . import EndOfDayRequirement1
from . import Fraction5DecimalNumber
from . import Max256Text
from . import NonNegativeFraction5DecimalNumber

class Position1(base_types._BaseFieldType):

	__slots__ = ["_GrssDltaEqvtQty", "_GrssDltaEqvtVal", "_GrssMktVal", "_GrssNtnl", "_NetDltaEqvtQty", "_NetDltaEqvtVal", "_NetNtnl", "_PdctId", "_RskRqrmnt"]
	@property
	def GrssDltaEqvtQty(self):
		return self._GrssDltaEqvtQty

	@GrssDltaEqvtQty.setter
	def GrssDltaEqvtQty(self, value):
		self._GrssDltaEqvtQty = value if value is not None else base_types.UninitialisedField(self, 'GrssDltaEqvtQty', NonNegativeFraction5DecimalNumber, False)

	@GrssDltaEqvtQty.deleter
	def GrssDltaEqvtQty(self):
		del self._GrssDltaEqvtQty
		self._GrssDltaEqvtQty = base_types.UninitialisedField(self, 'GrssDltaEqvtQty', NonNegativeFraction5DecimalNumber, False)

	@property
	def GrssDltaEqvtVal(self):
		return self._GrssDltaEqvtVal

	@GrssDltaEqvtVal.setter
	def GrssDltaEqvtVal(self, value):
		self._GrssDltaEqvtVal = value if value is not None else base_types.UninitialisedField(self, 'GrssDltaEqvtVal', ActiveCurrencyAndAmount, False)

	@GrssDltaEqvtVal.deleter
	def GrssDltaEqvtVal(self):
		del self._GrssDltaEqvtVal
		self._GrssDltaEqvtVal = base_types.UninitialisedField(self, 'GrssDltaEqvtVal', ActiveCurrencyAndAmount, False)

	@property
	def GrssMktVal(self):
		return self._GrssMktVal

	@GrssMktVal.setter
	def GrssMktVal(self, value):
		self._GrssMktVal = value if value is not None else base_types.UninitialisedField(self, 'GrssMktVal', ActiveCurrencyAndAmount, False)

	@GrssMktVal.deleter
	def GrssMktVal(self):
		del self._GrssMktVal
		self._GrssMktVal = base_types.UninitialisedField(self, 'GrssMktVal', ActiveCurrencyAndAmount, False)

	@property
	def GrssNtnl(self):
		return self._GrssNtnl

	@GrssNtnl.setter
	def GrssNtnl(self, value):
		self._GrssNtnl = value if value is not None else base_types.UninitialisedField(self, 'GrssNtnl', ActiveCurrencyAnd24Amount, False)

	@GrssNtnl.deleter
	def GrssNtnl(self):
		del self._GrssNtnl
		self._GrssNtnl = base_types.UninitialisedField(self, 'GrssNtnl', ActiveCurrencyAnd24Amount, False)

	@property
	def NetDltaEqvtQty(self):
		return self._NetDltaEqvtQty

	@NetDltaEqvtQty.setter
	def NetDltaEqvtQty(self, value):
		self._NetDltaEqvtQty = value if value is not None else base_types.UninitialisedField(self, 'NetDltaEqvtQty', Fraction5DecimalNumber, False)

	@NetDltaEqvtQty.deleter
	def NetDltaEqvtQty(self):
		del self._NetDltaEqvtQty
		self._NetDltaEqvtQty = base_types.UninitialisedField(self, 'NetDltaEqvtQty', Fraction5DecimalNumber, False)

	@property
	def NetDltaEqvtVal(self):
		return self._NetDltaEqvtVal

	@NetDltaEqvtVal.setter
	def NetDltaEqvtVal(self, value):
		self._NetDltaEqvtVal = value if value is not None else base_types.UninitialisedField(self, 'NetDltaEqvtVal', AmountAndDirection102, False)

	@NetDltaEqvtVal.deleter
	def NetDltaEqvtVal(self):
		del self._NetDltaEqvtVal
		self._NetDltaEqvtVal = base_types.UninitialisedField(self, 'NetDltaEqvtVal', AmountAndDirection102, False)

	@property
	def NetNtnl(self):
		return self._NetNtnl

	@NetNtnl.setter
	def NetNtnl(self, value):
		self._NetNtnl = value if value is not None else base_types.UninitialisedField(self, 'NetNtnl', AmountAndDirection102, False)

	@NetNtnl.deleter
	def NetNtnl(self):
		del self._NetNtnl
		self._NetNtnl = base_types.UninitialisedField(self, 'NetNtnl', AmountAndDirection102, False)

	@property
	def PdctId(self):
		return self._PdctId

	@PdctId.setter
	def PdctId(self, value):
		self._PdctId = value if value is not None else base_types.UninitialisedField(self, 'PdctId', Max256Text, False)

	@PdctId.deleter
	def PdctId(self):
		del self._PdctId
		self._PdctId = base_types.UninitialisedField(self, 'PdctId', Max256Text, False)

	@property
	def RskRqrmnt(self):
		return self._RskRqrmnt

	@RskRqrmnt.setter
	def RskRqrmnt(self, value):
		self._RskRqrmnt = value if value is not None else base_types.UninitialisedField(self, 'RskRqrmnt', EndOfDayRequirement1, False)

	@RskRqrmnt.deleter
	def RskRqrmnt(self):
		del self._RskRqrmnt
		self._RskRqrmnt = base_types.UninitialisedField(self, 'RskRqrmnt', EndOfDayRequirement1, False)

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