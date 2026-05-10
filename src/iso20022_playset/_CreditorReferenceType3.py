from . import base_types
from .Max35Text import Max35Text
from .CreditorReferenceType2Choice import CreditorReferenceType2Choice

class CreditorReferenceType3(base_types._BaseFieldType):

	__slots__ = ["_Issr", "_CdOrPrtry"]
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
	def CdOrPrtry(self):
		return self._CdOrPrtry

	@CdOrPrtry.setter
	def CdOrPrtry(self, value):
		self._CdOrPrtry = value if type(value) != base_types.auto else self.make_default("CdOrPrtry")

	@CdOrPrtry.deleter
	def CdOrPrtry(self):
		del self._CdOrPrtry
		self._CdOrPrtry = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Issr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdOrPrtry', type=CreditorReferenceType2Choice, min=1, max=1, mutex_group=None, array=False),
	))

