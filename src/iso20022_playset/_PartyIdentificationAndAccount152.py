# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AlternatePartyIdentification10
from . import Max35Text
from . import PartyIdentification245Choice
from . import PartyTextInformation1

class PartyIdentificationAndAccount152(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_AltrnId", "_Id", "_PrcgId"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', PartyTextInformation1, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', PartyTextInformation1, False)

	@property
	def AltrnId(self):
		return self._AltrnId

	@AltrnId.setter
	def AltrnId(self, value):
		self._AltrnId = value if value is not None else base_types.UninitialisedField(self, 'AltrnId', AlternatePartyIdentification10, False)

	@AltrnId.deleter
	def AltrnId(self):
		del self._AltrnId
		self._AltrnId = base_types.UninitialisedField(self, 'AltrnId', AlternatePartyIdentification10, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', PartyIdentification245Choice, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', PartyIdentification245Choice, False)

	@property
	def PrcgId(self):
		return self._PrcgId

	@PrcgId.setter
	def PrcgId(self, value):
		self._PrcgId = value if value is not None else base_types.UninitialisedField(self, 'PrcgId', Max35Text, False)

	@PrcgId.deleter
	def PrcgId(self):
		del self._PrcgId
		self._PrcgId = base_types.UninitialisedField(self, 'PrcgId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=PartyTextInformation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AltrnId', type=AlternatePartyIdentification10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=PartyIdentification245Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))