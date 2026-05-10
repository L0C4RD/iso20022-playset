from . import base_types
from .Max140Text import Max140Text
from .Max35Text import Max35Text

class UserDefinedInformation1(base_types._BaseFieldType):

	__slots__ = ["_Labl", "_Inf"]
	@property
	def Labl(self):
		return self._Labl

	@Labl.setter
	def Labl(self, value):
		self._Labl = value if type(value) != base_types.auto else self.make_default("Labl")

	@Labl.deleter
	def Labl(self):
		del self._Labl
		self._Labl = None

	@property
	def Inf(self):
		return self._Inf

	@Inf.setter
	def Inf(self, value):
		self._Inf = value if type(value) != base_types.auto else self.make_default("Inf")

	@Inf.deleter
	def Inf(self):
		del self._Inf
		self._Inf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Labl', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Inf', type=Max140Text, min=1, max=1, mutex_group=None, array=False),
	))

