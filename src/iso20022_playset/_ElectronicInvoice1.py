from . import base_types
from ._PresentmentType1Code import PresentmentType1Code

class ElectronicInvoice1(base_types._BaseFieldType):

	__slots__ = ["_PresntmntTp"]
	@property
	def PresntmntTp(self):
		return self._PresntmntTp

	@PresntmntTp.setter
	def PresntmntTp(self, value):
		self._PresntmntTp = value if type(value) != base_types.auto else self.make_default("PresntmntTp")

	@PresntmntTp.deleter
	def PresntmntTp(self):
		del self._PresntmntTp
		self._PresntmntTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PresntmntTp', type=PresentmentType1Code, min=1, max=1, mutex_group=None, array=False),
	))

