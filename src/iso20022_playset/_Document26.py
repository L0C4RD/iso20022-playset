# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISO2ALanguageCode
from . import LanguageVersion1Code
from . import Max2048Text

class Document26(base_types._BaseFieldType):

	__slots__ = ["_Desc", "_ElctrncSealRef", "_Lang", "_OrgnlOrTrnsltd", "_Ref"]
	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if value is not None else base_types.UninitialisedField(self, 'Desc', Max2048Text, False)

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = base_types.UninitialisedField(self, 'Desc', Max2048Text, False)

	@property
	def ElctrncSealRef(self):
		return self._ElctrncSealRef

	@ElctrncSealRef.setter
	def ElctrncSealRef(self, value):
		self._ElctrncSealRef = value if value is not None else base_types.UninitialisedField(self, 'ElctrncSealRef', Max2048Text, False)

	@ElctrncSealRef.deleter
	def ElctrncSealRef(self):
		del self._ElctrncSealRef
		self._ElctrncSealRef = base_types.UninitialisedField(self, 'ElctrncSealRef', Max2048Text, False)

	@property
	def Lang(self):
		return self._Lang

	@Lang.setter
	def Lang(self, value):
		self._Lang = value if value is not None else base_types.UninitialisedField(self, 'Lang', ISO2ALanguageCode, True)

	@Lang.deleter
	def Lang(self):
		del self._Lang
		self._Lang = base_types.UninitialisedField(self, 'Lang', ISO2ALanguageCode, True)

	@property
	def OrgnlOrTrnsltd(self):
		return self._OrgnlOrTrnsltd

	@OrgnlOrTrnsltd.setter
	def OrgnlOrTrnsltd(self, value):
		self._OrgnlOrTrnsltd = value if value is not None else base_types.UninitialisedField(self, 'OrgnlOrTrnsltd', LanguageVersion1Code, False)

	@OrgnlOrTrnsltd.deleter
	def OrgnlOrTrnsltd(self):
		del self._OrgnlOrTrnsltd
		self._OrgnlOrTrnsltd = base_types.UninitialisedField(self, 'OrgnlOrTrnsltd', LanguageVersion1Code, False)

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if value is not None else base_types.UninitialisedField(self, 'Ref', Max2048Text, False)

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = base_types.UninitialisedField(self, 'Ref', Max2048Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Desc', type=Max2048Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElctrncSealRef', type=Max2048Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lang', type=ISO2ALanguageCode, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrgnlOrTrnsltd', type=LanguageVersion1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=Max2048Text, min=1, max=1, mutex_group=None, array=False),
	))