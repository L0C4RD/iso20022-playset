from . import base_types
from .Max140Text import Max140Text

class Reason2(base_types._BaseFieldType):

	__slots__ = ["_Desc"]
	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if type(value) != base_types.auto else self.make_default("Desc")

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Desc', type=Max140Text, min=1, max=1, mutex_group=None, array=False),
	))

