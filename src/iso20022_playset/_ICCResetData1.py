from . import base_types
from .Max35Binary import Max35Binary
from .Max140Binary import Max140Binary

class ICCResetData1(base_types._BaseFieldType):

	__slots__ = ["_CardSts", "_ATRVal"]
	@property
	def CardSts(self):
		return self._CardSts

	@CardSts.setter
	def CardSts(self, value):
		self._CardSts = value if type(value) != base_types.auto else self.make_default("CardSts")

	@CardSts.deleter
	def CardSts(self):
		del self._CardSts
		self._CardSts = None

	@property
	def ATRVal(self):
		return self._ATRVal

	@ATRVal.setter
	def ATRVal(self, value):
		self._ATRVal = value if type(value) != base_types.auto else self.make_default("ATRVal")

	@ATRVal.deleter
	def ATRVal(self):
		del self._ATRVal
		self._ATRVal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CardSts', type=Max35Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ATRVal', type=Max140Binary, min=0, max=1, mutex_group=None, array=False),
	))

