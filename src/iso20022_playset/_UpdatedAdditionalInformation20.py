# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISO2ALanguageCode
from . import Max8000Text

class UpdatedAdditionalInformation20(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_Lang"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', Max8000Text, True)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', Max8000Text, True)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max8000Text, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Lang', type=ISO2ALanguageCode, min=1, max=1, mutex_group=None, array=False),
	))