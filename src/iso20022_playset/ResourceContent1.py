from . import base_types
from .ResourceType1Code import ResourceType1Code
from .SoundFormat1Code import SoundFormat1Code
from .LanguageCode import LanguageCode
from .Max1025Text import Max1025Text

class ResourceContent1(base_types._BaseFieldType):

	__slots__ = ["_RsrcRef", "_RsrcFrmt", "_RsrcTp", "_Lang"]
	@property
	def RsrcRef(self):
		return self._RsrcRef

	@RsrcRef.setter
	def RsrcRef(self, value):
		self._RsrcRef = value if type(value) != base_types.auto else self.make_default("RsrcRef")

	@RsrcRef.deleter
	def RsrcRef(self):
		del self._RsrcRef
		self._RsrcRef = None

	@property
	def RsrcFrmt(self):
		return self._RsrcFrmt

	@RsrcFrmt.setter
	def RsrcFrmt(self, value):
		self._RsrcFrmt = value if type(value) != base_types.auto else self.make_default("RsrcFrmt")

	@RsrcFrmt.deleter
	def RsrcFrmt(self):
		del self._RsrcFrmt
		self._RsrcFrmt = None

	@property
	def RsrcTp(self):
		return self._RsrcTp

	@RsrcTp.setter
	def RsrcTp(self, value):
		self._RsrcTp = value if type(value) != base_types.auto else self.make_default("RsrcTp")

	@RsrcTp.deleter
	def RsrcTp(self):
		del self._RsrcTp
		self._RsrcTp = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='RsrcRef', type=Max1025Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsrcFrmt', type=SoundFormat1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsrcTp', type=ResourceType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lang', type=LanguageCode, min=0, max=1, mutex_group=None, array=False),
	))

