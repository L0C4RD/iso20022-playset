from . import base_types
from ._ATICALaxProcessing import ATICALaxProcessing
from ._ISO3NumericCountryCode import ISO3NumericCountryCode
from ._ISO3NumericCurrencyCode import ISO3NumericCurrencyCode
from ._ISOYearMonth import ISOYearMonth
from ._Max104Text import Max104Text
from ._Max10Text import Max10Text
from ._Max19NumericText import Max19NumericText
from ._Max35Text import Max35Text
from ._Max4NumericText import Max4NumericText
from ._Min2Max3NumericText import Min2Max3NumericText
from ._TrueFalseIndicator import TrueFalseIndicator

class CardData17(base_types._BaseFieldType):

	__slots__ = ["_AcctFndgSrc", "_Brnd", "_CardSeqNb", "_Ccy", "_Ctry", "_FctvDt", "_IsseDt", "_NtlData", "_PAN", "_PANAcctRg", "_PANFourLastDgts", "_PANRefIdr", "_PdctSubTp", "_PdctTp", "_PmtAcctRef", "_PrtctdPAN", "_PrtflIdr", "_PrvtData", "_Schme", "_Sgmt", "_Trck3", "_XpryDt"]
	@property
	def AcctFndgSrc(self):
		return self._AcctFndgSrc

	@AcctFndgSrc.setter
	def AcctFndgSrc(self, value):
		self._AcctFndgSrc = value if type(value) != base_types.auto else self.make_default("AcctFndgSrc")

	@AcctFndgSrc.deleter
	def AcctFndgSrc(self):
		del self._AcctFndgSrc
		self._AcctFndgSrc = None

	@property
	def Brnd(self):
		return self._Brnd

	@Brnd.setter
	def Brnd(self, value):
		self._Brnd = value if type(value) != base_types.auto else self.make_default("Brnd")

	@Brnd.deleter
	def Brnd(self):
		del self._Brnd
		self._Brnd = None

	@property
	def CardSeqNb(self):
		return self._CardSeqNb

	@CardSeqNb.setter
	def CardSeqNb(self, value):
		self._CardSeqNb = value if type(value) != base_types.auto else self.make_default("CardSeqNb")

	@CardSeqNb.deleter
	def CardSeqNb(self):
		del self._CardSeqNb
		self._CardSeqNb = None

	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if type(value) != base_types.auto else self.make_default("Ccy")

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = None

	@property
	def Ctry(self):
		return self._Ctry

	@Ctry.setter
	def Ctry(self, value):
		self._Ctry = value if type(value) != base_types.auto else self.make_default("Ctry")

	@Ctry.deleter
	def Ctry(self):
		del self._Ctry
		self._Ctry = None

	@property
	def FctvDt(self):
		return self._FctvDt

	@FctvDt.setter
	def FctvDt(self, value):
		self._FctvDt = value if type(value) != base_types.auto else self.make_default("FctvDt")

	@FctvDt.deleter
	def FctvDt(self):
		del self._FctvDt
		self._FctvDt = None

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
	def NtlData(self):
		return self._NtlData

	@NtlData.setter
	def NtlData(self, value):
		self._NtlData = value if type(value) != base_types.auto else self.make_default("NtlData")

	@NtlData.deleter
	def NtlData(self):
		del self._NtlData
		self._NtlData = None

	@property
	def PAN(self):
		return self._PAN

	@PAN.setter
	def PAN(self, value):
		self._PAN = value if type(value) != base_types.auto else self.make_default("PAN")

	@PAN.deleter
	def PAN(self):
		del self._PAN
		self._PAN = None

	@property
	def PANAcctRg(self):
		return self._PANAcctRg

	@PANAcctRg.setter
	def PANAcctRg(self, value):
		self._PANAcctRg = value if type(value) != base_types.auto else self.make_default("PANAcctRg")

	@PANAcctRg.deleter
	def PANAcctRg(self):
		del self._PANAcctRg
		self._PANAcctRg = None

	@property
	def PANFourLastDgts(self):
		return self._PANFourLastDgts

	@PANFourLastDgts.setter
	def PANFourLastDgts(self, value):
		self._PANFourLastDgts = value if type(value) != base_types.auto else self.make_default("PANFourLastDgts")

	@PANFourLastDgts.deleter
	def PANFourLastDgts(self):
		del self._PANFourLastDgts
		self._PANFourLastDgts = None

	@property
	def PANRefIdr(self):
		return self._PANRefIdr

	@PANRefIdr.setter
	def PANRefIdr(self, value):
		self._PANRefIdr = value if type(value) != base_types.auto else self.make_default("PANRefIdr")

	@PANRefIdr.deleter
	def PANRefIdr(self):
		del self._PANRefIdr
		self._PANRefIdr = None

	@property
	def PdctSubTp(self):
		return self._PdctSubTp

	@PdctSubTp.setter
	def PdctSubTp(self, value):
		self._PdctSubTp = value if type(value) != base_types.auto else self.make_default("PdctSubTp")

	@PdctSubTp.deleter
	def PdctSubTp(self):
		del self._PdctSubTp
		self._PdctSubTp = None

	@property
	def PdctTp(self):
		return self._PdctTp

	@PdctTp.setter
	def PdctTp(self, value):
		self._PdctTp = value if type(value) != base_types.auto else self.make_default("PdctTp")

	@PdctTp.deleter
	def PdctTp(self):
		del self._PdctTp
		self._PdctTp = None

	@property
	def PmtAcctRef(self):
		return self._PmtAcctRef

	@PmtAcctRef.setter
	def PmtAcctRef(self, value):
		self._PmtAcctRef = value if type(value) != base_types.auto else self.make_default("PmtAcctRef")

	@PmtAcctRef.deleter
	def PmtAcctRef(self):
		del self._PmtAcctRef
		self._PmtAcctRef = None

	@property
	def PrtctdPAN(self):
		return self._PrtctdPAN

	@PrtctdPAN.setter
	def PrtctdPAN(self, value):
		self._PrtctdPAN = value if type(value) != base_types.auto else self.make_default("PrtctdPAN")

	@PrtctdPAN.deleter
	def PrtctdPAN(self):
		del self._PrtctdPAN
		self._PrtctdPAN = None

	@property
	def PrtflIdr(self):
		return self._PrtflIdr

	@PrtflIdr.setter
	def PrtflIdr(self, value):
		self._PrtflIdr = value if type(value) != base_types.auto else self.make_default("PrtflIdr")

	@PrtflIdr.deleter
	def PrtflIdr(self):
		del self._PrtflIdr
		self._PrtflIdr = None

	@property
	def PrvtData(self):
		return self._PrvtData

	@PrvtData.setter
	def PrvtData(self, value):
		self._PrvtData = value if type(value) != base_types.auto else self.make_default("PrvtData")

	@PrvtData.deleter
	def PrvtData(self):
		del self._PrvtData
		self._PrvtData = None

	@property
	def Schme(self):
		return self._Schme

	@Schme.setter
	def Schme(self, value):
		self._Schme = value if type(value) != base_types.auto else self.make_default("Schme")

	@Schme.deleter
	def Schme(self):
		del self._Schme
		self._Schme = None

	@property
	def Sgmt(self):
		return self._Sgmt

	@Sgmt.setter
	def Sgmt(self, value):
		self._Sgmt = value if type(value) != base_types.auto else self.make_default("Sgmt")

	@Sgmt.deleter
	def Sgmt(self):
		del self._Sgmt
		self._Sgmt = None

	@property
	def Trck3(self):
		return self._Trck3

	@Trck3.setter
	def Trck3(self, value):
		self._Trck3 = value if type(value) != base_types.auto else self.make_default("Trck3")

	@Trck3.deleter
	def Trck3(self):
		del self._Trck3
		self._Trck3 = None

	@property
	def XpryDt(self):
		return self._XpryDt

	@XpryDt.setter
	def XpryDt(self, value):
		self._XpryDt = value if type(value) != base_types.auto else self.make_default("XpryDt")

	@XpryDt.deleter
	def XpryDt(self):
		del self._XpryDt
		self._XpryDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctFndgSrc', type=Max10Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Brnd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardSeqNb', type=Min2Max3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ISO3NumericCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctry', type=ISO3NumericCountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FctvDt', type=ISOYearMonth, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IsseDt', type=ISOYearMonth, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtlData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PAN', type=Max19NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PANAcctRg', type=Max19NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PANFourLastDgts', type=Max4NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PANRefIdr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctSubTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtAcctRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdPAN', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtflIdr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvtData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Schme', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sgmt', type=Max10Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Trck3', type=Max104Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpryDt', type=ISOYearMonth, min=0, max=1, mutex_group=None, array=False),
	))

