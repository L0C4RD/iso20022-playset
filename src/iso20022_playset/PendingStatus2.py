from . import base_types
from .Quantity54Choice import Quantity54Choice
from .PendingStatus76Choice import PendingStatus76Choice

class PendingStatus2(base_types._BaseFieldType):

	__slots__ = ["_PdgRsn", "_PdgQty"]
	@property
	def PdgRsn(self):
		return self._PdgRsn

	@PdgRsn.setter
	def PdgRsn(self, value):
		self._PdgRsn = value if type(value) != auto else self.make_default("PdgRsn")

	@PdgRsn.deleter
	def PdgRsn(self):
		del self._PdgRsn
		self._PdgRsn = None

	@property
	def PdgQty(self):
		return self._PdgQty

	@PdgQty.setter
	def PdgQty(self, value):
		self._PdgQty = value if type(value) != auto else self.make_default("PdgQty")

	@PdgQty.deleter
	def PdgQty(self):
		del self._PdgQty
		self._PdgQty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PdgRsn', type=PendingStatus76Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdgQty', type=Quantity54Choice, min=0, max=1, mutex_group=None, array=False),
	))

