from . import base_types
from .CorporateActionNotificationType1Code import CorporateActionNotificationType1Code
from .RestrictedFINXMax16Text import RestrictedFINXMax16Text
from .CorporateActionProcessingStatus6Choice import CorporateActionProcessingStatus6Choice

class CorporateActionNotification11(base_types._BaseFieldType):

	__slots__ = ["_NtfctnTp", "_NtfctnId", "_PrcgSts"]
	@property
	def NtfctnTp(self):
		return self._NtfctnTp

	@NtfctnTp.setter
	def NtfctnTp(self, value):
		self._NtfctnTp = value if type(value) != auto else self.make_default("NtfctnTp")

	@NtfctnTp.deleter
	def NtfctnTp(self):
		del self._NtfctnTp
		self._NtfctnTp = None

	@property
	def NtfctnId(self):
		return self._NtfctnId

	@NtfctnId.setter
	def NtfctnId(self, value):
		self._NtfctnId = value if type(value) != auto else self.make_default("NtfctnId")

	@NtfctnId.deleter
	def NtfctnId(self):
		del self._NtfctnId
		self._NtfctnId = None

	@property
	def PrcgSts(self):
		return self._PrcgSts

	@PrcgSts.setter
	def PrcgSts(self, value):
		self._PrcgSts = value if type(value) != auto else self.make_default("PrcgSts")

	@PrcgSts.deleter
	def PrcgSts(self):
		del self._PrcgSts
		self._PrcgSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NtfctnTp', type=CorporateActionNotificationType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtfctnId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgSts', type=CorporateActionProcessingStatus6Choice, min=1, max=1, mutex_group=None, array=False),
	))

