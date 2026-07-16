# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISO2ALanguageCode
from . import Max500Text
from . import TrueFalseIndicator

class PartyName5(base_types._BaseFieldType):

	__slots__ = ["_Intrnl", "_Lang", "_Val"]
	@property
	def Intrnl(self):
		return self._Intrnl

	@Intrnl.setter
	def Intrnl(self, value):
		self._Intrnl = value if value is not None else base_types.UninitialisedField(self, 'Intrnl', TrueFalseIndicator, False)

	@Intrnl.deleter
	def Intrnl(self):
		del self._Intrnl
		self._Intrnl = base_types.UninitialisedField(self, 'Intrnl', TrueFalseIndicator, False)

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
	def Val(self):
		return self._Val

	@Val.setter
	def Val(self, value):
		self._Val = value if value is not None else base_types.UninitialisedField(self, 'Val', Max500Text, False)

	@Val.deleter
	def Val(self):
		del self._Val
		self._Val = base_types.UninitialisedField(self, 'Val', Max500Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Intrnl', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lang', type=ISO2ALanguageCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Val', type=Max500Text, min=1, max=1, mutex_group=None, array=False),
	))