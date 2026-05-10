from . import base_types
from .Max8Text import Max8Text
from .Max35Text import Max35Text

class GenericIdentification7(base_types._BaseFieldType):

	__slots__ = ["_Issr", "_Inf"]
	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if type(value) != base_types.auto else self.make_default("Issr")

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = None

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
		base_types.FieldEntry(name='Issr', type=Max8Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Inf', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

