# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BICFIIdentifier
from . import ClearingSystemMemberIdentification2
from . import GenericFinancialIdentification1
from . import Max140Text
from . import PostalAddress6

class FinancialInstitutionIdentification8(base_types._BaseFieldType):

	__slots__ = ["_BICFI", "_ClrSysMmbId", "_Nm", "_Othr", "_PstlAdr"]
	@property
	def BICFI(self):
		return self._BICFI

	@BICFI.setter
	def BICFI(self, value):
		self._BICFI = value if value is not None else base_types.UninitialisedField(self, 'BICFI', BICFIIdentifier, False)

	@BICFI.deleter
	def BICFI(self):
		del self._BICFI
		self._BICFI = base_types.UninitialisedField(self, 'BICFI', BICFIIdentifier, False)

	@property
	def ClrSysMmbId(self):
		return self._ClrSysMmbId

	@ClrSysMmbId.setter
	def ClrSysMmbId(self, value):
		self._ClrSysMmbId = value if value is not None else base_types.UninitialisedField(self, 'ClrSysMmbId', ClearingSystemMemberIdentification2, False)

	@ClrSysMmbId.deleter
	def ClrSysMmbId(self):
		del self._ClrSysMmbId
		self._ClrSysMmbId = base_types.UninitialisedField(self, 'ClrSysMmbId', ClearingSystemMemberIdentification2, False)

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if value is not None else base_types.UninitialisedField(self, 'Nm', Max140Text, False)

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = base_types.UninitialisedField(self, 'Nm', Max140Text, False)

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if value is not None else base_types.UninitialisedField(self, 'Othr', GenericFinancialIdentification1, False)

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = base_types.UninitialisedField(self, 'Othr', GenericFinancialIdentification1, False)

	@property
	def PstlAdr(self):
		return self._PstlAdr

	@PstlAdr.setter
	def PstlAdr(self, value):
		self._PstlAdr = value if value is not None else base_types.UninitialisedField(self, 'PstlAdr', PostalAddress6, False)

	@PstlAdr.deleter
	def PstlAdr(self):
		del self._PstlAdr
		self._PstlAdr = base_types.UninitialisedField(self, 'PstlAdr', PostalAddress6, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BICFI', type=BICFIIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrSysMmbId', type=ClearingSystemMemberIdentification2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Othr', type=GenericFinancialIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstlAdr', type=PostalAddress6, min=0, max=1, mutex_group=None, array=False),
	))