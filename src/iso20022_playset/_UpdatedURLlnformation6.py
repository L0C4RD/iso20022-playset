# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISO2ALanguageCode
from . import Max2048Text

class UpdatedURLlnformation6(base_types._BaseFieldType):

	__slots__ = ["_Lang", "_URLAdr"]
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
	def URLAdr(self):
		return self._URLAdr

	@URLAdr.setter
	def URLAdr(self, value):
		self._URLAdr = value if value is not None else base_types.UninitialisedField(self, 'URLAdr', Max2048Text, False)

	@URLAdr.deleter
	def URLAdr(self):
		del self._URLAdr
		self._URLAdr = base_types.UninitialisedField(self, 'URLAdr', Max2048Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Lang', type=ISO2ALanguageCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='URLAdr', type=Max2048Text, min=1, max=1, mutex_group=None, array=False),
	))