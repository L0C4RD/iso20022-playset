# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._AgreedRate3 import AgreedRate3
from ._AmountsAndValueDate4 import AmountsAndValueDate4
from ._DataType1Code import DataType1Code
from ._DerivativeExerciseStatus1Code import DerivativeExerciseStatus1Code
from ._ISODateTime import ISODateTime
from ._Max140Text import Max140Text
from ._Max35Text import Max35Text
from ._Max4AlphaNumericText import Max4AlphaNumericText
from ._OptionPayoutType1Code import OptionPayoutType1Code
from ._OptionStyle2Code import OptionStyle2Code
from ._OptionType1Code import OptionType1Code
from ._PercentageRate import PercentageRate
from ._PremiumAmount3 import PremiumAmount3
from ._SettlementDate8Code import SettlementDate8Code
from ._SettlementType1Code import SettlementType1Code

class Option16(base_types._BaseFieldType):

	__slots__ = ["_AddtlOptnInf", "_Data", "_DerivOptnId", "_ExrcSts", "_ExrcStyle", "_OptnAmts", "_OptnPyoutTp", "_OptnTp", "_Prm", "_RskAmt", "_StrkPric", "_SttlmAmtTp", "_SttlmTp", "_ValtnRate", "_VoltlyMrgn", "_XpryDtAndTm", "_XpryLctn"]
	@property
	def AddtlOptnInf(self):
		return self._AddtlOptnInf

	@AddtlOptnInf.setter
	def AddtlOptnInf(self, value):
		self._AddtlOptnInf = value if type(value) != base_types.auto else self.make_default("AddtlOptnInf")

	@AddtlOptnInf.deleter
	def AddtlOptnInf(self):
		del self._AddtlOptnInf
		self._AddtlOptnInf = None

	@property
	def Data(self):
		return self._Data

	@Data.setter
	def Data(self, value):
		self._Data = value if type(value) != base_types.auto else self.make_default("Data")

	@Data.deleter
	def Data(self):
		del self._Data
		self._Data = None

	@property
	def DerivOptnId(self):
		return self._DerivOptnId

	@DerivOptnId.setter
	def DerivOptnId(self, value):
		self._DerivOptnId = value if type(value) != base_types.auto else self.make_default("DerivOptnId")

	@DerivOptnId.deleter
	def DerivOptnId(self):
		del self._DerivOptnId
		self._DerivOptnId = None

	@property
	def ExrcSts(self):
		return self._ExrcSts

	@ExrcSts.setter
	def ExrcSts(self, value):
		self._ExrcSts = value if type(value) != base_types.auto else self.make_default("ExrcSts")

	@ExrcSts.deleter
	def ExrcSts(self):
		del self._ExrcSts
		self._ExrcSts = None

	@property
	def ExrcStyle(self):
		return self._ExrcStyle

	@ExrcStyle.setter
	def ExrcStyle(self, value):
		self._ExrcStyle = value if type(value) != base_types.auto else self.make_default("ExrcStyle")

	@ExrcStyle.deleter
	def ExrcStyle(self):
		del self._ExrcStyle
		self._ExrcStyle = None

	@property
	def OptnAmts(self):
		return self._OptnAmts

	@OptnAmts.setter
	def OptnAmts(self, value):
		self._OptnAmts = value if type(value) != base_types.auto else self.make_default("OptnAmts")

	@OptnAmts.deleter
	def OptnAmts(self):
		del self._OptnAmts
		self._OptnAmts = None

	@property
	def OptnPyoutTp(self):
		return self._OptnPyoutTp

	@OptnPyoutTp.setter
	def OptnPyoutTp(self, value):
		self._OptnPyoutTp = value if type(value) != base_types.auto else self.make_default("OptnPyoutTp")

	@OptnPyoutTp.deleter
	def OptnPyoutTp(self):
		del self._OptnPyoutTp
		self._OptnPyoutTp = None

	@property
	def OptnTp(self):
		return self._OptnTp

	@OptnTp.setter
	def OptnTp(self, value):
		self._OptnTp = value if type(value) != base_types.auto else self.make_default("OptnTp")

	@OptnTp.deleter
	def OptnTp(self):
		del self._OptnTp
		self._OptnTp = None

	@property
	def Prm(self):
		return self._Prm

	@Prm.setter
	def Prm(self, value):
		self._Prm = value if type(value) != base_types.auto else self.make_default("Prm")

	@Prm.deleter
	def Prm(self):
		del self._Prm
		self._Prm = None

	@property
	def RskAmt(self):
		return self._RskAmt

	@RskAmt.setter
	def RskAmt(self, value):
		self._RskAmt = value if type(value) != base_types.auto else self.make_default("RskAmt")

	@RskAmt.deleter
	def RskAmt(self):
		del self._RskAmt
		self._RskAmt = None

	@property
	def StrkPric(self):
		return self._StrkPric

	@StrkPric.setter
	def StrkPric(self, value):
		self._StrkPric = value if type(value) != base_types.auto else self.make_default("StrkPric")

	@StrkPric.deleter
	def StrkPric(self):
		del self._StrkPric
		self._StrkPric = None

	@property
	def SttlmAmtTp(self):
		return self._SttlmAmtTp

	@SttlmAmtTp.setter
	def SttlmAmtTp(self, value):
		self._SttlmAmtTp = value if type(value) != base_types.auto else self.make_default("SttlmAmtTp")

	@SttlmAmtTp.deleter
	def SttlmAmtTp(self):
		del self._SttlmAmtTp
		self._SttlmAmtTp = None

	@property
	def SttlmTp(self):
		return self._SttlmTp

	@SttlmTp.setter
	def SttlmTp(self, value):
		self._SttlmTp = value if type(value) != base_types.auto else self.make_default("SttlmTp")

	@SttlmTp.deleter
	def SttlmTp(self):
		del self._SttlmTp
		self._SttlmTp = None

	@property
	def ValtnRate(self):
		return self._ValtnRate

	@ValtnRate.setter
	def ValtnRate(self, value):
		self._ValtnRate = value if type(value) != base_types.auto else self.make_default("ValtnRate")

	@ValtnRate.deleter
	def ValtnRate(self):
		del self._ValtnRate
		self._ValtnRate = None

	@property
	def VoltlyMrgn(self):
		return self._VoltlyMrgn

	@VoltlyMrgn.setter
	def VoltlyMrgn(self, value):
		self._VoltlyMrgn = value if type(value) != base_types.auto else self.make_default("VoltlyMrgn")

	@VoltlyMrgn.deleter
	def VoltlyMrgn(self):
		del self._VoltlyMrgn
		self._VoltlyMrgn = None

	@property
	def XpryDtAndTm(self):
		return self._XpryDtAndTm

	@XpryDtAndTm.setter
	def XpryDtAndTm(self, value):
		self._XpryDtAndTm = value if type(value) != base_types.auto else self.make_default("XpryDtAndTm")

	@XpryDtAndTm.deleter
	def XpryDtAndTm(self):
		del self._XpryDtAndTm
		self._XpryDtAndTm = None

	@property
	def XpryLctn(self):
		return self._XpryLctn

	@XpryLctn.setter
	def XpryLctn(self, value):
		self._XpryLctn = value if type(value) != base_types.auto else self.make_default("XpryLctn")

	@XpryLctn.deleter
	def XpryLctn(self):
		del self._XpryLctn
		self._XpryLctn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlOptnInf', type=Max140Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Data', type=DataType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DerivOptnId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExrcSts', type=DerivativeExerciseStatus1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExrcStyle', type=OptionStyle2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnAmts', type=AmountsAndValueDate4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnPyoutTp', type=OptionPayoutType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnTp', type=OptionType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prm', type=PremiumAmount3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RskAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StrkPric', type=AgreedRate3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmAmtTp', type=SettlementType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmTp', type=SettlementDate8Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValtnRate', type=AgreedRate3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VoltlyMrgn', type=PercentageRate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpryDtAndTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpryLctn', type=Max4AlphaNumericText, min=1, max=1, mutex_group=None, array=False),
	))