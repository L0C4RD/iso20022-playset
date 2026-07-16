# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATICALaxProcessing
from . import Exact3NumericText
from . import ISO3NumericCountryCode
from . import ISOYearMonth
from . import Max104Text
from . import Max10Text
from . import Max19NumericText
from . import Max35Text
from . import Max76Text
from . import Min2Max3NumericText
from . import Track2Data1Choice
from . import TrueFalseIndicator

class CardData16(base_types._BaseFieldType):

	__slots__ = ["_AcctFndgSrc", "_Brnd", "_CardSeqNb", "_Ctry", "_FctvDt", "_IsseDt", "_NtlData", "_PAN", "_PANAcctRg", "_PdctSubTp", "_PdctTp", "_PmtAcctRef", "_PrtctdPAN", "_PrtflIdr", "_PrvtData", "_Schme", "_Sgmt", "_SvcCd", "_Trck1", "_Trck2", "_Trck3", "_XpryDt"]
	@property
	def AcctFndgSrc(self):
		return self._AcctFndgSrc

	@AcctFndgSrc.setter
	def AcctFndgSrc(self, value):
		self._AcctFndgSrc = value if value is not None else base_types.UninitialisedField(self, 'AcctFndgSrc', Max10Text, False)

	@AcctFndgSrc.deleter
	def AcctFndgSrc(self):
		del self._AcctFndgSrc
		self._AcctFndgSrc = base_types.UninitialisedField(self, 'AcctFndgSrc', Max10Text, False)

	@property
	def Brnd(self):
		return self._Brnd

	@Brnd.setter
	def Brnd(self, value):
		self._Brnd = value if value is not None else base_types.UninitialisedField(self, 'Brnd', Max35Text, False)

	@Brnd.deleter
	def Brnd(self):
		del self._Brnd
		self._Brnd = base_types.UninitialisedField(self, 'Brnd', Max35Text, False)

	@property
	def CardSeqNb(self):
		return self._CardSeqNb

	@CardSeqNb.setter
	def CardSeqNb(self, value):
		self._CardSeqNb = value if value is not None else base_types.UninitialisedField(self, 'CardSeqNb', Min2Max3NumericText, False)

	@CardSeqNb.deleter
	def CardSeqNb(self):
		del self._CardSeqNb
		self._CardSeqNb = base_types.UninitialisedField(self, 'CardSeqNb', Min2Max3NumericText, False)

	@property
	def Ctry(self):
		return self._Ctry

	@Ctry.setter
	def Ctry(self, value):
		self._Ctry = value if value is not None else base_types.UninitialisedField(self, 'Ctry', ISO3NumericCountryCode, False)

	@Ctry.deleter
	def Ctry(self):
		del self._Ctry
		self._Ctry = base_types.UninitialisedField(self, 'Ctry', ISO3NumericCountryCode, False)

	@property
	def FctvDt(self):
		return self._FctvDt

	@FctvDt.setter
	def FctvDt(self, value):
		self._FctvDt = value if value is not None else base_types.UninitialisedField(self, 'FctvDt', ISOYearMonth, False)

	@FctvDt.deleter
	def FctvDt(self):
		del self._FctvDt
		self._FctvDt = base_types.UninitialisedField(self, 'FctvDt', ISOYearMonth, False)

	@property
	def IsseDt(self):
		return self._IsseDt

	@IsseDt.setter
	def IsseDt(self, value):
		self._IsseDt = value if value is not None else base_types.UninitialisedField(self, 'IsseDt', ISOYearMonth, False)

	@IsseDt.deleter
	def IsseDt(self):
		del self._IsseDt
		self._IsseDt = base_types.UninitialisedField(self, 'IsseDt', ISOYearMonth, False)

	@property
	def NtlData(self):
		return self._NtlData

	@NtlData.setter
	def NtlData(self, value):
		self._NtlData = value if value is not None else base_types.UninitialisedField(self, 'NtlData', ATICALaxProcessing, True)

	@NtlData.deleter
	def NtlData(self):
		del self._NtlData
		self._NtlData = base_types.UninitialisedField(self, 'NtlData', ATICALaxProcessing, True)

	@property
	def PAN(self):
		return self._PAN

	@PAN.setter
	def PAN(self, value):
		self._PAN = value if value is not None else base_types.UninitialisedField(self, 'PAN', Max19NumericText, False)

	@PAN.deleter
	def PAN(self):
		del self._PAN
		self._PAN = base_types.UninitialisedField(self, 'PAN', Max19NumericText, False)

	@property
	def PANAcctRg(self):
		return self._PANAcctRg

	@PANAcctRg.setter
	def PANAcctRg(self, value):
		self._PANAcctRg = value if value is not None else base_types.UninitialisedField(self, 'PANAcctRg', Max19NumericText, False)

	@PANAcctRg.deleter
	def PANAcctRg(self):
		del self._PANAcctRg
		self._PANAcctRg = base_types.UninitialisedField(self, 'PANAcctRg', Max19NumericText, False)

	@property
	def PdctSubTp(self):
		return self._PdctSubTp

	@PdctSubTp.setter
	def PdctSubTp(self, value):
		self._PdctSubTp = value if value is not None else base_types.UninitialisedField(self, 'PdctSubTp', Max35Text, False)

	@PdctSubTp.deleter
	def PdctSubTp(self):
		del self._PdctSubTp
		self._PdctSubTp = base_types.UninitialisedField(self, 'PdctSubTp', Max35Text, False)

	@property
	def PdctTp(self):
		return self._PdctTp

	@PdctTp.setter
	def PdctTp(self, value):
		self._PdctTp = value if value is not None else base_types.UninitialisedField(self, 'PdctTp', Max35Text, False)

	@PdctTp.deleter
	def PdctTp(self):
		del self._PdctTp
		self._PdctTp = base_types.UninitialisedField(self, 'PdctTp', Max35Text, False)

	@property
	def PmtAcctRef(self):
		return self._PmtAcctRef

	@PmtAcctRef.setter
	def PmtAcctRef(self, value):
		self._PmtAcctRef = value if value is not None else base_types.UninitialisedField(self, 'PmtAcctRef', Max35Text, False)

	@PmtAcctRef.deleter
	def PmtAcctRef(self):
		del self._PmtAcctRef
		self._PmtAcctRef = base_types.UninitialisedField(self, 'PmtAcctRef', Max35Text, False)

	@property
	def PrtctdPAN(self):
		return self._PrtctdPAN

	@PrtctdPAN.setter
	def PrtctdPAN(self, value):
		self._PrtctdPAN = value if value is not None else base_types.UninitialisedField(self, 'PrtctdPAN', TrueFalseIndicator, False)

	@PrtctdPAN.deleter
	def PrtctdPAN(self):
		del self._PrtctdPAN
		self._PrtctdPAN = base_types.UninitialisedField(self, 'PrtctdPAN', TrueFalseIndicator, False)

	@property
	def PrtflIdr(self):
		return self._PrtflIdr

	@PrtflIdr.setter
	def PrtflIdr(self, value):
		self._PrtflIdr = value if value is not None else base_types.UninitialisedField(self, 'PrtflIdr', Max35Text, False)

	@PrtflIdr.deleter
	def PrtflIdr(self):
		del self._PrtflIdr
		self._PrtflIdr = base_types.UninitialisedField(self, 'PrtflIdr', Max35Text, False)

	@property
	def PrvtData(self):
		return self._PrvtData

	@PrvtData.setter
	def PrvtData(self, value):
		self._PrvtData = value if value is not None else base_types.UninitialisedField(self, 'PrvtData', ATICALaxProcessing, True)

	@PrvtData.deleter
	def PrvtData(self):
		del self._PrvtData
		self._PrvtData = base_types.UninitialisedField(self, 'PrvtData', ATICALaxProcessing, True)

	@property
	def Schme(self):
		return self._Schme

	@Schme.setter
	def Schme(self, value):
		self._Schme = value if value is not None else base_types.UninitialisedField(self, 'Schme', Max35Text, False)

	@Schme.deleter
	def Schme(self):
		del self._Schme
		self._Schme = base_types.UninitialisedField(self, 'Schme', Max35Text, False)

	@property
	def Sgmt(self):
		return self._Sgmt

	@Sgmt.setter
	def Sgmt(self, value):
		self._Sgmt = value if value is not None else base_types.UninitialisedField(self, 'Sgmt', Max10Text, False)

	@Sgmt.deleter
	def Sgmt(self):
		del self._Sgmt
		self._Sgmt = base_types.UninitialisedField(self, 'Sgmt', Max10Text, False)

	@property
	def SvcCd(self):
		return self._SvcCd

	@SvcCd.setter
	def SvcCd(self, value):
		self._SvcCd = value if value is not None else base_types.UninitialisedField(self, 'SvcCd', Exact3NumericText, False)

	@SvcCd.deleter
	def SvcCd(self):
		del self._SvcCd
		self._SvcCd = base_types.UninitialisedField(self, 'SvcCd', Exact3NumericText, False)

	@property
	def Trck1(self):
		return self._Trck1

	@Trck1.setter
	def Trck1(self, value):
		self._Trck1 = value if value is not None else base_types.UninitialisedField(self, 'Trck1', Max76Text, False)

	@Trck1.deleter
	def Trck1(self):
		del self._Trck1
		self._Trck1 = base_types.UninitialisedField(self, 'Trck1', Max76Text, False)

	@property
	def Trck2(self):
		return self._Trck2

	@Trck2.setter
	def Trck2(self, value):
		self._Trck2 = value if value is not None else base_types.UninitialisedField(self, 'Trck2', Track2Data1Choice, False)

	@Trck2.deleter
	def Trck2(self):
		del self._Trck2
		self._Trck2 = base_types.UninitialisedField(self, 'Trck2', Track2Data1Choice, False)

	@property
	def Trck3(self):
		return self._Trck3

	@Trck3.setter
	def Trck3(self, value):
		self._Trck3 = value if value is not None else base_types.UninitialisedField(self, 'Trck3', Max104Text, False)

	@Trck3.deleter
	def Trck3(self):
		del self._Trck3
		self._Trck3 = base_types.UninitialisedField(self, 'Trck3', Max104Text, False)

	@property
	def XpryDt(self):
		return self._XpryDt

	@XpryDt.setter
	def XpryDt(self, value):
		self._XpryDt = value if value is not None else base_types.UninitialisedField(self, 'XpryDt', ISOYearMonth, False)

	@XpryDt.deleter
	def XpryDt(self):
		del self._XpryDt
		self._XpryDt = base_types.UninitialisedField(self, 'XpryDt', ISOYearMonth, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctFndgSrc', type=Max10Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Brnd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardSeqNb', type=Min2Max3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctry', type=ISO3NumericCountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FctvDt', type=ISOYearMonth, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IsseDt', type=ISOYearMonth, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtlData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PAN', type=Max19NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PANAcctRg', type=Max19NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctSubTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtAcctRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdPAN', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtflIdr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvtData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Schme', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sgmt', type=Max10Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcCd', type=Exact3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Trck1', type=Max76Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Trck2', type=Track2Data1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Trck3', type=Max104Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpryDt', type=ISOYearMonth, min=0, max=1, mutex_group=None, array=False),
	))