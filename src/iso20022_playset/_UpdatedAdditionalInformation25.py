from . import base_types
from ._ISO2ALanguageCode import ISO2ALanguageCode
from ._RestrictedFINXMax350Text import RestrictedFINXMax350Text

class UpdatedAdditionalInformation25(base_types._BaseFieldType):

	__slots__ = ["_Lang", "_AddtlInf"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != base_types.auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

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
		base_types.FieldEntry(name='AddtlInf', type=RestrictedFINXMax350Text, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Lang', type=ISO2ALanguageCode, min=1, max=1, mutex_group=None, array=False),
	))

