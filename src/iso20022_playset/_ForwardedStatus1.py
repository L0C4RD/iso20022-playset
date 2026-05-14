from . import base_types
from ._NoSpecifiedReason1 import NoSpecifiedReason1
from ._Quantity51Choice import Quantity51Choice

class ForwardedStatus1(base_types._BaseFieldType):

	__slots__ = ["_FwddQty", "_FwddRsn"]
	@property
	def FwddQty(self):
		return self._FwddQty

	@FwddQty.setter
	def FwddQty(self, value):
		self._FwddQty = value if type(value) != base_types.auto else self.make_default("FwddQty")

	@FwddQty.deleter
	def FwddQty(self):
		del self._FwddQty
		self._FwddQty = None

	@property
	def FwddRsn(self):
		return self._FwddRsn

	@FwddRsn.setter
	def FwddRsn(self, value):
		self._FwddRsn = value if type(value) != base_types.auto else self.make_default("FwddRsn")

	@FwddRsn.deleter
	def FwddRsn(self):
		del self._FwddRsn
		self._FwddRsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FwddQty', type=Quantity51Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FwddRsn', type=NoSpecifiedReason1, min=1, max=1, mutex_group=None, array=False),
	))

