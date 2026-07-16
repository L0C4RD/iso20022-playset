# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISOMax3ALanguageCode
from . import Max40KText

class LocalData9(base_types._BaseFieldType):

	__slots__ = ["_Lang", "_TxtMsg"]
	@property
	def Lang(self):
		return self._Lang

	@Lang.setter
	def Lang(self, value):
		self._Lang = value if value is not None else base_types.UninitialisedField(self, 'Lang', ISOMax3ALanguageCode, False)

	@Lang.deleter
	def Lang(self):
		del self._Lang
		self._Lang = base_types.UninitialisedField(self, 'Lang', ISOMax3ALanguageCode, False)

	@property
	def TxtMsg(self):
		return self._TxtMsg

	@TxtMsg.setter
	def TxtMsg(self, value):
		self._TxtMsg = value if value is not None else base_types.UninitialisedField(self, 'TxtMsg', Max40KText, False)

	@TxtMsg.deleter
	def TxtMsg(self):
		del self._TxtMsg
		self._TxtMsg = base_types.UninitialisedField(self, 'TxtMsg', Max40KText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Lang', type=ISOMax3ALanguageCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxtMsg', type=Max40KText, min=1, max=1, mutex_group=None, array=False),
	))