# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateFormat1
from . import ISODateTime
from . import Max35Text
from . import MeetingType4Code
from . import MeetingTypeClassification2Choice
from . import PartyIdentification129Choice
from . import PostalAddress1

class MeetingReference11(base_types._BaseFieldType):

	__slots__ = ["_Clssfctn", "_EntitlmntFxgDt", "_Issr", "_IssrMtgId", "_Lctn", "_MtgDtAndTm", "_MtgId", "_Tp"]
	@property
	def Clssfctn(self):
		return self._Clssfctn

	@Clssfctn.setter
	def Clssfctn(self, value):
		self._Clssfctn = value if value is not None else base_types.UninitialisedField(self, 'Clssfctn', MeetingTypeClassification2Choice, False)

	@Clssfctn.deleter
	def Clssfctn(self):
		del self._Clssfctn
		self._Clssfctn = base_types.UninitialisedField(self, 'Clssfctn', MeetingTypeClassification2Choice, False)

	@property
	def EntitlmntFxgDt(self):
		return self._EntitlmntFxgDt

	@EntitlmntFxgDt.setter
	def EntitlmntFxgDt(self, value):
		self._EntitlmntFxgDt = value if value is not None else base_types.UninitialisedField(self, 'EntitlmntFxgDt', DateFormat1, False)

	@EntitlmntFxgDt.deleter
	def EntitlmntFxgDt(self):
		del self._EntitlmntFxgDt
		self._EntitlmntFxgDt = base_types.UninitialisedField(self, 'EntitlmntFxgDt', DateFormat1, False)

	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if value is not None else base_types.UninitialisedField(self, 'Issr', PartyIdentification129Choice, False)

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = base_types.UninitialisedField(self, 'Issr', PartyIdentification129Choice, False)

	@property
	def IssrMtgId(self):
		return self._IssrMtgId

	@IssrMtgId.setter
	def IssrMtgId(self, value):
		self._IssrMtgId = value if value is not None else base_types.UninitialisedField(self, 'IssrMtgId', Max35Text, False)

	@IssrMtgId.deleter
	def IssrMtgId(self):
		del self._IssrMtgId
		self._IssrMtgId = base_types.UninitialisedField(self, 'IssrMtgId', Max35Text, False)

	@property
	def Lctn(self):
		return self._Lctn

	@Lctn.setter
	def Lctn(self, value):
		self._Lctn = value if value is not None else base_types.UninitialisedField(self, 'Lctn', PostalAddress1, True)

	@Lctn.deleter
	def Lctn(self):
		del self._Lctn
		self._Lctn = base_types.UninitialisedField(self, 'Lctn', PostalAddress1, True)

	@property
	def MtgDtAndTm(self):
		return self._MtgDtAndTm

	@MtgDtAndTm.setter
	def MtgDtAndTm(self, value):
		self._MtgDtAndTm = value if value is not None else base_types.UninitialisedField(self, 'MtgDtAndTm', ISODateTime, False)

	@MtgDtAndTm.deleter
	def MtgDtAndTm(self):
		del self._MtgDtAndTm
		self._MtgDtAndTm = base_types.UninitialisedField(self, 'MtgDtAndTm', ISODateTime, False)

	@property
	def MtgId(self):
		return self._MtgId

	@MtgId.setter
	def MtgId(self, value):
		self._MtgId = value if value is not None else base_types.UninitialisedField(self, 'MtgId', Max35Text, False)

	@MtgId.deleter
	def MtgId(self):
		del self._MtgId
		self._MtgId = base_types.UninitialisedField(self, 'MtgId', Max35Text, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', MeetingType4Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', MeetingType4Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Clssfctn', type=MeetingTypeClassification2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EntitlmntFxgDt', type=DateFormat1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Issr', type=PartyIdentification129Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrMtgId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lctn', type=PostalAddress1, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='MtgDtAndTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=MeetingType4Code, min=1, max=1, mutex_group=None, array=False),
	))