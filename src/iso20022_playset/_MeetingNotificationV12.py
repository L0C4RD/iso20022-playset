from . import base_types
from ._VoteParameters9 import VoteParameters9
from ._SupplementaryData1 import SupplementaryData1
from ._Resolution8 import Resolution8
from ._MeetingEventReference1 import MeetingEventReference1
from ._SecurityPosition20 import SecurityPosition20
from ._NotificationUpdate2 import NotificationUpdate2
from ._IssuerAgent3 import IssuerAgent3
from ._MeetingNotice9 import MeetingNotice9
from ._PowerOfAttorneyRequirements4 import PowerOfAttorneyRequirements4
from ._CorporateEventNarrative4 import CorporateEventNarrative4
from ._Meeting7 import Meeting7
from ._NotificationGeneralInformation4 import NotificationGeneralInformation4
from ._Pagination1 import Pagination1
from ._IssuerInformation3 import IssuerInformation3

class MeetingNotificationV12(base_types._BaseFieldType):

	__slots__ = ["_NtfctnUpd", "_IssrAgt", "_AddtlInf", "_Mtg", "_Scty", "_Vote", "_Rsltn", "_PwrOfAttnyRqrmnts", "_MtgDtls", "_Issr", "_EvtsLkg", "_SplmtryData", "_Pgntn", "_NtfctnGnlInf"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != base_types.auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def EvtsLkg(self):
		return self._EvtsLkg

	@EvtsLkg.setter
	def EvtsLkg(self, value):
		self._EvtsLkg = value if type(value) != base_types.auto else self.make_default("EvtsLkg")

	@EvtsLkg.deleter
	def EvtsLkg(self):
		del self._EvtsLkg
		self._EvtsLkg = None

	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if type(value) != base_types.auto else self.make_default("Issr")

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = None

	@property
	def IssrAgt(self):
		return self._IssrAgt

	@IssrAgt.setter
	def IssrAgt(self, value):
		self._IssrAgt = value if type(value) != base_types.auto else self.make_default("IssrAgt")

	@IssrAgt.deleter
	def IssrAgt(self):
		del self._IssrAgt
		self._IssrAgt = None

	@property
	def Mtg(self):
		return self._Mtg

	@Mtg.setter
	def Mtg(self, value):
		self._Mtg = value if type(value) != base_types.auto else self.make_default("Mtg")

	@Mtg.deleter
	def Mtg(self):
		del self._Mtg
		self._Mtg = None

	@property
	def MtgDtls(self):
		return self._MtgDtls

	@MtgDtls.setter
	def MtgDtls(self, value):
		self._MtgDtls = value if type(value) != base_types.auto else self.make_default("MtgDtls")

	@MtgDtls.deleter
	def MtgDtls(self):
		del self._MtgDtls
		self._MtgDtls = None

	@property
	def NtfctnGnlInf(self):
		return self._NtfctnGnlInf

	@NtfctnGnlInf.setter
	def NtfctnGnlInf(self, value):
		self._NtfctnGnlInf = value if type(value) != base_types.auto else self.make_default("NtfctnGnlInf")

	@NtfctnGnlInf.deleter
	def NtfctnGnlInf(self):
		del self._NtfctnGnlInf
		self._NtfctnGnlInf = None

	@property
	def NtfctnUpd(self):
		return self._NtfctnUpd

	@NtfctnUpd.setter
	def NtfctnUpd(self, value):
		self._NtfctnUpd = value if type(value) != base_types.auto else self.make_default("NtfctnUpd")

	@NtfctnUpd.deleter
	def NtfctnUpd(self):
		del self._NtfctnUpd
		self._NtfctnUpd = None

	@property
	def Pgntn(self):
		return self._Pgntn

	@Pgntn.setter
	def Pgntn(self, value):
		self._Pgntn = value if type(value) != base_types.auto else self.make_default("Pgntn")

	@Pgntn.deleter
	def Pgntn(self):
		del self._Pgntn
		self._Pgntn = None

	@property
	def PwrOfAttnyRqrmnts(self):
		return self._PwrOfAttnyRqrmnts

	@PwrOfAttnyRqrmnts.setter
	def PwrOfAttnyRqrmnts(self, value):
		self._PwrOfAttnyRqrmnts = value if type(value) != base_types.auto else self.make_default("PwrOfAttnyRqrmnts")

	@PwrOfAttnyRqrmnts.deleter
	def PwrOfAttnyRqrmnts(self):
		del self._PwrOfAttnyRqrmnts
		self._PwrOfAttnyRqrmnts = None

	@property
	def Rsltn(self):
		return self._Rsltn

	@Rsltn.setter
	def Rsltn(self, value):
		self._Rsltn = value if type(value) != base_types.auto else self.make_default("Rsltn")

	@Rsltn.deleter
	def Rsltn(self):
		del self._Rsltn
		self._Rsltn = None

	@property
	def Scty(self):
		return self._Scty

	@Scty.setter
	def Scty(self, value):
		self._Scty = value if type(value) != base_types.auto else self.make_default("Scty")

	@Scty.deleter
	def Scty(self):
		del self._Scty
		self._Scty = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def Vote(self):
		return self._Vote

	@Vote.setter
	def Vote(self, value):
		self._Vote = value if type(value) != base_types.auto else self.make_default("Vote")

	@Vote.deleter
	def Vote(self):
		del self._Vote
		self._Vote = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=CorporateEventNarrative4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtsLkg', type=MeetingEventReference1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Issr', type=IssuerInformation3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrAgt', type=IssuerAgent3, min=0, max=10, mutex_group=None, array=True),
		base_types.FieldEntry(name='Mtg', type=MeetingNotice9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtgDtls', type=Meeting7, min=1, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='NtfctnGnlInf', type=NotificationGeneralInformation4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtfctnUpd', type=NotificationUpdate2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pgntn', type=Pagination1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PwrOfAttnyRqrmnts', type=PowerOfAttorneyRequirements4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsltn', type=Resolution8, min=0, max=1000, mutex_group=None, array=True),
		base_types.FieldEntry(name='Scty', type=SecurityPosition20, min=1, max=200, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Vote', type=VoteParameters9, min=0, max=1, mutex_group=None, array=False),
	))

