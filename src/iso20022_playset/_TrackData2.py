from . import base_types
from ._Max140Text import Max140Text
from ._Number import Number
from ._TrackFormat1Code import TrackFormat1Code

class TrackData2(base_types._BaseFieldType):

	__slots__ = ["_TrckVal", "_TrckNb", "_TrckFrmt"]
	@property
	def TrckVal(self):
		return self._TrckVal

	@TrckVal.setter
	def TrckVal(self, value):
		self._TrckVal = value if type(value) != base_types.auto else self.make_default("TrckVal")

	@TrckVal.deleter
	def TrckVal(self):
		del self._TrckVal
		self._TrckVal = None

	@property
	def TrckNb(self):
		return self._TrckNb

	@TrckNb.setter
	def TrckNb(self, value):
		self._TrckNb = value if type(value) != base_types.auto else self.make_default("TrckNb")

	@TrckNb.deleter
	def TrckNb(self):
		del self._TrckNb
		self._TrckNb = None

	@property
	def TrckFrmt(self):
		return self._TrckFrmt

	@TrckFrmt.setter
	def TrckFrmt(self, value):
		self._TrckFrmt = value if type(value) != base_types.auto else self.make_default("TrckFrmt")

	@TrckFrmt.deleter
	def TrckFrmt(self):
		del self._TrckFrmt
		self._TrckFrmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TrckVal', type=Max140Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrckNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrckFrmt', type=TrackFormat1Code, min=0, max=1, mutex_group=None, array=False),
	))

