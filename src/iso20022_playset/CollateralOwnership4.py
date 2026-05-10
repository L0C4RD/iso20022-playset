from . import base_types
from .PartyIdentification178Choice import PartyIdentification178Choice
from .YesNoIndicator import YesNoIndicator

class CollateralOwnership4(base_types._BaseFieldType):

	__slots__ = ["_Prtry", "_ClntNm"]
	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if type(value) != auto else self.make_default("Prtry")

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = None

	@property
	def ClntNm(self):
		return self._ClntNm

	@ClntNm.setter
	def ClntNm(self, value):
		self._ClntNm = value if type(value) != auto else self.make_default("ClntNm")

	@ClntNm.deleter
	def ClntNm(self):
		del self._ClntNm
		self._ClntNm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Prtry', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntNm', type=PartyIdentification178Choice, min=0, max=1, mutex_group=None, array=False),
	))

