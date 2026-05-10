from . import base_types
from ._Max35Text import Max35Text
from ._OrderStatus3Choice import OrderStatus3Choice
from ._PartyIdentification113 import PartyIdentification113

class OrderStatusAndReason10(base_types._BaseFieldType):

	__slots__ = ["_MstrRef", "_OrdrSts", "_StsInitr"]
	@property
	def MstrRef(self):
		return self._MstrRef

	@MstrRef.setter
	def MstrRef(self, value):
		self._MstrRef = value if type(value) != base_types.auto else self.make_default("MstrRef")

	@MstrRef.deleter
	def MstrRef(self):
		del self._MstrRef
		self._MstrRef = None

	@property
	def OrdrSts(self):
		return self._OrdrSts

	@OrdrSts.setter
	def OrdrSts(self, value):
		self._OrdrSts = value if type(value) != base_types.auto else self.make_default("OrdrSts")

	@OrdrSts.deleter
	def OrdrSts(self):
		del self._OrdrSts
		self._OrdrSts = None

	@property
	def StsInitr(self):
		return self._StsInitr

	@StsInitr.setter
	def StsInitr(self, value):
		self._StsInitr = value if type(value) != base_types.auto else self.make_default("StsInitr")

	@StsInitr.deleter
	def StsInitr(self):
		del self._StsInitr
		self._StsInitr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MstrRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrSts', type=OrderStatus3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsInitr', type=PartyIdentification113, min=0, max=1, mutex_group=None, array=False),
	))

