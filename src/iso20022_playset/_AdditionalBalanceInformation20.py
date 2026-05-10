from . import base_types
from ._Max140Text import Max140Text
from ._Balance21 import Balance21
from ._QuantityBreakdown57 import QuantityBreakdown57
from ._SubBalanceType12Choice import SubBalanceType12Choice

class AdditionalBalanceInformation20(base_types._BaseFieldType):

	__slots__ = ["_SubBalTp", "_SubBalAddtlDtls", "_Qty", "_QtyBrkdwn"]
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
	def SubBalAddtlDtls(self):
		return self._SubBalAddtlDtls

	@SubBalAddtlDtls.setter
	def SubBalAddtlDtls(self, value):
		self._SubBalAddtlDtls = value if type(value) != base_types.auto else self.make_default("SubBalAddtlDtls")

	@SubBalAddtlDtls.deleter
	def SubBalAddtlDtls(self):
		del self._SubBalAddtlDtls
		self._SubBalAddtlDtls = None

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

	@property
	def QtyBrkdwn(self):
		return self._QtyBrkdwn

	@QtyBrkdwn.setter
	def QtyBrkdwn(self, value):
		self._QtyBrkdwn = value if type(value) != base_types.auto else self.make_default("QtyBrkdwn")

	@QtyBrkdwn.deleter
	def QtyBrkdwn(self):
		del self._QtyBrkdwn
		self._QtyBrkdwn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SubBalTp', type=SubBalanceType12Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubBalAddtlDtls', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=Balance21, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtyBrkdwn', type=QuantityBreakdown57, min=0, max=None, mutex_group=None, array=True),
	))

