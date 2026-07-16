# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateEventNarrative4
from . import IssuerAgent3
from . import IssuerInformation3
from . import Meeting7
from . import MeetingEventReference1
from . import MeetingNotice10
from . import NotificationGeneralInformation4
from . import NotificationUpdate2
from . import Pagination1
from . import PowerOfAttorneyRequirements4
from . import Resolution8
from . import SecurityPosition20
from . import SupplementaryData1
from . import VoteParameters10

class MeetingNotificationV13(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_EvtsLkg", "_Issr", "_IssrAgt", "_Mtg", "_MtgDtls", "_NtfctnGnlInf", "_NtfctnUpd", "_Pgntn", "_PwrOfAttnyRqrmnts", "_Rsltn", "_Scty", "_SplmtryData", "_Vote"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', CorporateEventNarrative4, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', CorporateEventNarrative4, False)

	@property
	def EvtsLkg(self):
		return self._EvtsLkg

	@EvtsLkg.setter
	def EvtsLkg(self, value):
		self._EvtsLkg = value if value is not None else base_types.UninitialisedField(self, 'EvtsLkg', MeetingEventReference1, True)

	@EvtsLkg.deleter
	def EvtsLkg(self):
		del self._EvtsLkg
		self._EvtsLkg = base_types.UninitialisedField(self, 'EvtsLkg', MeetingEventReference1, True)

	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if value is not None else base_types.UninitialisedField(self, 'Issr', IssuerInformation3, False)

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = base_types.UninitialisedField(self, 'Issr', IssuerInformation3, False)

	@property
	def IssrAgt(self):
		return self._IssrAgt

	@IssrAgt.setter
	def IssrAgt(self, value):
		self._IssrAgt = value if value is not None else base_types.UninitialisedField(self, 'IssrAgt', IssuerAgent3, True)

	@IssrAgt.deleter
	def IssrAgt(self):
		del self._IssrAgt
		self._IssrAgt = base_types.UninitialisedField(self, 'IssrAgt', IssuerAgent3, True)

	@property
	def Mtg(self):
		return self._Mtg

	@Mtg.setter
	def Mtg(self, value):
		self._Mtg = value if value is not None else base_types.UninitialisedField(self, 'Mtg', MeetingNotice10, False)

	@Mtg.deleter
	def Mtg(self):
		del self._Mtg
		self._Mtg = base_types.UninitialisedField(self, 'Mtg', MeetingNotice10, False)

	@property
	def MtgDtls(self):
		return self._MtgDtls

	@MtgDtls.setter
	def MtgDtls(self, value):
		self._MtgDtls = value if value is not None else base_types.UninitialisedField(self, 'MtgDtls', Meeting7, True)

	@MtgDtls.deleter
	def MtgDtls(self):
		del self._MtgDtls
		self._MtgDtls = base_types.UninitialisedField(self, 'MtgDtls', Meeting7, True)

	@property
	def NtfctnGnlInf(self):
		return self._NtfctnGnlInf

	@NtfctnGnlInf.setter
	def NtfctnGnlInf(self, value):
		self._NtfctnGnlInf = value if value is not None else base_types.UninitialisedField(self, 'NtfctnGnlInf', NotificationGeneralInformation4, False)

	@NtfctnGnlInf.deleter
	def NtfctnGnlInf(self):
		del self._NtfctnGnlInf
		self._NtfctnGnlInf = base_types.UninitialisedField(self, 'NtfctnGnlInf', NotificationGeneralInformation4, False)

	@property
	def NtfctnUpd(self):
		return self._NtfctnUpd

	@NtfctnUpd.setter
	def NtfctnUpd(self, value):
		self._NtfctnUpd = value if value is not None else base_types.UninitialisedField(self, 'NtfctnUpd', NotificationUpdate2, False)

	@NtfctnUpd.deleter
	def NtfctnUpd(self):
		del self._NtfctnUpd
		self._NtfctnUpd = base_types.UninitialisedField(self, 'NtfctnUpd', NotificationUpdate2, False)

	@property
	def Pgntn(self):
		return self._Pgntn

	@Pgntn.setter
	def Pgntn(self, value):
		self._Pgntn = value if value is not None else base_types.UninitialisedField(self, 'Pgntn', Pagination1, False)

	@Pgntn.deleter
	def Pgntn(self):
		del self._Pgntn
		self._Pgntn = base_types.UninitialisedField(self, 'Pgntn', Pagination1, False)

	@property
	def PwrOfAttnyRqrmnts(self):
		return self._PwrOfAttnyRqrmnts

	@PwrOfAttnyRqrmnts.setter
	def PwrOfAttnyRqrmnts(self, value):
		self._PwrOfAttnyRqrmnts = value if value is not None else base_types.UninitialisedField(self, 'PwrOfAttnyRqrmnts', PowerOfAttorneyRequirements4, False)

	@PwrOfAttnyRqrmnts.deleter
	def PwrOfAttnyRqrmnts(self):
		del self._PwrOfAttnyRqrmnts
		self._PwrOfAttnyRqrmnts = base_types.UninitialisedField(self, 'PwrOfAttnyRqrmnts', PowerOfAttorneyRequirements4, False)

	@property
	def Rsltn(self):
		return self._Rsltn

	@Rsltn.setter
	def Rsltn(self, value):
		self._Rsltn = value if value is not None else base_types.UninitialisedField(self, 'Rsltn', Resolution8, True)

	@Rsltn.deleter
	def Rsltn(self):
		del self._Rsltn
		self._Rsltn = base_types.UninitialisedField(self, 'Rsltn', Resolution8, True)

	@property
	def Scty(self):
		return self._Scty

	@Scty.setter
	def Scty(self, value):
		self._Scty = value if value is not None else base_types.UninitialisedField(self, 'Scty', SecurityPosition20, True)

	@Scty.deleter
	def Scty(self):
		del self._Scty
		self._Scty = base_types.UninitialisedField(self, 'Scty', SecurityPosition20, True)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@property
	def Vote(self):
		return self._Vote

	@Vote.setter
	def Vote(self, value):
		self._Vote = value if value is not None else base_types.UninitialisedField(self, 'Vote', VoteParameters10, False)

	@Vote.deleter
	def Vote(self):
		del self._Vote
		self._Vote = base_types.UninitialisedField(self, 'Vote', VoteParameters10, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=CorporateEventNarrative4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtsLkg', type=MeetingEventReference1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Issr', type=IssuerInformation3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrAgt', type=IssuerAgent3, min=0, max=10, mutex_group=None, array=True),
		base_types.FieldEntry(name='Mtg', type=MeetingNotice10, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtgDtls', type=Meeting7, min=1, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='NtfctnGnlInf', type=NotificationGeneralInformation4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtfctnUpd', type=NotificationUpdate2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pgntn', type=Pagination1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PwrOfAttnyRqrmnts', type=PowerOfAttorneyRequirements4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsltn', type=Resolution8, min=0, max=1000, mutex_group=None, array=True),
		base_types.FieldEntry(name='Scty', type=SecurityPosition20, min=1, max=200, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Vote', type=VoteParameters10, min=0, max=1, mutex_group=None, array=False),
	))