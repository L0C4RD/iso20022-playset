from . import base_types
from .AcceptedStatus13Choice import AcceptedStatus13Choice
from .Quantity54Choice import Quantity54Choice

class AcceptedStatus3(base_types._BaseFieldType):

	__slots__ = ["_AccptdQty", "_AccptdRsn"]
	@property
	def AccptdQty(self):
		return self._AccptdQty

	@AccptdQty.setter
	def AccptdQty(self, value):
		self._AccptdQty = value if type(value) != auto else self.make_default("AccptdQty")

	@AccptdQty.deleter
	def AccptdQty(self):
		del self._AccptdQty
		self._AccptdQty = None

	@property
	def AccptdRsn(self):
		return self._AccptdRsn

	@AccptdRsn.setter
	def AccptdRsn(self, value):
		self._AccptdRsn = value if type(value) != auto else self.make_default("AccptdRsn")

	@AccptdRsn.deleter
	def AccptdRsn(self):
		del self._AccptdRsn
		self._AccptdRsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AccptdQty', type=Quantity54Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AccptdRsn', type=AcceptedStatus13Choice, min=1, max=1, mutex_group=None, array=False),
	))

