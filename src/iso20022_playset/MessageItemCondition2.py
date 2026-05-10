from . import base_types
from .MessageItemCondition2Code import MessageItemCondition2Code
from .Max140Text import Max140Text

class MessageItemCondition2(base_types._BaseFieldType):

	__slots__ = ["_Val", "_Cond", "_ItmId"]
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

	@property
	def Cond(self):
		return self._Cond

	@Cond.setter
	def Cond(self, value):
		self._Cond = value if type(value) != base_types.auto else self.make_default("Cond")

	@Cond.deleter
	def Cond(self):
		del self._Cond
		self._Cond = None

	@property
	def ItmId(self):
		return self._ItmId

	@ItmId.setter
	def ItmId(self, value):
		self._ItmId = value if type(value) != base_types.auto else self.make_default("ItmId")

	@ItmId.deleter
	def ItmId(self):
		del self._ItmId
		self._ItmId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Val', type=Max140Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Cond', type=MessageItemCondition2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ItmId', type=Max140Text, min=1, max=1, mutex_group=None, array=False),
	))

