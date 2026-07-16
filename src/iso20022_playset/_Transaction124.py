# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BasketIdentificationAndEligibilitySetProfile1
from . import CashBalance15
from . import ClosingDate4Choice
from . import CollateralAmount17
from . import CollateralParties11
from . import ExposureType23Choice
from . import InterestComputationMethodFormat4Choice
from . import Max35Text
from . import Max52Text
from . import OptionType6Choice
from . import PercentageRate
from . import RateOrName4Choice
from . import RepoTerminationOption1Code
from . import SecuritiesBalance3
from . import TransactionStatus6
from . import YesNoIndicator

class Transaction124(base_types._BaseFieldType):

	__slots__ = ["_AutomtcAllcn", "_BsktIdAndElgbltySetPrfl", "_ClntTrptyCollTxId", "_ClsgDt", "_CmonTxId", "_CollPties", "_CshBal", "_CtrPtyCollTxRef", "_DayCntBsis", "_ExctnReqdDt", "_MrgnRate", "_OptnTp", "_PricgRate", "_SctiesBal", "_SprdRate", "_TermntnOptn", "_TrptyAgtSvcPrvdrCollTxId", "_TxSts", "_ValtnAmts", "_XpsrTp"]
	@property
	def AutomtcAllcn(self):
		return self._AutomtcAllcn

	@AutomtcAllcn.setter
	def AutomtcAllcn(self, value):
		self._AutomtcAllcn = value if value is not None else base_types.UninitialisedField(self, 'AutomtcAllcn', YesNoIndicator, False)

	@AutomtcAllcn.deleter
	def AutomtcAllcn(self):
		del self._AutomtcAllcn
		self._AutomtcAllcn = base_types.UninitialisedField(self, 'AutomtcAllcn', YesNoIndicator, False)

	@property
	def BsktIdAndElgbltySetPrfl(self):
		return self._BsktIdAndElgbltySetPrfl

	@BsktIdAndElgbltySetPrfl.setter
	def BsktIdAndElgbltySetPrfl(self, value):
		self._BsktIdAndElgbltySetPrfl = value if value is not None else base_types.UninitialisedField(self, 'BsktIdAndElgbltySetPrfl', BasketIdentificationAndEligibilitySetProfile1, False)

	@BsktIdAndElgbltySetPrfl.deleter
	def BsktIdAndElgbltySetPrfl(self):
		del self._BsktIdAndElgbltySetPrfl
		self._BsktIdAndElgbltySetPrfl = base_types.UninitialisedField(self, 'BsktIdAndElgbltySetPrfl', BasketIdentificationAndEligibilitySetProfile1, False)

	@property
	def ClntTrptyCollTxId(self):
		return self._ClntTrptyCollTxId

	@ClntTrptyCollTxId.setter
	def ClntTrptyCollTxId(self, value):
		self._ClntTrptyCollTxId = value if value is not None else base_types.UninitialisedField(self, 'ClntTrptyCollTxId', Max35Text, False)

	@ClntTrptyCollTxId.deleter
	def ClntTrptyCollTxId(self):
		del self._ClntTrptyCollTxId
		self._ClntTrptyCollTxId = base_types.UninitialisedField(self, 'ClntTrptyCollTxId', Max35Text, False)

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
	def CmonTxId(self):
		return self._CmonTxId

	@CmonTxId.setter
	def CmonTxId(self, value):
		self._CmonTxId = value if value is not None else base_types.UninitialisedField(self, 'CmonTxId', Max52Text, False)

	@CmonTxId.deleter
	def CmonTxId(self):
		del self._CmonTxId
		self._CmonTxId = base_types.UninitialisedField(self, 'CmonTxId', Max52Text, False)

	@property
	def CollPties(self):
		return self._CollPties

	@CollPties.setter
	def CollPties(self, value):
		self._CollPties = value if value is not None else base_types.UninitialisedField(self, 'CollPties', CollateralParties11, False)

	@CollPties.deleter
	def CollPties(self):
		del self._CollPties
		self._CollPties = base_types.UninitialisedField(self, 'CollPties', CollateralParties11, False)

	@property
	def CshBal(self):
		return self._CshBal

	@CshBal.setter
	def CshBal(self, value):
		self._CshBal = value if value is not None else base_types.UninitialisedField(self, 'CshBal', CashBalance15, True)

	@CshBal.deleter
	def CshBal(self):
		del self._CshBal
		self._CshBal = base_types.UninitialisedField(self, 'CshBal', CashBalance15, True)

	@property
	def CtrPtyCollTxRef(self):
		return self._CtrPtyCollTxRef

	@CtrPtyCollTxRef.setter
	def CtrPtyCollTxRef(self, value):
		self._CtrPtyCollTxRef = value if value is not None else base_types.UninitialisedField(self, 'CtrPtyCollTxRef', Max35Text, False)

	@CtrPtyCollTxRef.deleter
	def CtrPtyCollTxRef(self):
		del self._CtrPtyCollTxRef
		self._CtrPtyCollTxRef = base_types.UninitialisedField(self, 'CtrPtyCollTxRef', Max35Text, False)

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
	def ExctnReqdDt(self):
		return self._ExctnReqdDt

	@ExctnReqdDt.setter
	def ExctnReqdDt(self, value):
		self._ExctnReqdDt = value if value is not None else base_types.UninitialisedField(self, 'ExctnReqdDt', ClosingDate4Choice, False)

	@ExctnReqdDt.deleter
	def ExctnReqdDt(self):
		del self._ExctnReqdDt
		self._ExctnReqdDt = base_types.UninitialisedField(self, 'ExctnReqdDt', ClosingDate4Choice, False)

	@property
	def MrgnRate(self):
		return self._MrgnRate

	@MrgnRate.setter
	def MrgnRate(self, value):
		self._MrgnRate = value if value is not None else base_types.UninitialisedField(self, 'MrgnRate', PercentageRate, False)

	@MrgnRate.deleter
	def MrgnRate(self):
		del self._MrgnRate
		self._MrgnRate = base_types.UninitialisedField(self, 'MrgnRate', PercentageRate, False)

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
	def PricgRate(self):
		return self._PricgRate

	@PricgRate.setter
	def PricgRate(self, value):
		self._PricgRate = value if value is not None else base_types.UninitialisedField(self, 'PricgRate', RateOrName4Choice, False)

	@PricgRate.deleter
	def PricgRate(self):
		del self._PricgRate
		self._PricgRate = base_types.UninitialisedField(self, 'PricgRate', RateOrName4Choice, False)

	@property
	def SctiesBal(self):
		return self._SctiesBal

	@SctiesBal.setter
	def SctiesBal(self, value):
		self._SctiesBal = value if value is not None else base_types.UninitialisedField(self, 'SctiesBal', SecuritiesBalance3, True)

	@SctiesBal.deleter
	def SctiesBal(self):
		del self._SctiesBal
		self._SctiesBal = base_types.UninitialisedField(self, 'SctiesBal', SecuritiesBalance3, True)

	@property
	def SprdRate(self):
		return self._SprdRate

	@SprdRate.setter
	def SprdRate(self, value):
		self._SprdRate = value if value is not None else base_types.UninitialisedField(self, 'SprdRate', PercentageRate, False)

	@SprdRate.deleter
	def SprdRate(self):
		del self._SprdRate
		self._SprdRate = base_types.UninitialisedField(self, 'SprdRate', PercentageRate, False)

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

	@property
	def TrptyAgtSvcPrvdrCollTxId(self):
		return self._TrptyAgtSvcPrvdrCollTxId

	@TrptyAgtSvcPrvdrCollTxId.setter
	def TrptyAgtSvcPrvdrCollTxId(self, value):
		self._TrptyAgtSvcPrvdrCollTxId = value if value is not None else base_types.UninitialisedField(self, 'TrptyAgtSvcPrvdrCollTxId', Max35Text, False)

	@TrptyAgtSvcPrvdrCollTxId.deleter
	def TrptyAgtSvcPrvdrCollTxId(self):
		del self._TrptyAgtSvcPrvdrCollTxId
		self._TrptyAgtSvcPrvdrCollTxId = base_types.UninitialisedField(self, 'TrptyAgtSvcPrvdrCollTxId', Max35Text, False)

	@property
	def TxSts(self):
		return self._TxSts

	@TxSts.setter
	def TxSts(self, value):
		self._TxSts = value if value is not None else base_types.UninitialisedField(self, 'TxSts', TransactionStatus6, True)

	@TxSts.deleter
	def TxSts(self):
		del self._TxSts
		self._TxSts = base_types.UninitialisedField(self, 'TxSts', TransactionStatus6, True)

	@property
	def ValtnAmts(self):
		return self._ValtnAmts

	@ValtnAmts.setter
	def ValtnAmts(self, value):
		self._ValtnAmts = value if value is not None else base_types.UninitialisedField(self, 'ValtnAmts', CollateralAmount17, False)

	@ValtnAmts.deleter
	def ValtnAmts(self):
		del self._ValtnAmts
		self._ValtnAmts = base_types.UninitialisedField(self, 'ValtnAmts', CollateralAmount17, False)

	@property
	def XpsrTp(self):
		return self._XpsrTp

	@XpsrTp.setter
	def XpsrTp(self, value):
		self._XpsrTp = value if value is not None else base_types.UninitialisedField(self, 'XpsrTp', ExposureType23Choice, False)

	@XpsrTp.deleter
	def XpsrTp(self):
		del self._XpsrTp
		self._XpsrTp = base_types.UninitialisedField(self, 'XpsrTp', ExposureType23Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AutomtcAllcn', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BsktIdAndElgbltySetPrfl', type=BasketIdentificationAndEligibilitySetProfile1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntTrptyCollTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClsgDt', type=ClosingDate4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmonTxId', type=Max52Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollPties', type=CollateralParties11, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshBal', type=CashBalance15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CtrPtyCollTxRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DayCntBsis', type=InterestComputationMethodFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExctnReqdDt', type=ClosingDate4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnTp', type=OptionType6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricgRate', type=RateOrName4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesBal', type=SecuritiesBalance3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SprdRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TermntnOptn', type=RepoTerminationOption1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrptyAgtSvcPrvdrCollTxId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxSts', type=TransactionStatus6, min=0, max=2, mutex_group=None, array=True),
		base_types.FieldEntry(name='ValtnAmts', type=CollateralAmount17, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpsrTp', type=ExposureType23Choice, min=1, max=1, mutex_group=None, array=False),
	))