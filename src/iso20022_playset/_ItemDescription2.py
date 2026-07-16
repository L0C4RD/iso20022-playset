# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISO2ALanguageCode
from . import Max1025Text
from . import Max8000Text

class ItemDescription2(base_types._BaseFieldType):

	__slots__ = ["_Desc", "_Lang", "_Titl"]
	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if value is not None else base_types.UninitialisedField(self, 'Desc', Max8000Text, True)

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = base_types.UninitialisedField(self, 'Desc', Max8000Text, True)

	@property
	def Lang(self):
		return self._Lang

	@Lang.setter
	def Lang(self, value):
		self._Lang = value if value is not None else base_types.UninitialisedField(self, 'Lang', ISO2ALanguageCode, False)

	@Lang.deleter
	def Lang(self):
		del self._Lang
		self._Lang = base_types.UninitialisedField(self, 'Lang', ISO2ALanguageCode, False)

	@property
	def Titl(self):
		return self._Titl

	@Titl.setter
	def Titl(self, value):
		self._Titl = value if value is not None else base_types.UninitialisedField(self, 'Titl', Max1025Text, False)

	@Titl.deleter
	def Titl(self):
		del self._Titl
		self._Titl = base_types.UninitialisedField(self, 'Titl', Max1025Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Desc', type=Max8000Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Lang', type=ISO2ALanguageCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Titl', type=Max1025Text, min=0, max=1, mutex_group=None, array=False),
	))