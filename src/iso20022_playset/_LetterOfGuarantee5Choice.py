from . import base_types
from ._GenericIdentification47 import GenericIdentification47
from ._YesNoIndicator import YesNoIndicator

class LetterOfGuarantee5Choice(base_types._BaseFieldType):

	__slots__ = ["_Ind", "_Prtry"]
	@property
	def Ind(self):
		return self._Ind

	@Ind.setter
	def Ind(self, value):
		self._Ind = value if type(value) != base_types.auto else self.make_default("Ind")

	@Ind.deleter
	def Ind(self):
		del self._Ind
		self._Ind = None

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
		base_types.FieldEntry(name='Ind', type=YesNoIndicator, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=GenericIdentification47, min=0, max=1, mutex_group=1, array=False),
	))

