from . import base_types
from .ExternallyDefinedData5 import ExternallyDefinedData5
from .PositiveNumber import PositiveNumber
from .GenericIdentification176 import GenericIdentification176

class PackageType5(base_types._BaseFieldType):

	__slots__ = ["_PackgLngth", "_PackgId", "_OffsetEnd", "_PackgBlck", "_OffsetStart"]
	@property
	def PackgLngth(self):
		return self._PackgLngth

	@PackgLngth.setter
	def PackgLngth(self, value):
		self._PackgLngth = value if type(value) != auto else self.make_default("PackgLngth")

	@PackgLngth.deleter
	def PackgLngth(self):
		del self._PackgLngth
		self._PackgLngth = None

	@property
	def PackgId(self):
		return self._PackgId

	@PackgId.setter
	def PackgId(self, value):
		self._PackgId = value if type(value) != auto else self.make_default("PackgId")

	@PackgId.deleter
	def PackgId(self):
		del self._PackgId
		self._PackgId = None

	@property
	def OffsetEnd(self):
		return self._OffsetEnd

	@OffsetEnd.setter
	def OffsetEnd(self, value):
		self._OffsetEnd = value if type(value) != auto else self.make_default("OffsetEnd")

	@OffsetEnd.deleter
	def OffsetEnd(self):
		del self._OffsetEnd
		self._OffsetEnd = None

	@property
	def PackgBlck(self):
		return self._PackgBlck

	@PackgBlck.setter
	def PackgBlck(self, value):
		self._PackgBlck = value if type(value) != auto else self.make_default("PackgBlck")

	@PackgBlck.deleter
	def PackgBlck(self):
		del self._PackgBlck
		self._PackgBlck = None

	@property
	def OffsetStart(self):
		return self._OffsetStart

	@OffsetStart.setter
	def OffsetStart(self, value):
		self._OffsetStart = value if type(value) != auto else self.make_default("OffsetStart")

	@OffsetStart.deleter
	def OffsetStart(self):
		del self._OffsetStart
		self._OffsetStart = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PackgLngth', type=PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PackgId', type=GenericIdentification176, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OffsetEnd', type=PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PackgBlck', type=ExternallyDefinedData5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OffsetStart', type=PositiveNumber, min=0, max=1, mutex_group=None, array=False),
	))

