from . import base_types
from .Max3NumericText import Max3NumericText

class Limit1(base_types._BaseFieldType):

	__slots__ = ["_Cur", "_Lmt"]
	@property
	def Cur(self):
		return self._Cur

	@Cur.setter
	def Cur(self, value):
		self._Cur = value if type(value) != base_types.auto else self.make_default("Cur")

	@Cur.deleter
	def Cur(self):
		del self._Cur
		self._Cur = None

	@property
	def Lmt(self):
		return self._Lmt

	@Lmt.setter
	def Lmt(self, value):
		self._Lmt = value if type(value) != base_types.auto else self.make_default("Lmt")

	@Lmt.deleter
	def Lmt(self):
		del self._Lmt
		self._Lmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cur', type=Max3NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lmt', type=Max3NumericText, min=1, max=1, mutex_group=None, array=False),
	))

