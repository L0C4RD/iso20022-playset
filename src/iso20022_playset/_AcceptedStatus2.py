from . import base_types
from ._Quantity51Choice import Quantity51Choice
from ._AcceptedStatus8Choice import AcceptedStatus8Choice

class AcceptedStatus2(base_types._BaseFieldType):

	__slots__ = ["_AccptdQty", "_AccptdRsn"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='AccptdQty', type=Quantity51Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AccptdRsn', type=AcceptedStatus8Choice, min=1, max=1, mutex_group=None, array=False),
	))

