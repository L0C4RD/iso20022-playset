from . import base_types
from ._ShortLong1Code import ShortLong1Code
from ._Quantity48Choice import Quantity48Choice

class SignedQuantityFormat11(base_types._BaseFieldType):

	__slots__ = ["_QtyChc", "_ShrtLngPos"]
	@property
	def QtyChc(self):
		return self._QtyChc

	@QtyChc.setter
	def QtyChc(self, value):
		self._QtyChc = value if type(value) != base_types.auto else self.make_default("QtyChc")

	@QtyChc.deleter
	def QtyChc(self):
		del self._QtyChc
		self._QtyChc = None

	@property
	def ShrtLngPos(self):
		return self._ShrtLngPos

	@ShrtLngPos.setter
	def ShrtLngPos(self, value):
		self._ShrtLngPos = value if type(value) != base_types.auto else self.make_default("ShrtLngPos")

	@ShrtLngPos.deleter
	def ShrtLngPos(self):
		del self._ShrtLngPos
		self._ShrtLngPos = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='QtyChc', type=Quantity48Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrtLngPos', type=ShortLong1Code, min=1, max=1, mutex_group=None, array=False),
	))

