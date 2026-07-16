# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BICFIDec2014Identifier
from . import ClearingSystemMemberIdentification4Choice
from . import NameAndAddress5
from . import SimpleIdentificationInformation4

class FinancialInstitutionIdentification11Choice(base_types._BaseFieldType):

	__slots__ = ["_BICFI", "_ClrSysMmbId", "_NmAndAdr", "_PrtryId"]
	@property
	def BICFI(self):
		return self._BICFI

	@BICFI.setter
	def BICFI(self, value):
		self._BICFI = value if value is not None else base_types.UninitialisedField(self, 'BICFI', BICFIDec2014Identifier, False)

	@BICFI.deleter
	def BICFI(self):
		del self._BICFI
		self._BICFI = base_types.UninitialisedField(self, 'BICFI', BICFIDec2014Identifier, False)

	@property
	def ClrSysMmbId(self):
		return self._ClrSysMmbId

	@ClrSysMmbId.setter
	def ClrSysMmbId(self, value):
		self._ClrSysMmbId = value if value is not None else base_types.UninitialisedField(self, 'ClrSysMmbId', ClearingSystemMemberIdentification4Choice, False)

	@ClrSysMmbId.deleter
	def ClrSysMmbId(self):
		del self._ClrSysMmbId
		self._ClrSysMmbId = base_types.UninitialisedField(self, 'ClrSysMmbId', ClearingSystemMemberIdentification4Choice, False)

	@property
	def NmAndAdr(self):
		return self._NmAndAdr

	@NmAndAdr.setter
	def NmAndAdr(self, value):
		self._NmAndAdr = value if value is not None else base_types.UninitialisedField(self, 'NmAndAdr', NameAndAddress5, False)

	@NmAndAdr.deleter
	def NmAndAdr(self):
		del self._NmAndAdr
		self._NmAndAdr = base_types.UninitialisedField(self, 'NmAndAdr', NameAndAddress5, False)

	@property
	def PrtryId(self):
		return self._PrtryId

	@PrtryId.setter
	def PrtryId(self, value):
		self._PrtryId = value if value is not None else base_types.UninitialisedField(self, 'PrtryId', SimpleIdentificationInformation4, False)

	@PrtryId.deleter
	def PrtryId(self):
		del self._PrtryId
		self._PrtryId = base_types.UninitialisedField(self, 'PrtryId', SimpleIdentificationInformation4, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BICFI', type=BICFIDec2014Identifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ClrSysMmbId', type=ClearingSystemMemberIdentification4Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NmAndAdr', type=NameAndAddress5, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtryId', type=SimpleIdentificationInformation4, min=0, max=1, mutex_group=1, array=False),
	))