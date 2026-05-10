from . import base_types
from ._Max256Text import Max256Text

class AdditionalInformation5(base_types._BaseFieldType):

	__slots__ = ["_Inf"]
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
		base_types.FieldEntry(name='Inf', type=Max256Text, min=1, max=None, mutex_group=None, array=True),
	))

