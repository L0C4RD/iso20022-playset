from . import base_types
from ._ActiveOrHistoricCurrencyCode import ActiveOrHistoricCurrencyCode
from ._CFIOct2015Identifier import CFIOct2015Identifier
from ._CountryCode import CountryCode
from ._DatePeriodSearch1Choice import DatePeriodSearch1Choice
from ._SecurityIdentification39 import SecurityIdentification39
from ._SecurityStatus3Choice import SecurityStatus3Choice
from ._SystemPartyIdentification2Choice import SystemPartyIdentification2Choice

class SecuritiesSearchCriteria4(base_types._BaseFieldType):

	__slots__ = ["_CSD", "_ClssfctnFinInstrm", "_CtryOfIsse", "_FinInstrmId", "_InvstrCSD", "_IsseCcy", "_IsseDt", "_IssrCSD", "_MntngCSD", "_MtrtyDt", "_SctySts", "_TechIssrCSD"]
	@property
	def CSD(self):
		return self._CSD

	@CSD.setter
	def CSD(self, value):
		self._CSD = value if type(value) != base_types.auto else self.make_default("CSD")

	@CSD.deleter
	def CSD(self):
		del self._CSD
		self._CSD = None

	@property
	def ClssfctnFinInstrm(self):
		return self._ClssfctnFinInstrm

	@ClssfctnFinInstrm.setter
	def ClssfctnFinInstrm(self, value):
		self._ClssfctnFinInstrm = value if type(value) != base_types.auto else self.make_default("ClssfctnFinInstrm")

	@ClssfctnFinInstrm.deleter
	def ClssfctnFinInstrm(self):
		del self._ClssfctnFinInstrm
		self._ClssfctnFinInstrm = None

	@property
	def CtryOfIsse(self):
		return self._CtryOfIsse

	@CtryOfIsse.setter
	def CtryOfIsse(self, value):
		self._CtryOfIsse = value if type(value) != base_types.auto else self.make_default("CtryOfIsse")

	@CtryOfIsse.deleter
	def CtryOfIsse(self):
		del self._CtryOfIsse
		self._CtryOfIsse = None

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if type(value) != base_types.auto else self.make_default("FinInstrmId")

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = None

	@property
	def InvstrCSD(self):
		return self._InvstrCSD

	@InvstrCSD.setter
	def InvstrCSD(self, value):
		self._InvstrCSD = value if type(value) != base_types.auto else self.make_default("InvstrCSD")

	@InvstrCSD.deleter
	def InvstrCSD(self):
		del self._InvstrCSD
		self._InvstrCSD = None

	@property
	def IsseCcy(self):
		return self._IsseCcy

	@IsseCcy.setter
	def IsseCcy(self, value):
		self._IsseCcy = value if type(value) != base_types.auto else self.make_default("IsseCcy")

	@IsseCcy.deleter
	def IsseCcy(self):
		del self._IsseCcy
		self._IsseCcy = None

	@property
	def IsseDt(self):
		return self._IsseDt

	@IsseDt.setter
	def IsseDt(self, value):
		self._IsseDt = value if type(value) != base_types.auto else self.make_default("IsseDt")

	@IsseDt.deleter
	def IsseDt(self):
		del self._IsseDt
		self._IsseDt = None

	@property
	def IssrCSD(self):
		return self._IssrCSD

	@IssrCSD.setter
	def IssrCSD(self, value):
		self._IssrCSD = value if type(value) != base_types.auto else self.make_default("IssrCSD")

	@IssrCSD.deleter
	def IssrCSD(self):
		del self._IssrCSD
		self._IssrCSD = None

	@property
	def MntngCSD(self):
		return self._MntngCSD

	@MntngCSD.setter
	def MntngCSD(self, value):
		self._MntngCSD = value if type(value) != base_types.auto else self.make_default("MntngCSD")

	@MntngCSD.deleter
	def MntngCSD(self):
		del self._MntngCSD
		self._MntngCSD = None

	@property
	def MtrtyDt(self):
		return self._MtrtyDt

	@MtrtyDt.setter
	def MtrtyDt(self, value):
		self._MtrtyDt = value if type(value) != base_types.auto else self.make_default("MtrtyDt")

	@MtrtyDt.deleter
	def MtrtyDt(self):
		del self._MtrtyDt
		self._MtrtyDt = None

	@property
	def SctySts(self):
		return self._SctySts

	@SctySts.setter
	def SctySts(self, value):
		self._SctySts = value if type(value) != base_types.auto else self.make_default("SctySts")

	@SctySts.deleter
	def SctySts(self):
		del self._SctySts
		self._SctySts = None

	@property
	def TechIssrCSD(self):
		return self._TechIssrCSD

	@TechIssrCSD.setter
	def TechIssrCSD(self, value):
		self._TechIssrCSD = value if type(value) != base_types.auto else self.make_default("TechIssrCSD")

	@TechIssrCSD.deleter
	def TechIssrCSD(self):
		del self._TechIssrCSD
		self._TechIssrCSD = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CSD', type=SystemPartyIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClssfctnFinInstrm', type=CFIOct2015Identifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryOfIsse', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification39, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstrCSD', type=SystemPartyIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IsseCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IsseDt', type=DatePeriodSearch1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrCSD', type=SystemPartyIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MntngCSD', type=SystemPartyIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtrtyDt', type=DatePeriodSearch1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctySts', type=SecurityStatus3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TechIssrCSD', type=SystemPartyIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
	))

