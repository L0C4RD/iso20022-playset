from . import base_types
from ._GenericIdentification47 import GenericIdentification47
from ._ProprietaryReason5 import ProprietaryReason5

class ProprietaryStatusAndReason7(base_types._BaseFieldType):

	__slots__ = ["_PrtryRsn", "_PrtrySts"]
	@property
	def PrtryRsn(self):
		return self._PrtryRsn

	@PrtryRsn.setter
	def PrtryRsn(self, value):
		self._PrtryRsn = value if type(value) != base_types.auto else self.make_default("PrtryRsn")

	@PrtryRsn.deleter
	def PrtryRsn(self):
		del self._PrtryRsn
		self._PrtryRsn = None

	@property
	def PrtrySts(self):
		return self._PrtrySts

	@PrtrySts.setter
	def PrtrySts(self, value):
		self._PrtrySts = value if type(value) != base_types.auto else self.make_default("PrtrySts")

	@PrtrySts.deleter
	def PrtrySts(self):
		del self._PrtrySts
		self._PrtrySts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrtryRsn', type=ProprietaryReason5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrtrySts', type=GenericIdentification47, min=1, max=1, mutex_group=None, array=False),
	))

