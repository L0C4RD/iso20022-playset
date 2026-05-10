from . import base_types
import Max35Text
import CreditorReferenceType1Choice

class CreditorReferenceType2(base_types._BaseFieldType):

	__slots__ = ["_CdOrPrtry", "_Issr"]
	@property
	def CdOrPrtry(self):
		return self._CdOrPrtry

	@CdOrPrtry.setter
	def CdOrPrtry(self, value):
		self._CdOrPrtry = value if type(value) != auto else self.make_default("CdOrPrtry")

	@CdOrPrtry.deleter
	def CdOrPrtry(self):
		del self._CdOrPrtry
		self._CdOrPrtry = None

	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if type(value) != auto else self.make_default("Issr")

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CdOrPrtry', type=CreditorReferenceType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Issr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

