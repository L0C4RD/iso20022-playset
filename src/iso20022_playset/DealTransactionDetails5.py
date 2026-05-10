import base_types
import ClosingDate4Choice
import PlaceOfTradeIdentification1
import OptionType6Choice
import RepoTerminationOption1Code
import PercentageRate
import InterestComputationMethodFormat4Choice
import CollateralAmount18
import RateOrName4Choice
import FrequencyRateFixing1Choice
import DeliveryReceiptType2Code
import Exact3NumericText
import YesNoIndicator

class DealTransactionDetails5(base_types._BaseFieldType):

	__slots__ = ["_DealDtlsAmt", "_PlcOfTrad", "_MinNtcePrd", "_OvrnghtFrqcyRateFxg", "_DayCntBsis", "_OptnTp", "_ClsgDt", "_TermntnOptn", "_Sprd", "_Pmt", "_PricgRateAndIndx", "_CncntrtnLmt"]
	@property
	def DealDtlsAmt(self):
		return self._DealDtlsAmt

	@DealDtlsAmt.setter
	def DealDtlsAmt(self, value):
		self._DealDtlsAmt = value if type(value) != auto else self.make_default("DealDtlsAmt")

	@DealDtlsAmt.deleter
	def DealDtlsAmt(self):
		del self._DealDtlsAmt
		self._DealDtlsAmt = None

	@property
	def PlcOfTrad(self):
		return self._PlcOfTrad

	@PlcOfTrad.setter
	def PlcOfTrad(self, value):
		self._PlcOfTrad = value if type(value) != auto else self.make_default("PlcOfTrad")

	@PlcOfTrad.deleter
	def PlcOfTrad(self):
		del self._PlcOfTrad
		self._PlcOfTrad = None

	@property
	def MinNtcePrd(self):
		return self._MinNtcePrd

	@MinNtcePrd.setter
	def MinNtcePrd(self, value):
		self._MinNtcePrd = value if type(value) != auto else self.make_default("MinNtcePrd")

	@MinNtcePrd.deleter
	def MinNtcePrd(self):
		del self._MinNtcePrd
		self._MinNtcePrd = None

	@property
	def OvrnghtFrqcyRateFxg(self):
		return self._OvrnghtFrqcyRateFxg

	@OvrnghtFrqcyRateFxg.setter
	def OvrnghtFrqcyRateFxg(self, value):
		self._OvrnghtFrqcyRateFxg = value if type(value) != auto else self.make_default("OvrnghtFrqcyRateFxg")

	@OvrnghtFrqcyRateFxg.deleter
	def OvrnghtFrqcyRateFxg(self):
		del self._OvrnghtFrqcyRateFxg
		self._OvrnghtFrqcyRateFxg = None

	@property
	def DayCntBsis(self):
		return self._DayCntBsis

	@DayCntBsis.setter
	def DayCntBsis(self, value):
		self._DayCntBsis = value if type(value) != auto else self.make_default("DayCntBsis")

	@DayCntBsis.deleter
	def DayCntBsis(self):
		del self._DayCntBsis
		self._DayCntBsis = None

	@property
	def OptnTp(self):
		return self._OptnTp

	@OptnTp.setter
	def OptnTp(self, value):
		self._OptnTp = value if type(value) != auto else self.make_default("OptnTp")

	@OptnTp.deleter
	def OptnTp(self):
		del self._OptnTp
		self._OptnTp = None

	@property
	def ClsgDt(self):
		return self._ClsgDt

	@ClsgDt.setter
	def ClsgDt(self, value):
		self._ClsgDt = value if type(value) != auto else self.make_default("ClsgDt")

	@ClsgDt.deleter
	def ClsgDt(self):
		del self._ClsgDt
		self._ClsgDt = None

	@property
	def TermntnOptn(self):
		return self._TermntnOptn

	@TermntnOptn.setter
	def TermntnOptn(self, value):
		self._TermntnOptn = value if type(value) != auto else self.make_default("TermntnOptn")

	@TermntnOptn.deleter
	def TermntnOptn(self):
		del self._TermntnOptn
		self._TermntnOptn = None

	@property
	def Sprd(self):
		return self._Sprd

	@Sprd.setter
	def Sprd(self, value):
		self._Sprd = value if type(value) != auto else self.make_default("Sprd")

	@Sprd.deleter
	def Sprd(self):
		del self._Sprd
		self._Sprd = None

	@property
	def Pmt(self):
		return self._Pmt

	@Pmt.setter
	def Pmt(self, value):
		self._Pmt = value if type(value) != auto else self.make_default("Pmt")

	@Pmt.deleter
	def Pmt(self):
		del self._Pmt
		self._Pmt = None

	@property
	def PricgRateAndIndx(self):
		return self._PricgRateAndIndx

	@PricgRateAndIndx.setter
	def PricgRateAndIndx(self, value):
		self._PricgRateAndIndx = value if type(value) != auto else self.make_default("PricgRateAndIndx")

	@PricgRateAndIndx.deleter
	def PricgRateAndIndx(self):
		del self._PricgRateAndIndx
		self._PricgRateAndIndx = None

	@property
	def CncntrtnLmt(self):
		return self._CncntrtnLmt

	@CncntrtnLmt.setter
	def CncntrtnLmt(self, value):
		self._CncntrtnLmt = value if type(value) != auto else self.make_default("CncntrtnLmt")

	@CncntrtnLmt.deleter
	def CncntrtnLmt(self):
		del self._CncntrtnLmt
		self._CncntrtnLmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DealDtlsAmt', type=CollateralAmount18, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfTrad', type=PlaceOfTradeIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinNtcePrd', type=Exact3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OvrnghtFrqcyRateFxg', type=FrequencyRateFixing1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DayCntBsis', type=InterestComputationMethodFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnTp', type=OptionType6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClsgDt', type=ClosingDate4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TermntnOptn', type=RepoTerminationOption1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sprd', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pmt', type=DeliveryReceiptType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricgRateAndIndx', type=RateOrName4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CncntrtnLmt', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
	))

