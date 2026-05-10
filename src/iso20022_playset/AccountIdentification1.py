from . import base_types
from .SimpleIdentificationInformation import SimpleIdentificationInformation

class AccountIdentification1(base_types._BaseFieldType):

	__slots__ = ["_Prtry"]
	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if type(value) != base_types.auto else self.make_default("Prtry")

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Prtry', type=SimpleIdentificationInformation, min=1, max=1, mutex_group=None, array=False),
	))

