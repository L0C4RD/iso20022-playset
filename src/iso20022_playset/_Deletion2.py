from . import base_types
from ._Max350Text import Max350Text

class Deletion2(base_types._BaseFieldType):

	__slots__ = ["_DeltdVal"]
	@property
	def DeltdVal(self):
		return self._DeltdVal

	@DeltdVal.setter
	def DeltdVal(self, value):
		self._DeltdVal = value if type(value) != base_types.auto else self.make_default("DeltdVal")

	@DeltdVal.deleter
	def DeltdVal(self):
		del self._DeltdVal
		self._DeltdVal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DeltdVal', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
	))

