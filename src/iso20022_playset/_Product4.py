from . import base_types
from .Max70Text import Max70Text

class Product4(base_types._BaseFieldType):

	__slots__ = ["_PdctCd", "_AddtlPdctCd"]
	@property
	def PdctCd(self):
		return self._PdctCd

	@PdctCd.setter
	def PdctCd(self, value):
		self._PdctCd = value if type(value) != base_types.auto else self.make_default("PdctCd")

	@PdctCd.deleter
	def PdctCd(self):
		del self._PdctCd
		self._PdctCd = None

	@property
	def AddtlPdctCd(self):
		return self._AddtlPdctCd

	@AddtlPdctCd.setter
	def AddtlPdctCd(self, value):
		self._AddtlPdctCd = value if type(value) != base_types.auto else self.make_default("AddtlPdctCd")

	@AddtlPdctCd.deleter
	def AddtlPdctCd(self):
		del self._AddtlPdctCd
		self._AddtlPdctCd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PdctCd', type=Max70Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlPdctCd', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
	))

