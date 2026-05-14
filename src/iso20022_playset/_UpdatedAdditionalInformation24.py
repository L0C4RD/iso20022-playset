# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ISO2ALanguageCode import ISO2ALanguageCode
from ._RestrictedFINXMax350Text import RestrictedFINXMax350Text

class UpdatedAdditionalInformation24(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_Lang"]
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
		base_types.FieldEntry(name='AddtlInf', type=RestrictedFINXMax350Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lang', type=ISO2ALanguageCode, min=1, max=1, mutex_group=None, array=False),
	))