from . import base_types
from .IndividualPerson42 import IndividualPerson42
from .ProxyType3Code import ProxyType3Code

class Proxy12(base_types._BaseFieldType):

	__slots__ = ["_PrsnDtls", "_PrxyTp"]
	@property
	def PrsnDtls(self):
		return self._PrsnDtls

	@PrsnDtls.setter
	def PrsnDtls(self, value):
		self._PrsnDtls = value if type(value) != base_types.auto else self.make_default("PrsnDtls")

	@PrsnDtls.deleter
	def PrsnDtls(self):
		del self._PrsnDtls
		self._PrsnDtls = None

	@property
	def PrxyTp(self):
		return self._PrxyTp

	@PrxyTp.setter
	def PrxyTp(self, value):
		self._PrxyTp = value if type(value) != base_types.auto else self.make_default("PrxyTp")

	@PrxyTp.deleter
	def PrxyTp(self):
		del self._PrxyTp
		self._PrxyTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrsnDtls', type=IndividualPerson42, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrxyTp', type=ProxyType3Code, min=1, max=1, mutex_group=None, array=False),
	))

