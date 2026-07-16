# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max140Text
from . import MessageItemCondition2Code

class MessageItemCondition2(base_types._BaseFieldType):

	__slots__ = ["_Cond", "_ItmId", "_Val"]
	@property
	def Cond(self):
		return self._Cond

	@Cond.setter
	def Cond(self, value):
		self._Cond = value if value is not None else base_types.UninitialisedField(self, 'Cond', MessageItemCondition2Code, False)

	@Cond.deleter
	def Cond(self):
		del self._Cond
		self._Cond = base_types.UninitialisedField(self, 'Cond', MessageItemCondition2Code, False)

	@property
	def ItmId(self):
		return self._ItmId

	@ItmId.setter
	def ItmId(self, value):
		self._ItmId = value if value is not None else base_types.UninitialisedField(self, 'ItmId', Max140Text, False)

	@ItmId.deleter
	def ItmId(self):
		del self._ItmId
		self._ItmId = base_types.UninitialisedField(self, 'ItmId', Max140Text, False)

	@property
	def Val(self):
		return self._Val

	@Val.setter
	def Val(self, value):
		self._Val = value if value is not None else base_types.UninitialisedField(self, 'Val', Max140Text, True)

	@Val.deleter
	def Val(self):
		del self._Val
		self._Val = base_types.UninitialisedField(self, 'Val', Max140Text, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cond', type=MessageItemCondition2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ItmId', type=Max140Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Val', type=Max140Text, min=0, max=None, mutex_group=None, array=True),
	))