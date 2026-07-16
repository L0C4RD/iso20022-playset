# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import LanguageCode
from . import Max1025Text
from . import ResourceType1Code
from . import SoundFormat1Code

class ResourceContent1(base_types._BaseFieldType):

	__slots__ = ["_Lang", "_RsrcFrmt", "_RsrcRef", "_RsrcTp"]
	@property
	def Lang(self):
		return self._Lang

	@Lang.setter
	def Lang(self, value):
		self._Lang = value if value is not None else base_types.UninitialisedField(self, 'Lang', LanguageCode, False)

	@Lang.deleter
	def Lang(self):
		del self._Lang
		self._Lang = base_types.UninitialisedField(self, 'Lang', LanguageCode, False)

	@property
	def RsrcFrmt(self):
		return self._RsrcFrmt

	@RsrcFrmt.setter
	def RsrcFrmt(self, value):
		self._RsrcFrmt = value if value is not None else base_types.UninitialisedField(self, 'RsrcFrmt', SoundFormat1Code, False)

	@RsrcFrmt.deleter
	def RsrcFrmt(self):
		del self._RsrcFrmt
		self._RsrcFrmt = base_types.UninitialisedField(self, 'RsrcFrmt', SoundFormat1Code, False)

	@property
	def RsrcRef(self):
		return self._RsrcRef

	@RsrcRef.setter
	def RsrcRef(self, value):
		self._RsrcRef = value if value is not None else base_types.UninitialisedField(self, 'RsrcRef', Max1025Text, False)

	@RsrcRef.deleter
	def RsrcRef(self):
		del self._RsrcRef
		self._RsrcRef = base_types.UninitialisedField(self, 'RsrcRef', Max1025Text, False)

	@property
	def RsrcTp(self):
		return self._RsrcTp

	@RsrcTp.setter
	def RsrcTp(self, value):
		self._RsrcTp = value if value is not None else base_types.UninitialisedField(self, 'RsrcTp', ResourceType1Code, False)

	@RsrcTp.deleter
	def RsrcTp(self):
		del self._RsrcTp
		self._RsrcTp = base_types.UninitialisedField(self, 'RsrcTp', ResourceType1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Lang', type=LanguageCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsrcFrmt', type=SoundFormat1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsrcRef', type=Max1025Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsrcTp', type=ResourceType1Code, min=1, max=1, mutex_group=None, array=False),
	))