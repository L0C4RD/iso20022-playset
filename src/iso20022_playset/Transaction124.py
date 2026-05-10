from . import base_types
from .TransactionStatus6 import TransactionStatus6
from .CollateralParties11 import CollateralParties11
from .RepoTerminationOption1Code import RepoTerminationOption1Code
from .ClosingDate4Choice import ClosingDate4Choice
from .RateOrName4Choice import RateOrName4Choice
from .InterestComputationMethodFormat4Choice import InterestComputationMethodFormat4Choice
from .ExposureType23Choice import ExposureType23Choice
from .BasketIdentificationAndEligibilitySetProfile1 import BasketIdentificationAndEligibilitySetProfile1
from .CashBalance15 import CashBalance15
from .SecuritiesBalance3 import SecuritiesBalance3
from .CollateralAmount17 import CollateralAmount17
from .OptionType6Choice import OptionType6Choice
from .PercentageRate import PercentageRate
from .Max35Text import Max35Text
from .Max52Text import Max52Text
from .YesNoIndicator import YesNoIndicator

class Transaction124(base_types._BaseFieldType):

	__slots__ = ["_CmonTxId", "_ClntTrptyCollTxId", "_MrgnRate", "_CtrPtyCollTxRef", "_DayCntBsis", "_OptnTp", "_TrptyAgtSvcPrvdrCollTxId", "_ExctnReqdDt", "_CshBal", "_PricgRate", "_ValtnAmts", "_CollPties", "_XpsrTp", "_TxSts", "_ClsgDt", "_BsktIdAndElgbltySetPrfl", "_AutomtcAllcn", "_SctiesBal", "_SprdRate", "_TermntnOptn"]
	@property
	def CmonTxId(self):
		return self._CmonTxId

	@CmonTxId.setter
	def CmonTxId(self, value):
		self._CmonTxId = value if type(value) != base_types.auto else self.make_default("CmonTxId")

	@CmonTxId.deleter
	def CmonTxId(self):
		del self._CmonTxId
		self._CmonTxId = None

	@property
	def ClntTrptyCollTxId(self):
		return self._ClntTrptyCollTxId

	@ClntTrptyCollTxId.setter
	def ClntTrptyCollTxId(self, value):
		self._ClntTrptyCollTxId = value if type(value) != base_types.auto else self.make_default("ClntTrptyCollTxId")

	@ClntTrptyCollTxId.deleter
	def ClntTrptyCollTxId(self):
		del self._ClntTrptyCollTxId
		self._ClntTrptyCollTxId = None

	@property
	def MrgnRate(self):
		return self._MrgnRate

	@MrgnRate.setter
	def MrgnRate(self, value):
		self._MrgnRate = value if type(value) != base_types.auto else self.make_default("MrgnRate")

	@MrgnRate.deleter
	def MrgnRate(self):
		del self._MrgnRate
		self._MrgnRate = None

	@property
	def CtrPtyCollTxRef(self):
		return self._CtrPtyCollTxRef

	@CtrPtyCollTxRef.setter
	def CtrPtyCollTxRef(self, value):
		self._CtrPtyCollTxRef = value if type(value) != base_types.auto else self.make_default("CtrPtyCollTxRef")

	@CtrPtyCollTxRef.deleter
	def CtrPtyCollTxRef(self):
		del self._CtrPtyCollTxRef
		self._CtrPtyCollTxRef = None

	@property
	def DayCntBsis(self):
		return self._DayCntBsis

	@DayCntBsis.setter
	def DayCntBsis(self, value):
		self._DayCntBsis = value if type(value) != base_types.auto else self.make_default("DayCntBsis")

	@DayCntBsis.deleter
	def DayCntBsis(self):
		del self._DayCntBsis
		self._DayCntBsis = None

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
	def TrptyAgtSvcPrvdrCollTxId(self):
		return self._TrptyAgtSvcPrvdrCollTxId

	@TrptyAgtSvcPrvdrCollTxId.setter
	def TrptyAgtSvcPrvdrCollTxId(self, value):
		self._TrptyAgtSvcPrvdrCollTxId = value if type(value) != base_types.auto else self.make_default("TrptyAgtSvcPrvdrCollTxId")

	@TrptyAgtSvcPrvdrCollTxId.deleter
	def TrptyAgtSvcPrvdrCollTxId(self):
		del self._TrptyAgtSvcPrvdrCollTxId
		self._TrptyAgtSvcPrvdrCollTxId = None

	@property
	def ExctnReqdDt(self):
		return self._ExctnReqdDt

	@ExctnReqdDt.setter
	def ExctnReqdDt(self, value):
		self._ExctnReqdDt = value if type(value) != base_types.auto else self.make_default("ExctnReqdDt")

	@ExctnReqdDt.deleter
	def ExctnReqdDt(self):
		del self._ExctnReqdDt
		self._ExctnReqdDt = None

	@property
	def CshBal(self):
		return self._CshBal

	@CshBal.setter
	def CshBal(self, value):
		self._CshBal = value if type(value) != base_types.auto else self.make_default("CshBal")

	@CshBal.deleter
	def CshBal(self):
		del self._CshBal
		self._CshBal = None

	@property
	def PricgRate(self):
		return self._PricgRate

	@PricgRate.setter
	def PricgRate(self, value):
		self._PricgRate = value if type(value) != base_types.auto else self.make_default("PricgRate")

	@PricgRate.deleter
	def PricgRate(self):
		del self._PricgRate
		self._PricgRate = None

	@property
	def ValtnAmts(self):
		return self._ValtnAmts

	@ValtnAmts.setter
	def ValtnAmts(self, value):
		self._ValtnAmts = value if type(value) != base_types.auto else self.make_default("ValtnAmts")

	@ValtnAmts.deleter
	def ValtnAmts(self):
		del self._ValtnAmts
		self._ValtnAmts = None

	@property
	def CollPties(self):
		return self._CollPties

	@CollPties.setter
	def CollPties(self, value):
		self._CollPties = value if type(value) != base_types.auto else self.make_default("CollPties")

	@CollPties.deleter
	def CollPties(self):
		del self._CollPties
		self._CollPties = None

	@property
	def XpsrTp(self):
		return self._XpsrTp

	@XpsrTp.setter
	def XpsrTp(self, value):
		self._XpsrTp = value if type(value) != base_types.auto else self.make_default("XpsrTp")

	@XpsrTp.deleter
	def XpsrTp(self):
		del self._XpsrTp
		self._XpsrTp = None

	@property
	def TxSts(self):
		return self._TxSts

	@TxSts.setter
	def TxSts(self, value):
		self._TxSts = value if type(value) != base_types.auto else self.make_default("TxSts")

	@TxSts.deleter
	def TxSts(self):
		del self._TxSts
		self._TxSts = None

	@property
	def ClsgDt(self):
		return self._ClsgDt

	@ClsgDt.setter
	def ClsgDt(self, value):
		self._ClsgDt = value if type(value) != base_types.auto else self.make_default("ClsgDt")

	@ClsgDt.deleter
	def ClsgDt(self):
		del self._ClsgDt
		self._ClsgDt = None

	@property
	def BsktIdAndElgbltySetPrfl(self):
		return self._BsktIdAndElgbltySetPrfl

	@BsktIdAndElgbltySetPrfl.setter
	def BsktIdAndElgbltySetPrfl(self, value):
		self._BsktIdAndElgbltySetPrfl = value if type(value) != base_types.auto else self.make_default("BsktIdAndElgbltySetPrfl")

	@BsktIdAndElgbltySetPrfl.deleter
	def BsktIdAndElgbltySetPrfl(self):
		del self._BsktIdAndElgbltySetPrfl
		self._BsktIdAndElgbltySetPrfl = None

	@property
	def AutomtcAllcn(self):
		return self._AutomtcAllcn

	@AutomtcAllcn.setter
	def AutomtcAllcn(self, value):
		self._AutomtcAllcn = value if type(value) != base_types.auto else self.make_default("AutomtcAllcn")

	@AutomtcAllcn.deleter
	def AutomtcAllcn(self):
		del self._AutomtcAllcn
		self._AutomtcAllcn = None

	@property
	def SctiesBal(self):
		return self._SctiesBal

	@SctiesBal.setter
	def SctiesBal(self, value):
		self._SctiesBal = value if type(value) != base_types.auto else self.make_default("SctiesBal")

	@SctiesBal.deleter
	def SctiesBal(self):
		del self._SctiesBal
		self._SctiesBal = None

	@property
	def SprdRate(self):
		return self._SprdRate

	@SprdRate.setter
	def SprdRate(self, value):
		self._SprdRate = value if type(value) != base_types.auto else self.make_default("SprdRate")

	@SprdRate.deleter
	def SprdRate(self):
		del self._SprdRate
		self._SprdRate = None

	@property
	def TermntnOptn(self):
		return self._TermntnOptn

	@TermntnOptn.setter
	def TermntnOptn(self, value):
		self._TermntnOptn = value if type(value) != base_types.auto else self.make_default("TermntnOptn")

	@TermntnOptn.deleter
	def TermntnOptn(self):
		del self._TermntnOptn
		self._TermntnOptn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CmonTxId', type=Max52Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntTrptyCollTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtyCollTxRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DayCntBsis', type=InterestComputationMethodFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnTp', type=OptionType6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrptyAgtSvcPrvdrCollTxId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExctnReqdDt', type=ClosingDate4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshBal', type=CashBalance15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PricgRate', type=RateOrName4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValtnAmts', type=CollateralAmount17, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollPties', type=CollateralParties11, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpsrTp', type=ExposureType23Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxSts', type=TransactionStatus6, min=0, max=2, mutex_group=None, array=True),
		base_types.FieldEntry(name='ClsgDt', type=ClosingDate4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BsktIdAndElgbltySetPrfl', type=BasketIdentificationAndEligibilitySetProfile1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AutomtcAllcn', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesBal', type=SecuritiesBalance3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SprdRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TermntnOptn', type=RepoTerminationOption1Code, min=0, max=1, mutex_group=None, array=False),
	))

