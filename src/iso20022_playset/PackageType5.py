import base_types
import GenericIdentification176
import PositiveNumber
import ExternallyDefinedData5

class PackageType5(base_types._BaseFieldType):

	__slots__ = ["_PackgLngth", "_OffsetEnd", "_OffsetStart", "_PackgId", "_PackgBlck"]
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
	def OffsetStart(self):
		return self._OffsetStart

	@OffsetStart.setter
	def OffsetStart(self, value):
		self._OffsetStart = value if type(value) != auto else self.make_default("OffsetStart")

	@OffsetStart.deleter
	def OffsetStart(self):
		del self._OffsetStart
		self._OffsetStart = None

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
	def PackgBlck(self):
		return self._PackgBlck

	@PackgBlck.setter
	def PackgBlck(self, value):
		self._PackgBlck = value if type(value) != auto else self.make_default("PackgBlck")

	@PackgBlck.deleter
	def PackgBlck(self):
		del self._PackgBlck
		self._PackgBlck = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PackgLngth', type=PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OffsetEnd', type=PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OffsetStart', type=PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PackgId', type=GenericIdentification176, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PackgBlck', type=ExternallyDefinedData5, min=0, max=None, mutex_group=None, array=True),
	))

