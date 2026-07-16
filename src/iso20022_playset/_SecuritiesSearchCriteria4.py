# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyCode
from . import CFIOct2015Identifier
from . import CountryCode
from . import DatePeriodSearch1Choice
from . import SecurityIdentification39
from . import SecurityStatus3Choice
from . import SystemPartyIdentification2Choice

class SecuritiesSearchCriteria4(base_types._BaseFieldType):

	__slots__ = ["_CSD", "_ClssfctnFinInstrm", "_CtryOfIsse", "_FinInstrmId", "_InvstrCSD", "_IsseCcy", "_IsseDt", "_IssrCSD", "_MntngCSD", "_MtrtyDt", "_SctySts", "_TechIssrCSD"]
	@property
	def CSD(self):
		return self._CSD

	@CSD.setter
	def CSD(self, value):
		self._CSD = value if value is not None else base_types.UninitialisedField(self, 'CSD', SystemPartyIdentification2Choice, False)

	@CSD.deleter
	def CSD(self):
		del self._CSD
		self._CSD = base_types.UninitialisedField(self, 'CSD', SystemPartyIdentification2Choice, False)

	@property
	def ClssfctnFinInstrm(self):
		return self._ClssfctnFinInstrm

	@ClssfctnFinInstrm.setter
	def ClssfctnFinInstrm(self, value):
		self._ClssfctnFinInstrm = value if value is not None else base_types.UninitialisedField(self, 'ClssfctnFinInstrm', CFIOct2015Identifier, False)

	@ClssfctnFinInstrm.deleter
	def ClssfctnFinInstrm(self):
		del self._ClssfctnFinInstrm
		self._ClssfctnFinInstrm = base_types.UninitialisedField(self, 'ClssfctnFinInstrm', CFIOct2015Identifier, False)

	@property
	def CtryOfIsse(self):
		return self._CtryOfIsse

	@CtryOfIsse.setter
	def CtryOfIsse(self, value):
		self._CtryOfIsse = value if value is not None else base_types.UninitialisedField(self, 'CtryOfIsse', CountryCode, False)

	@CtryOfIsse.deleter
	def CtryOfIsse(self):
		del self._CtryOfIsse
		self._CtryOfIsse = base_types.UninitialisedField(self, 'CtryOfIsse', CountryCode, False)

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification39, False)

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification39, False)

	@property
	def InvstrCSD(self):
		return self._InvstrCSD

	@InvstrCSD.setter
	def InvstrCSD(self, value):
		self._InvstrCSD = value if value is not None else base_types.UninitialisedField(self, 'InvstrCSD', SystemPartyIdentification2Choice, False)

	@InvstrCSD.deleter
	def InvstrCSD(self):
		del self._InvstrCSD
		self._InvstrCSD = base_types.UninitialisedField(self, 'InvstrCSD', SystemPartyIdentification2Choice, False)

	@property
	def IsseCcy(self):
		return self._IsseCcy

	@IsseCcy.setter
	def IsseCcy(self, value):
		self._IsseCcy = value if value is not None else base_types.UninitialisedField(self, 'IsseCcy', ActiveOrHistoricCurrencyCode, False)

	@IsseCcy.deleter
	def IsseCcy(self):
		del self._IsseCcy
		self._IsseCcy = base_types.UninitialisedField(self, 'IsseCcy', ActiveOrHistoricCurrencyCode, False)

	@property
	def IsseDt(self):
		return self._IsseDt

	@IsseDt.setter
	def IsseDt(self, value):
		self._IsseDt = value if value is not None else base_types.UninitialisedField(self, 'IsseDt', DatePeriodSearch1Choice, False)

	@IsseDt.deleter
	def IsseDt(self):
		del self._IsseDt
		self._IsseDt = base_types.UninitialisedField(self, 'IsseDt', DatePeriodSearch1Choice, False)

	@property
	def IssrCSD(self):
		return self._IssrCSD

	@IssrCSD.setter
	def IssrCSD(self, value):
		self._IssrCSD = value if value is not None else base_types.UninitialisedField(self, 'IssrCSD', SystemPartyIdentification2Choice, False)

	@IssrCSD.deleter
	def IssrCSD(self):
		del self._IssrCSD
		self._IssrCSD = base_types.UninitialisedField(self, 'IssrCSD', SystemPartyIdentification2Choice, False)

	@property
	def MntngCSD(self):
		return self._MntngCSD

	@MntngCSD.setter
	def MntngCSD(self, value):
		self._MntngCSD = value if value is not None else base_types.UninitialisedField(self, 'MntngCSD', SystemPartyIdentification2Choice, False)

	@MntngCSD.deleter
	def MntngCSD(self):
		del self._MntngCSD
		self._MntngCSD = base_types.UninitialisedField(self, 'MntngCSD', SystemPartyIdentification2Choice, False)

	@property
	def MtrtyDt(self):
		return self._MtrtyDt

	@MtrtyDt.setter
	def MtrtyDt(self, value):
		self._MtrtyDt = value if value is not None else base_types.UninitialisedField(self, 'MtrtyDt', DatePeriodSearch1Choice, False)

	@MtrtyDt.deleter
	def MtrtyDt(self):
		del self._MtrtyDt
		self._MtrtyDt = base_types.UninitialisedField(self, 'MtrtyDt', DatePeriodSearch1Choice, False)

	@property
	def SctySts(self):
		return self._SctySts

	@SctySts.setter
	def SctySts(self, value):
		self._SctySts = value if value is not None else base_types.UninitialisedField(self, 'SctySts', SecurityStatus3Choice, False)

	@SctySts.deleter
	def SctySts(self):
		del self._SctySts
		self._SctySts = base_types.UninitialisedField(self, 'SctySts', SecurityStatus3Choice, False)

	@property
	def TechIssrCSD(self):
		return self._TechIssrCSD

	@TechIssrCSD.setter
	def TechIssrCSD(self, value):
		self._TechIssrCSD = value if value is not None else base_types.UninitialisedField(self, 'TechIssrCSD', SystemPartyIdentification2Choice, False)

	@TechIssrCSD.deleter
	def TechIssrCSD(self):
		del self._TechIssrCSD
		self._TechIssrCSD = base_types.UninitialisedField(self, 'TechIssrCSD', SystemPartyIdentification2Choice, False)

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