from . import base_types
from .Max20000Text import Max20000Text
from .NarrativeType1Choice import NarrativeType1Choice

class Narrative1(base_types._BaseFieldType):

	__slots__ = ["_Tp", "_Txt"]
	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def Txt(self):
		return self._Txt

	@Txt.setter
	def Txt(self, value):
		self._Txt = value if type(value) != base_types.auto else self.make_default("Txt")

	@Txt.deleter
	def Txt(self):
		del self._Txt
		self._Txt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tp', type=NarrativeType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Txt', type=Max20000Text, min=1, max=5, mutex_group=None, array=True),
	))

