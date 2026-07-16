# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ClosingDate4Choice
from . import CollateralAmount18
from . import DeliveryReceiptType2Code
from . import Exact3NumericText
from . import FrequencyRateFixing1Choice
from . import InterestComputationMethodFormat4Choice
from . import OptionType6Choice
from . import PercentageRate
from . import PlaceOfTradeIdentification1
from . import RateOrName4Choice
from . import RepoTerminationOption1Code
from . import YesNoIndicator

class DealTransactionDetails5(base_types._BaseFieldType):

	__slots__ = ["_ClsgDt", "_CncntrtnLmt", "_DayCntBsis", "_DealDtlsAmt", "_MinNtcePrd", "_OptnTp", "_OvrnghtFrqcyRateFxg", "_PlcOfTrad", "_Pmt", "_PricgRateAndIndx", "_Sprd", "_TermntnOptn"]
	@property
	def ClsgDt(self):
		return self._ClsgDt

	@ClsgDt.setter
	def ClsgDt(self, value):
		self._ClsgDt = value if value is not None else base_types.UninitialisedField(self, 'ClsgDt', ClosingDate4Choice, False)

	@ClsgDt.deleter
	def ClsgDt(self):
		del self._ClsgDt
		self._ClsgDt = base_types.UninitialisedField(self, 'ClsgDt', ClosingDate4Choice, False)

	@property
	def CncntrtnLmt(self):
		return self._CncntrtnLmt

	@CncntrtnLmt.setter
	def CncntrtnLmt(self, value):
		self._CncntrtnLmt = value if value is not None else base_types.UninitialisedField(self, 'CncntrtnLmt', YesNoIndicator, False)

	@CncntrtnLmt.deleter
	def CncntrtnLmt(self):
		del self._CncntrtnLmt
		self._CncntrtnLmt = base_types.UninitialisedField(self, 'CncntrtnLmt', YesNoIndicator, False)

	@property
	def DayCntBsis(self):
		return self._DayCntBsis

	@DayCntBsis.setter
	def DayCntBsis(self, value):
		self._DayCntBsis = value if value is not None else base_types.UninitialisedField(self, 'DayCntBsis', InterestComputationMethodFormat4Choice, False)

	@DayCntBsis.deleter
	def DayCntBsis(self):
		del self._DayCntBsis
		self._DayCntBsis = base_types.UninitialisedField(self, 'DayCntBsis', InterestComputationMethodFormat4Choice, False)

	@property
	def DealDtlsAmt(self):
		return self._DealDtlsAmt

	@DealDtlsAmt.setter
	def DealDtlsAmt(self, value):
		self._DealDtlsAmt = value if value is not None else base_types.UninitialisedField(self, 'DealDtlsAmt', CollateralAmount18, False)

	@DealDtlsAmt.deleter
	def DealDtlsAmt(self):
		del self._DealDtlsAmt
		self._DealDtlsAmt = base_types.UninitialisedField(self, 'DealDtlsAmt', CollateralAmount18, False)

	@property
	def MinNtcePrd(self):
		return self._MinNtcePrd

	@MinNtcePrd.setter
	def MinNtcePrd(self, value):
		self._MinNtcePrd = value if value is not None else base_types.UninitialisedField(self, 'MinNtcePrd', Exact3NumericText, False)

	@MinNtcePrd.deleter
	def MinNtcePrd(self):
		del self._MinNtcePrd
		self._MinNtcePrd = base_types.UninitialisedField(self, 'MinNtcePrd', Exact3NumericText, False)

	@property
	def OptnTp(self):
		return self._OptnTp

	@OptnTp.setter
	def OptnTp(self, value):
		self._OptnTp = value if value is not None else base_types.UninitialisedField(self, 'OptnTp', OptionType6Choice, False)

	@OptnTp.deleter
	def OptnTp(self):
		del self._OptnTp
		self._OptnTp = base_types.UninitialisedField(self, 'OptnTp', OptionType6Choice, False)

	@property
	def OvrnghtFrqcyRateFxg(self):
		return self._OvrnghtFrqcyRateFxg

	@OvrnghtFrqcyRateFxg.setter
	def OvrnghtFrqcyRateFxg(self, value):
		self._OvrnghtFrqcyRateFxg = value if value is not None else base_types.UninitialisedField(self, 'OvrnghtFrqcyRateFxg', FrequencyRateFixing1Choice, False)

	@OvrnghtFrqcyRateFxg.deleter
	def OvrnghtFrqcyRateFxg(self):
		del self._OvrnghtFrqcyRateFxg
		self._OvrnghtFrqcyRateFxg = base_types.UninitialisedField(self, 'OvrnghtFrqcyRateFxg', FrequencyRateFixing1Choice, False)

	@property
	def PlcOfTrad(self):
		return self._PlcOfTrad

	@PlcOfTrad.setter
	def PlcOfTrad(self, value):
		self._PlcOfTrad = value if value is not None else base_types.UninitialisedField(self, 'PlcOfTrad', PlaceOfTradeIdentification1, False)

	@PlcOfTrad.deleter
	def PlcOfTrad(self):
		del self._PlcOfTrad
		self._PlcOfTrad = base_types.UninitialisedField(self, 'PlcOfTrad', PlaceOfTradeIdentification1, False)

	@property
	def Pmt(self):
		return self._Pmt

	@Pmt.setter
	def Pmt(self, value):
		self._Pmt = value if value is not None else base_types.UninitialisedField(self, 'Pmt', DeliveryReceiptType2Code, False)

	@Pmt.deleter
	def Pmt(self):
		del self._Pmt
		self._Pmt = base_types.UninitialisedField(self, 'Pmt', DeliveryReceiptType2Code, False)

	@property
	def PricgRateAndIndx(self):
		return self._PricgRateAndIndx

	@PricgRateAndIndx.setter
	def PricgRateAndIndx(self, value):
		self._PricgRateAndIndx = value if value is not None else base_types.UninitialisedField(self, 'PricgRateAndIndx', RateOrName4Choice, False)

	@PricgRateAndIndx.deleter
	def PricgRateAndIndx(self):
		del self._PricgRateAndIndx
		self._PricgRateAndIndx = base_types.UninitialisedField(self, 'PricgRateAndIndx', RateOrName4Choice, False)

	@property
	def Sprd(self):
		return self._Sprd

	@Sprd.setter
	def Sprd(self, value):
		self._Sprd = value if value is not None else base_types.UninitialisedField(self, 'Sprd', PercentageRate, False)

	@Sprd.deleter
	def Sprd(self):
		del self._Sprd
		self._Sprd = base_types.UninitialisedField(self, 'Sprd', PercentageRate, False)

	@property
	def TermntnOptn(self):
		return self._TermntnOptn

	@TermntnOptn.setter
	def TermntnOptn(self, value):
		self._TermntnOptn = value if value is not None else base_types.UninitialisedField(self, 'TermntnOptn', RepoTerminationOption1Code, False)

	@TermntnOptn.deleter
	def TermntnOptn(self):
		del self._TermntnOptn
		self._TermntnOptn = base_types.UninitialisedField(self, 'TermntnOptn', RepoTerminationOption1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClsgDt', type=ClosingDate4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CncntrtnLmt', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DayCntBsis', type=InterestComputationMethodFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DealDtlsAmt', type=CollateralAmount18, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinNtcePrd', type=Exact3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnTp', type=OptionType6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OvrnghtFrqcyRateFxg', type=FrequencyRateFixing1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfTrad', type=PlaceOfTradeIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pmt', type=DeliveryReceiptType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricgRateAndIndx', type=RateOrName4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sprd', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TermntnOptn', type=RepoTerminationOption1Code, min=0, max=1, mutex_group=None, array=False),
	))