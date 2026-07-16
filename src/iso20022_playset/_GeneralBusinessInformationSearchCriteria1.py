# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CharacterSearch1Choice
from . import InformationQualifierType1
from . import Max35Text

class GeneralBusinessInformationSearchCriteria1(base_types._BaseFieldType):

	__slots__ = ["_Qlfr", "_Ref", "_Sbjt"]
	@property
	def Qlfr(self):
		return self._Qlfr

	@Qlfr.setter
	def Qlfr(self, value):
		self._Qlfr = value if value is not None else base_types.UninitialisedField(self, 'Qlfr', InformationQualifierType1, True)

	@Qlfr.deleter
	def Qlfr(self):
		del self._Qlfr
		self._Qlfr = base_types.UninitialisedField(self, 'Qlfr', InformationQualifierType1, True)

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if value is not None else base_types.UninitialisedField(self, 'Ref', Max35Text, True)

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = base_types.UninitialisedField(self, 'Ref', Max35Text, True)

	@property
	def Sbjt(self):
		return self._Sbjt

	@Sbjt.setter
	def Sbjt(self, value):
		self._Sbjt = value if value is not None else base_types.UninitialisedField(self, 'Sbjt', CharacterSearch1Choice, True)

	@Sbjt.deleter
	def Sbjt(self):
		del self._Sbjt
		self._Sbjt = base_types.UninitialisedField(self, 'Sbjt', CharacterSearch1Choice, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Qlfr', type=InformationQualifierType1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Ref', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sbjt', type=CharacterSearch1Choice, min=0, max=None, mutex_group=None, array=True),
	))