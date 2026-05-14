# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AdditionalData1 import AdditionalData1
from ._ISO3NumericCountryCode import ISO3NumericCountryCode
from ._ISOYearMonth import ISOYearMonth
from ._Max19NumericText import Max19NumericText
from ._Max35Text import Max35Text
from ._Min2Max3NumericText import Min2Max3NumericText
from ._Track2Data1Choice import Track2Data1Choice
from ._TrueFalseIndicator import TrueFalseIndicator

class CardData13(base_types._BaseFieldType):

	__slots__ = ["_AddtlCardData", "_CardSeqNb", "_CtryCd", "_FctvDt", "_PAN", "_PANAcctRg", "_PdctSubTp", "_PdctTp", "_PmtAcctRef", "_PrtctdPAN", "_PrtflIdr", "_Trck2", "_XpryDt"]
	@property
	def AddtlCardData(self):
		return self._AddtlCardData

	@AddtlCardData.setter
	def AddtlCardData(self, value):
		self._AddtlCardData = value if type(value) != base_types.auto else self.make_default("AddtlCardData")

	@AddtlCardData.deleter
	def AddtlCardData(self):
		del self._AddtlCardData
		self._AddtlCardData = None

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
	def CtryCd(self):
		return self._CtryCd

	@CtryCd.setter
	def CtryCd(self, value):
		self._CtryCd = value if type(value) != base_types.auto else self.make_default("CtryCd")

	@CtryCd.deleter
	def CtryCd(self):
		del self._CtryCd
		self._CtryCd = None

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
	def Trck2(self):
		return self._Trck2

	@Trck2.setter
	def Trck2(self, value):
		self._Trck2 = value if type(value) != base_types.auto else self.make_default("Trck2")

	@Trck2.deleter
	def Trck2(self):
		del self._Trck2
		self._Trck2 = None

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
		base_types.FieldEntry(name='AddtlCardData', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CardSeqNb', type=Min2Max3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryCd', type=ISO3NumericCountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FctvDt', type=ISOYearMonth, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PAN', type=Max19NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PANAcctRg', type=Max19NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctSubTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtAcctRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdPAN', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtflIdr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Trck2', type=Track2Data1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpryDt', type=ISOYearMonth, min=0, max=1, mutex_group=None, array=False),
	))