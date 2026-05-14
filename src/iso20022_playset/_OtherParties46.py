from . import base_types
from ._PartyIdentificationAndAccount197 import PartyIdentificationAndAccount197

class OtherParties46(base_types._BaseFieldType):

	__slots__ = ["_Invstr"]
	@property
	def Invstr(self):
		return self._Invstr

	@Invstr.setter
	def Invstr(self, value):
		self._Invstr = value if type(value) != base_types.auto else self.make_default("Invstr")

	@Invstr.deleter
	def Invstr(self):
		del self._Invstr
		self._Invstr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Invstr', type=PartyIdentificationAndAccount197, min=0, max=None, mutex_group=None, array=True),
	))

