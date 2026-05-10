from . import base_types
from ._DecimalNumber import DecimalNumber
from ._Max35Text import Max35Text

class Entitlement1Choice(base_types._BaseFieldType):

	__slots__ = ["_EntitlmntRatio", "_EntitlmntDesc"]
	@property
	def EntitlmntDesc(self):
		return self._EntitlmntDesc

	@EntitlmntDesc.setter
	def EntitlmntDesc(self, value):
		self._EntitlmntDesc = value if type(value) != base_types.auto else self.make_default("EntitlmntDesc")

	@EntitlmntDesc.deleter
	def EntitlmntDesc(self):
		del self._EntitlmntDesc
		self._EntitlmntDesc = None

	@property
	def EntitlmntRatio(self):
		return self._EntitlmntRatio

	@EntitlmntRatio.setter
	def EntitlmntRatio(self, value):
		self._EntitlmntRatio = value if type(value) != base_types.auto else self.make_default("EntitlmntRatio")

	@EntitlmntRatio.deleter
	def EntitlmntRatio(self):
		del self._EntitlmntRatio
		self._EntitlmntRatio = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='EntitlmntDesc', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='EntitlmntRatio', type=DecimalNumber, min=0, max=1, mutex_group=1, array=False),
	))

