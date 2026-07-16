# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalData1
from . import ISO3NumericCountryCode
from . import ISOYearMonth
from . import Max19NumericText
from . import Max35Text
from . import Min2Max3NumericText
from . import Track2Data1Choice
from . import TrueFalseIndicator

class CardData13(base_types._BaseFieldType):

	__slots__ = ["_AddtlCardData", "_CardSeqNb", "_CtryCd", "_FctvDt", "_PAN", "_PANAcctRg", "_PdctSubTp", "_PdctTp", "_PmtAcctRef", "_PrtctdPAN", "_PrtflIdr", "_Trck2", "_XpryDt"]
	@property
	def AddtlCardData(self):
		return self._AddtlCardData

	@AddtlCardData.setter
	def AddtlCardData(self, value):
		self._AddtlCardData = value if value is not None else base_types.UninitialisedField(self, 'AddtlCardData', AdditionalData1, True)

	@AddtlCardData.deleter
	def AddtlCardData(self):
		del self._AddtlCardData
		self._AddtlCardData = base_types.UninitialisedField(self, 'AddtlCardData', AdditionalData1, True)

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
	def CtryCd(self):
		return self._CtryCd

	@CtryCd.setter
	def CtryCd(self, value):
		self._CtryCd = value if value is not None else base_types.UninitialisedField(self, 'CtryCd', ISO3NumericCountryCode, False)

	@CtryCd.deleter
	def CtryCd(self):
		del self._CtryCd
		self._CtryCd = base_types.UninitialisedField(self, 'CtryCd', ISO3NumericCountryCode, False)

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