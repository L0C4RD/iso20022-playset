# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AdditionalData1 import AdditionalData1
from ._ISO3NumericCountryCode import ISO3NumericCountryCode
from ._ISOYearMonth import ISOYearMonth
from ._Max19NumericText import Max19NumericText
from ._Max35Text import Max35Text
from ._Min2Max3NumericText import Min2Max3NumericText
from ._TrueFalseIndicator import TrueFalseIndicator

class CardData15(base_types._BaseFieldType):

	__slots__ = ["_AddtlData", "_CardSeqNb", "_Ctry", "_FctvDt", "_PAN", "_PANAcctRg", "_PANRefIdr", "_PdctSubTp", "_PdctTp", "_PmtAcctRef", "_PrtctdPAN", "_PrtflIdr", "_XpryDt"]
	@property
	def AddtlData(self):
		return self._AddtlData

	@AddtlData.setter
	def AddtlData(self, value):
		self._AddtlData = value if type(value) != base_types.auto else self.make_default("AddtlData")

	@AddtlData.deleter
	def AddtlData(self):
		del self._AddtlData
		self._AddtlData = None

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
		base_types.FieldEntry(name='AddtlData', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CardSeqNb', type=Min2Max3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctry', type=ISO3NumericCountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FctvDt', type=ISOYearMonth, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PAN', type=Max19NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PANAcctRg', type=Max19NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PANRefIdr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctSubTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtAcctRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdPAN', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtflIdr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpryDt', type=ISOYearMonth, min=0, max=1, mutex_group=None, array=False),
	))