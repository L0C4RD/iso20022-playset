# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ISO2ALanguageCode import ISO2ALanguageCode
from ._Max500Text import Max500Text
from ._TrueFalseIndicator import TrueFalseIndicator

class PartyName5(base_types._BaseFieldType):

	__slots__ = ["_Intrnl", "_Lang", "_Val"]
	@property
	def Intrnl(self):
		return self._Intrnl

	@Intrnl.setter
	def Intrnl(self, value):
		self._Intrnl = value if type(value) != base_types.auto else self.make_default("Intrnl")

	@Intrnl.deleter
	def Intrnl(self):
		del self._Intrnl
		self._Intrnl = None

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

	@property
	def Val(self):
		return self._Val

	@Val.setter
	def Val(self, value):
		self._Val = value if type(value) != base_types.auto else self.make_default("Val")

	@Val.deleter
	def Val(self):
		del self._Val
		self._Val = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Intrnl', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lang', type=ISO2ALanguageCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Val', type=Max500Text, min=1, max=1, mutex_group=None, array=False),
	))