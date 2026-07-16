# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Balance9
from . import Max140Text
from . import QuantityBreakdown54
from . import SubBalanceType12Choice

class AdditionalBalanceBreakdown1(base_types._BaseFieldType):

	__slots__ = ["_Qty", "_QtyBrkdwn", "_SubBalAddtlDtls", "_SubBalTp"]
	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if value is not None else base_types.UninitialisedField(self, 'Qty', Balance9, False)

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = base_types.UninitialisedField(self, 'Qty', Balance9, False)

	@property
	def QtyBrkdwn(self):
		return self._QtyBrkdwn

	@QtyBrkdwn.setter
	def QtyBrkdwn(self, value):
		self._QtyBrkdwn = value if value is not None else base_types.UninitialisedField(self, 'QtyBrkdwn', QuantityBreakdown54, True)

	@QtyBrkdwn.deleter
	def QtyBrkdwn(self):
		del self._QtyBrkdwn
		self._QtyBrkdwn = base_types.UninitialisedField(self, 'QtyBrkdwn', QuantityBreakdown54, True)

	@property
	def SubBalAddtlDtls(self):
		return self._SubBalAddtlDtls

	@SubBalAddtlDtls.setter
	def SubBalAddtlDtls(self, value):
		self._SubBalAddtlDtls = value if value is not None else base_types.UninitialisedField(self, 'SubBalAddtlDtls', Max140Text, False)

	@SubBalAddtlDtls.deleter
	def SubBalAddtlDtls(self):
		del self._SubBalAddtlDtls
		self._SubBalAddtlDtls = base_types.UninitialisedField(self, 'SubBalAddtlDtls', Max140Text, False)

	@property
	def SubBalTp(self):
		return self._SubBalTp

	@SubBalTp.setter
	def SubBalTp(self, value):
		self._SubBalTp = value if value is not None else base_types.UninitialisedField(self, 'SubBalTp', SubBalanceType12Choice, False)

	@SubBalTp.deleter
	def SubBalTp(self):
		del self._SubBalTp
		self._SubBalTp = base_types.UninitialisedField(self, 'SubBalTp', SubBalanceType12Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Qty', type=Balance9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtyBrkdwn', type=QuantityBreakdown54, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SubBalAddtlDtls', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubBalTp', type=SubBalanceType12Choice, min=1, max=1, mutex_group=None, array=False),
	))