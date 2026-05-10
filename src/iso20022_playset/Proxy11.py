from . import base_types
from .ProxyType3Code import ProxyType3Code
from .IndividualPerson43 import IndividualPerson43

class Proxy11(base_types._BaseFieldType):

	__slots__ = ["_PrxyTp", "_PrsnDtls"]
	@property
	def PrxyTp(self):
		return self._PrxyTp

	@PrxyTp.setter
	def PrxyTp(self, value):
		self._PrxyTp = value if type(value) != auto else self.make_default("PrxyTp")

	@PrxyTp.deleter
	def PrxyTp(self):
		del self._PrxyTp
		self._PrxyTp = None

	@property
	def PrsnDtls(self):
		return self._PrsnDtls

	@PrsnDtls.setter
	def PrsnDtls(self, value):
		self._PrsnDtls = value if type(value) != auto else self.make_default("PrsnDtls")

	@PrsnDtls.deleter
	def PrsnDtls(self):
		del self._PrsnDtls
		self._PrsnDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrxyTp', type=ProxyType3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrsnDtls', type=IndividualPerson43, min=0, max=1, mutex_group=None, array=False),
	))

