from . import base_types
import CollateralDirection1Code
import SettlementStatus3Code
import CashCollateral4
import CollateralType8Code
import CollateralAppliedExcess1Code
import Max35Text
import Number
import SecuritiesCollateral13
import OtherCollateral10
import InterestComputationMethod2Code
import BaseOneRate
import CollateralAmount1

class CollateralValuation13(base_types._BaseFieldType):

	__slots__ = ["_CcyHrcut", "_CollId", "_ApldXcssInd", "_CollTp", "_CollDrctn", "_AdjstdRate", "_SctiesColl", "_ValtnAmts", "_DayCntBsis", "_NbOfDaysAcrd", "_CshColl", "_OthrColl", "_SttlmSts", "_XchgRate"]
	@property
	def CcyHrcut(self):
		return self._CcyHrcut

	@CcyHrcut.setter
	def CcyHrcut(self, value):
		self._CcyHrcut = value if type(value) != auto else self.make_default("CcyHrcut")

	@CcyHrcut.deleter
	def CcyHrcut(self):
		del self._CcyHrcut
		self._CcyHrcut = None

	@property
	def CollId(self):
		return self._CollId

	@CollId.setter
	def CollId(self, value):
		self._CollId = value if type(value) != auto else self.make_default("CollId")

	@CollId.deleter
	def CollId(self):
		del self._CollId
		self._CollId = None

	@property
	def ApldXcssInd(self):
		return self._ApldXcssInd

	@ApldXcssInd.setter
	def ApldXcssInd(self, value):
		self._ApldXcssInd = value if type(value) != auto else self.make_default("ApldXcssInd")

	@ApldXcssInd.deleter
	def ApldXcssInd(self):
		del self._ApldXcssInd
		self._ApldXcssInd = None

	@property
	def CollTp(self):
		return self._CollTp

	@CollTp.setter
	def CollTp(self, value):
		self._CollTp = value if type(value) != auto else self.make_default("CollTp")

	@CollTp.deleter
	def CollTp(self):
		del self._CollTp
		self._CollTp = None

	@property
	def CollDrctn(self):
		return self._CollDrctn

	@CollDrctn.setter
	def CollDrctn(self, value):
		self._CollDrctn = value if type(value) != auto else self.make_default("CollDrctn")

	@CollDrctn.deleter
	def CollDrctn(self):
		del self._CollDrctn
		self._CollDrctn = None

	@property
	def AdjstdRate(self):
		return self._AdjstdRate

	@AdjstdRate.setter
	def AdjstdRate(self, value):
		self._AdjstdRate = value if type(value) != auto else self.make_default("AdjstdRate")

	@AdjstdRate.deleter
	def AdjstdRate(self):
		del self._AdjstdRate
		self._AdjstdRate = None

	@property
	def SctiesColl(self):
		return self._SctiesColl

	@SctiesColl.setter
	def SctiesColl(self, value):
		self._SctiesColl = value if type(value) != auto else self.make_default("SctiesColl")

	@SctiesColl.deleter
	def SctiesColl(self):
		del self._SctiesColl
		self._SctiesColl = None

	@property
	def ValtnAmts(self):
		return self._ValtnAmts

	@ValtnAmts.setter
	def ValtnAmts(self, value):
		self._ValtnAmts = value if type(value) != auto else self.make_default("ValtnAmts")

	@ValtnAmts.deleter
	def ValtnAmts(self):
		del self._ValtnAmts
		self._ValtnAmts = None

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
	def NbOfDaysAcrd(self):
		return self._NbOfDaysAcrd

	@NbOfDaysAcrd.setter
	def NbOfDaysAcrd(self, value):
		self._NbOfDaysAcrd = value if type(value) != auto else self.make_default("NbOfDaysAcrd")

	@NbOfDaysAcrd.deleter
	def NbOfDaysAcrd(self):
		del self._NbOfDaysAcrd
		self._NbOfDaysAcrd = None

	@property
	def CshColl(self):
		return self._CshColl

	@CshColl.setter
	def CshColl(self, value):
		self._CshColl = value if type(value) != auto else self.make_default("CshColl")

	@CshColl.deleter
	def CshColl(self):
		del self._CshColl
		self._CshColl = None

	@property
	def OthrColl(self):
		return self._OthrColl

	@OthrColl.setter
	def OthrColl(self, value):
		self._OthrColl = value if type(value) != auto else self.make_default("OthrColl")

	@OthrColl.deleter
	def OthrColl(self):
		del self._OthrColl
		self._OthrColl = None

	@property
	def SttlmSts(self):
		return self._SttlmSts

	@SttlmSts.setter
	def SttlmSts(self, value):
		self._SttlmSts = value if type(value) != auto else self.make_default("SttlmSts")

	@SttlmSts.deleter
	def SttlmSts(self):
		del self._SttlmSts
		self._SttlmSts = None

	@property
	def XchgRate(self):
		return self._XchgRate

	@XchgRate.setter
	def XchgRate(self, value):
		self._XchgRate = value if type(value) != auto else self.make_default("XchgRate")

	@XchgRate.deleter
	def XchgRate(self):
		del self._XchgRate
		self._XchgRate = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CcyHrcut', type=BaseOneRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ApldXcssInd', type=CollateralAppliedExcess1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollTp', type=CollateralType8Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollDrctn', type=CollateralDirection1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AdjstdRate', type=BaseOneRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesColl', type=SecuritiesCollateral13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValtnAmts', type=CollateralAmount1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DayCntBsis', type=InterestComputationMethod2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfDaysAcrd', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshColl', type=CashCollateral4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrColl', type=OtherCollateral10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmSts', type=SettlementStatus3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgRate', type=BaseOneRate, min=0, max=1, mutex_group=None, array=False),
	))

