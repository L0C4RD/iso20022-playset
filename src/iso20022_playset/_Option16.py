# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import AgreedRate3
from . import AmountsAndValueDate4
from . import DataType1Code
from . import DerivativeExerciseStatus1Code
from . import ISODateTime
from . import Max140Text
from . import Max35Text
from . import Max4AlphaNumericText
from . import OptionPayoutType1Code
from . import OptionStyle2Code
from . import OptionType1Code
from . import PercentageRate
from . import PremiumAmount3
from . import SettlementDate8Code
from . import SettlementType1Code

class Option16(base_types._BaseFieldType):

	__slots__ = ["_AddtlOptnInf", "_Data", "_DerivOptnId", "_ExrcSts", "_ExrcStyle", "_OptnAmts", "_OptnPyoutTp", "_OptnTp", "_Prm", "_RskAmt", "_StrkPric", "_SttlmAmtTp", "_SttlmTp", "_ValtnRate", "_VoltlyMrgn", "_XpryDtAndTm", "_XpryLctn"]
	@property
	def AddtlOptnInf(self):
		return self._AddtlOptnInf

	@AddtlOptnInf.setter
	def AddtlOptnInf(self, value):
		self._AddtlOptnInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlOptnInf', Max140Text, False)

	@AddtlOptnInf.deleter
	def AddtlOptnInf(self):
		del self._AddtlOptnInf
		self._AddtlOptnInf = base_types.UninitialisedField(self, 'AddtlOptnInf', Max140Text, False)

	@property
	def Data(self):
		return self._Data

	@Data.setter
	def Data(self, value):
		self._Data = value if value is not None else base_types.UninitialisedField(self, 'Data', DataType1Code, False)

	@Data.deleter
	def Data(self):
		del self._Data
		self._Data = base_types.UninitialisedField(self, 'Data', DataType1Code, False)

	@property
	def DerivOptnId(self):
		return self._DerivOptnId

	@DerivOptnId.setter
	def DerivOptnId(self, value):
		self._DerivOptnId = value if value is not None else base_types.UninitialisedField(self, 'DerivOptnId', Max35Text, False)

	@DerivOptnId.deleter
	def DerivOptnId(self):
		del self._DerivOptnId
		self._DerivOptnId = base_types.UninitialisedField(self, 'DerivOptnId', Max35Text, False)

	@property
	def ExrcSts(self):
		return self._ExrcSts

	@ExrcSts.setter
	def ExrcSts(self, value):
		self._ExrcSts = value if value is not None else base_types.UninitialisedField(self, 'ExrcSts', DerivativeExerciseStatus1Code, False)

	@ExrcSts.deleter
	def ExrcSts(self):
		del self._ExrcSts
		self._ExrcSts = base_types.UninitialisedField(self, 'ExrcSts', DerivativeExerciseStatus1Code, False)

	@property
	def ExrcStyle(self):
		return self._ExrcStyle

	@ExrcStyle.setter
	def ExrcStyle(self, value):
		self._ExrcStyle = value if value is not None else base_types.UninitialisedField(self, 'ExrcStyle', OptionStyle2Code, False)

	@ExrcStyle.deleter
	def ExrcStyle(self):
		del self._ExrcStyle
		self._ExrcStyle = base_types.UninitialisedField(self, 'ExrcStyle', OptionStyle2Code, False)

	@property
	def OptnAmts(self):
		return self._OptnAmts

	@OptnAmts.setter
	def OptnAmts(self, value):
		self._OptnAmts = value if value is not None else base_types.UninitialisedField(self, 'OptnAmts', AmountsAndValueDate4, False)

	@OptnAmts.deleter
	def OptnAmts(self):
		del self._OptnAmts
		self._OptnAmts = base_types.UninitialisedField(self, 'OptnAmts', AmountsAndValueDate4, False)

	@property
	def OptnPyoutTp(self):
		return self._OptnPyoutTp

	@OptnPyoutTp.setter
	def OptnPyoutTp(self, value):
		self._OptnPyoutTp = value if value is not None else base_types.UninitialisedField(self, 'OptnPyoutTp', OptionPayoutType1Code, False)

	@OptnPyoutTp.deleter
	def OptnPyoutTp(self):
		del self._OptnPyoutTp
		self._OptnPyoutTp = base_types.UninitialisedField(self, 'OptnPyoutTp', OptionPayoutType1Code, False)

	@property
	def OptnTp(self):
		return self._OptnTp

	@OptnTp.setter
	def OptnTp(self, value):
		self._OptnTp = value if value is not None else base_types.UninitialisedField(self, 'OptnTp', OptionType1Code, False)

	@OptnTp.deleter
	def OptnTp(self):
		del self._OptnTp
		self._OptnTp = base_types.UninitialisedField(self, 'OptnTp', OptionType1Code, False)

	@property
	def Prm(self):
		return self._Prm

	@Prm.setter
	def Prm(self, value):
		self._Prm = value if value is not None else base_types.UninitialisedField(self, 'Prm', PremiumAmount3, False)

	@Prm.deleter
	def Prm(self):
		del self._Prm
		self._Prm = base_types.UninitialisedField(self, 'Prm', PremiumAmount3, False)

	@property
	def RskAmt(self):
		return self._RskAmt

	@RskAmt.setter
	def RskAmt(self, value):
		self._RskAmt = value if value is not None else base_types.UninitialisedField(self, 'RskAmt', ActiveCurrencyAndAmount, False)

	@RskAmt.deleter
	def RskAmt(self):
		del self._RskAmt
		self._RskAmt = base_types.UninitialisedField(self, 'RskAmt', ActiveCurrencyAndAmount, False)

	@property
	def StrkPric(self):
		return self._StrkPric

	@StrkPric.setter
	def StrkPric(self, value):
		self._StrkPric = value if value is not None else base_types.UninitialisedField(self, 'StrkPric', AgreedRate3, False)

	@StrkPric.deleter
	def StrkPric(self):
		del self._StrkPric
		self._StrkPric = base_types.UninitialisedField(self, 'StrkPric', AgreedRate3, False)

	@property
	def SttlmAmtTp(self):
		return self._SttlmAmtTp

	@SttlmAmtTp.setter
	def SttlmAmtTp(self, value):
		self._SttlmAmtTp = value if value is not None else base_types.UninitialisedField(self, 'SttlmAmtTp', SettlementType1Code, False)

	@SttlmAmtTp.deleter
	def SttlmAmtTp(self):
		del self._SttlmAmtTp
		self._SttlmAmtTp = base_types.UninitialisedField(self, 'SttlmAmtTp', SettlementType1Code, False)

	@property
	def SttlmTp(self):
		return self._SttlmTp

	@SttlmTp.setter
	def SttlmTp(self, value):
		self._SttlmTp = value if value is not None else base_types.UninitialisedField(self, 'SttlmTp', SettlementDate8Code, False)

	@SttlmTp.deleter
	def SttlmTp(self):
		del self._SttlmTp
		self._SttlmTp = base_types.UninitialisedField(self, 'SttlmTp', SettlementDate8Code, False)

	@property
	def ValtnRate(self):
		return self._ValtnRate

	@ValtnRate.setter
	def ValtnRate(self, value):
		self._ValtnRate = value if value is not None else base_types.UninitialisedField(self, 'ValtnRate', AgreedRate3, False)

	@ValtnRate.deleter
	def ValtnRate(self):
		del self._ValtnRate
		self._ValtnRate = base_types.UninitialisedField(self, 'ValtnRate', AgreedRate3, False)

	@property
	def VoltlyMrgn(self):
		return self._VoltlyMrgn

	@VoltlyMrgn.setter
	def VoltlyMrgn(self, value):
		self._VoltlyMrgn = value if value is not None else base_types.UninitialisedField(self, 'VoltlyMrgn', PercentageRate, False)

	@VoltlyMrgn.deleter
	def VoltlyMrgn(self):
		del self._VoltlyMrgn
		self._VoltlyMrgn = base_types.UninitialisedField(self, 'VoltlyMrgn', PercentageRate, False)

	@property
	def XpryDtAndTm(self):
		return self._XpryDtAndTm

	@XpryDtAndTm.setter
	def XpryDtAndTm(self, value):
		self._XpryDtAndTm = value if value is not None else base_types.UninitialisedField(self, 'XpryDtAndTm', ISODateTime, False)

	@XpryDtAndTm.deleter
	def XpryDtAndTm(self):
		del self._XpryDtAndTm
		self._XpryDtAndTm = base_types.UninitialisedField(self, 'XpryDtAndTm', ISODateTime, False)

	@property
	def XpryLctn(self):
		return self._XpryLctn

	@XpryLctn.setter
	def XpryLctn(self, value):
		self._XpryLctn = value if value is not None else base_types.UninitialisedField(self, 'XpryLctn', Max4AlphaNumericText, False)

	@XpryLctn.deleter
	def XpryLctn(self):
		del self._XpryLctn
		self._XpryLctn = base_types.UninitialisedField(self, 'XpryLctn', Max4AlphaNumericText, False)

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