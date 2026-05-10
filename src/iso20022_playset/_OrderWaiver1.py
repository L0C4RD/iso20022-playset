from . import base_types
from ._OrderWaiverReason3Choice import OrderWaiverReason3Choice
from ._Max350Text import Max350Text

class OrderWaiver1(base_types._BaseFieldType):

	__slots__ = ["_InfVal", "_OrdrWvrRsn"]
	@property
	def InfVal(self):
		return self._InfVal

	@InfVal.setter
	def InfVal(self, value):
		self._InfVal = value if type(value) != base_types.auto else self.make_default("InfVal")

	@InfVal.deleter
	def InfVal(self):
		del self._InfVal
		self._InfVal = None

	@property
	def OrdrWvrRsn(self):
		return self._OrdrWvrRsn

	@OrdrWvrRsn.setter
	def OrdrWvrRsn(self, value):
		self._OrdrWvrRsn = value if type(value) != base_types.auto else self.make_default("OrdrWvrRsn")

	@OrdrWvrRsn.deleter
	def OrdrWvrRsn(self):
		del self._OrdrWvrRsn
		self._OrdrWvrRsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='InfVal', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrWvrRsn', type=OrderWaiverReason3Choice, min=0, max=None, mutex_group=None, array=True),
	))

