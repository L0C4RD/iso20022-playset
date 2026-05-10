from . import base_types
from ._Quantity54Choice import Quantity54Choice
from ._AcceptedStatus13Choice import AcceptedStatus13Choice

class AcceptedStatus3(base_types._BaseFieldType):

	__slots__ = ["_AccptdRsn", "_AccptdQty"]
	@property
	def AccptdRsn(self):
		return self._AccptdRsn

	@AccptdRsn.setter
	def AccptdRsn(self, value):
		self._AccptdRsn = value if type(value) != base_types.auto else self.make_default("AccptdRsn")

	@AccptdRsn.deleter
	def AccptdRsn(self):
		del self._AccptdRsn
		self._AccptdRsn = None

	@property
	def AccptdQty(self):
		return self._AccptdQty

	@AccptdQty.setter
	def AccptdQty(self, value):
		self._AccptdQty = value if type(value) != base_types.auto else self.make_default("AccptdQty")

	@AccptdQty.deleter
	def AccptdQty(self):
		del self._AccptdQty
		self._AccptdQty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AccptdRsn', type=AcceptedStatus13Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AccptdQty', type=Quantity54Choice, min=0, max=1, mutex_group=None, array=False),
	))

