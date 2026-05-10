from . import base_types
from .StressItem1Choice import StressItem1Choice

class StressItem1(base_types._BaseFieldType):

	__slots__ = ["_StrssPdct"]
	@property
	def StrssPdct(self):
		return self._StrssPdct

	@StrssPdct.setter
	def StrssPdct(self, value):
		self._StrssPdct = value if type(value) != base_types.auto else self.make_default("StrssPdct")

	@StrssPdct.deleter
	def StrssPdct(self):
		del self._StrssPdct
		self._StrssPdct = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='StrssPdct', type=StressItem1Choice, min=1, max=1, mutex_group=None, array=False),
	))

