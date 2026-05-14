from . import base_types
from ._SecurityIdentification19 import SecurityIdentification19
from ._SystemPartyIdentification2Choice import SystemPartyIdentification2Choice

class CloseLink5(base_types._BaseFieldType):

	__slots__ = ["_CdtPrvdrId", "_PtyId", "_SctyId"]
	@property
	def CdtPrvdrId(self):
		return self._CdtPrvdrId

	@CdtPrvdrId.setter
	def CdtPrvdrId(self, value):
		self._CdtPrvdrId = value if type(value) != base_types.auto else self.make_default("CdtPrvdrId")

	@CdtPrvdrId.deleter
	def CdtPrvdrId(self):
		del self._CdtPrvdrId
		self._CdtPrvdrId = None

	@property
	def PtyId(self):
		return self._PtyId

	@PtyId.setter
	def PtyId(self, value):
		self._PtyId = value if type(value) != base_types.auto else self.make_default("PtyId")

	@PtyId.deleter
	def PtyId(self):
		del self._PtyId
		self._PtyId = None

	@property
	def SctyId(self):
		return self._SctyId

	@SctyId.setter
	def SctyId(self, value):
		self._SctyId = value if type(value) != base_types.auto else self.make_default("SctyId")

	@SctyId.deleter
	def SctyId(self):
		del self._SctyId
		self._SctyId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CdtPrvdrId', type=SystemPartyIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyId', type=SystemPartyIdentification2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyId', type=SecurityIdentification19, min=1, max=None, mutex_group=None, array=True),
	))

