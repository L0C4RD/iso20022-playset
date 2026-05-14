from . import base_types
from ._ISO2ALanguageCode import ISO2ALanguageCode
from ._LanguageVersion1Code import LanguageVersion1Code
from ._Max2048Text import Max2048Text

class Document26(base_types._BaseFieldType):

	__slots__ = ["_Desc", "_ElctrncSealRef", "_Lang", "_OrgnlOrTrnsltd", "_Ref"]
	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if type(value) != base_types.auto else self.make_default("Desc")

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = None

	@property
	def ElctrncSealRef(self):
		return self._ElctrncSealRef

	@ElctrncSealRef.setter
	def ElctrncSealRef(self, value):
		self._ElctrncSealRef = value if type(value) != base_types.auto else self.make_default("ElctrncSealRef")

	@ElctrncSealRef.deleter
	def ElctrncSealRef(self):
		del self._ElctrncSealRef
		self._ElctrncSealRef = None

	@property
	def Lang(self):
		return self._Lang

	@Lang.setter
	def Lang(self, value):
		self._Lang = value if type(value) != base_types.auto else self.make_default("Lang")

	@Lang.deleter
	def Lang(self):
		del self._Lang
		self._Lang = None

	@property
	def OrgnlOrTrnsltd(self):
		return self._OrgnlOrTrnsltd

	@OrgnlOrTrnsltd.setter
	def OrgnlOrTrnsltd(self, value):
		self._OrgnlOrTrnsltd = value if type(value) != base_types.auto else self.make_default("OrgnlOrTrnsltd")

	@OrgnlOrTrnsltd.deleter
	def OrgnlOrTrnsltd(self):
		del self._OrgnlOrTrnsltd
		self._OrgnlOrTrnsltd = None

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
		base_types.FieldEntry(name='Desc', type=Max2048Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElctrncSealRef', type=Max2048Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lang', type=ISO2ALanguageCode, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrgnlOrTrnsltd', type=LanguageVersion1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=Max2048Text, min=1, max=1, mutex_group=None, array=False),
	))

