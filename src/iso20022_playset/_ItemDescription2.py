from . import base_types
from .Max8000Text import Max8000Text
from .ISO2ALanguageCode import ISO2ALanguageCode
from .Max1025Text import Max1025Text

class ItemDescription2(base_types._BaseFieldType):

	__slots__ = ["_Desc", "_Titl", "_Lang"]
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
	def Titl(self):
		return self._Titl

	@Titl.setter
	def Titl(self, value):
		self._Titl = value if type(value) != base_types.auto else self.make_default("Titl")

	@Titl.deleter
	def Titl(self):
		del self._Titl
		self._Titl = None

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
		base_types.FieldEntry(name='Desc', type=Max8000Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Titl', type=Max1025Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lang', type=ISO2ALanguageCode, min=1, max=1, mutex_group=None, array=False),
	))

