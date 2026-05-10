from . import base_types
from .Max35Text import Max35Text
from .CharacterSearch1Choice import CharacterSearch1Choice
from .InformationQualifierType1 import InformationQualifierType1

class GeneralBusinessInformationSearchCriteria1(base_types._BaseFieldType):

	__slots__ = ["_Sbjt", "_Ref", "_Qlfr"]
	@property
	def Sbjt(self):
		return self._Sbjt

	@Sbjt.setter
	def Sbjt(self, value):
		self._Sbjt = value if type(value) != base_types.auto else self.make_default("Sbjt")

	@Sbjt.deleter
	def Sbjt(self):
		del self._Sbjt
		self._Sbjt = None

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if type(value) != base_types.auto else self.make_default("Ref")

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = None

	@property
	def Qlfr(self):
		return self._Qlfr

	@Qlfr.setter
	def Qlfr(self, value):
		self._Qlfr = value if type(value) != base_types.auto else self.make_default("Qlfr")

	@Qlfr.deleter
	def Qlfr(self):
		del self._Qlfr
		self._Qlfr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Sbjt', type=CharacterSearch1Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Ref', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Qlfr', type=InformationQualifierType1, min=0, max=None, mutex_group=None, array=True),
	))

