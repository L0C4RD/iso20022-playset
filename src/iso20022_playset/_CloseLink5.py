# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecurityIdentification19
from . import SystemPartyIdentification2Choice

class CloseLink5(base_types._BaseFieldType):

	__slots__ = ["_CdtPrvdrId", "_PtyId", "_SctyId"]
	@property
	def CdtPrvdrId(self):
		return self._CdtPrvdrId

	@CdtPrvdrId.setter
	def CdtPrvdrId(self, value):
		self._CdtPrvdrId = value if value is not None else base_types.UninitialisedField(self, 'CdtPrvdrId', SystemPartyIdentification2Choice, False)

	@CdtPrvdrId.deleter
	def CdtPrvdrId(self):
		del self._CdtPrvdrId
		self._CdtPrvdrId = base_types.UninitialisedField(self, 'CdtPrvdrId', SystemPartyIdentification2Choice, False)

	@property
	def PtyId(self):
		return self._PtyId

	@PtyId.setter
	def PtyId(self, value):
		self._PtyId = value if value is not None else base_types.UninitialisedField(self, 'PtyId', SystemPartyIdentification2Choice, False)

	@PtyId.deleter
	def PtyId(self):
		del self._PtyId
		self._PtyId = base_types.UninitialisedField(self, 'PtyId', SystemPartyIdentification2Choice, False)

	@property
	def SctyId(self):
		return self._SctyId

	@SctyId.setter
	def SctyId(self, value):
		self._SctyId = value if value is not None else base_types.UninitialisedField(self, 'SctyId', SecurityIdentification19, True)

	@SctyId.deleter
	def SctyId(self):
		del self._SctyId
		self._SctyId = base_types.UninitialisedField(self, 'SctyId', SecurityIdentification19, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CdtPrvdrId', type=SystemPartyIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyId', type=SystemPartyIdentification2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyId', type=SecurityIdentification19, min=1, max=None, mutex_group=None, array=True),
	))