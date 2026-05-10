from . import base_types
from ._Max35Text import Max35Text
from ._InformationQualifierType1 import InformationQualifierType1
from ._CharacterSearch1Choice import CharacterSearch1Choice

class GeneralBusinessInformationSearchCriteria1(base_types._BaseFieldType):

	__slots__ = ["_Qlfr", "_Sbjt", "_Ref"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Qlfr', type=InformationQualifierType1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sbjt', type=CharacterSearch1Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Ref', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
	))

