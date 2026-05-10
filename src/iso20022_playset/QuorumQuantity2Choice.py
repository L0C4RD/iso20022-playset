from . import base_types
from .Max35Text import Max35Text
from .Percentage14Rate import Percentage14Rate

class QuorumQuantity2Choice(base_types._BaseFieldType):

	__slots__ = ["_QrmQtyPctg", "_QrmQty"]
	@property
	def QrmQtyPctg(self):
		return self._QrmQtyPctg

	@QrmQtyPctg.setter
	def QrmQtyPctg(self, value):
		self._QrmQtyPctg = value if type(value) != auto else self.make_default("QrmQtyPctg")

	@QrmQtyPctg.deleter
	def QrmQtyPctg(self):
		del self._QrmQtyPctg
		self._QrmQtyPctg = None

	@property
	def QrmQty(self):
		return self._QrmQty

	@QrmQty.setter
	def QrmQty(self, value):
		self._QrmQty = value if type(value) != auto else self.make_default("QrmQty")

	@QrmQty.deleter
	def QrmQty(self):
		del self._QrmQty
		self._QrmQty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='QrmQtyPctg', type=Percentage14Rate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='QrmQty', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
	))

