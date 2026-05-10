from . import base_types
from ._LimitIdentification8 import LimitIdentification8
from ._LimitIdentification9 import LimitIdentification9

class LimitIdentification3Choice(base_types._BaseFieldType):

	__slots__ = ["_AllCur", "_AllDflt", "_Cur", "_Dflt"]
	@property
	def AllCur(self):
		return self._AllCur

	@AllCur.setter
	def AllCur(self, value):
		self._AllCur = value if type(value) != base_types.auto else self.make_default("AllCur")

	@AllCur.deleter
	def AllCur(self):
		del self._AllCur
		self._AllCur = None

	@property
	def AllDflt(self):
		return self._AllDflt

	@AllDflt.setter
	def AllDflt(self, value):
		self._AllDflt = value if type(value) != base_types.auto else self.make_default("AllDflt")

	@AllDflt.deleter
	def AllDflt(self):
		del self._AllDflt
		self._AllDflt = None

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
	def Dflt(self):
		return self._Dflt

	@Dflt.setter
	def Dflt(self, value):
		self._Dflt = value if type(value) != base_types.auto else self.make_default("Dflt")

	@Dflt.deleter
	def Dflt(self):
		del self._Dflt
		self._Dflt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AllCur', type=LimitIdentification9, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AllDflt', type=LimitIdentification9, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Cur', type=LimitIdentification8, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Dflt', type=LimitIdentification8, min=0, max=1, mutex_group=1, array=False),
	))

