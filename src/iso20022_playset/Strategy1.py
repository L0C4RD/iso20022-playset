import base_types
import StressSize1Choice
import Max35Text

class Strategy1(base_types._BaseFieldType):

	__slots__ = ["_Id", "_StrssSz"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def StrssSz(self):
		return self._StrssSz

	@StrssSz.setter
	def StrssSz(self, value):
		self._StrssSz = value if type(value) != auto else self.make_default("StrssSz")

	@StrssSz.deleter
	def StrssSz(self):
		del self._StrssSz
		self._StrssSz = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StrssSz', type=StressSize1Choice, min=1, max=1, mutex_group=None, array=False),
	))

