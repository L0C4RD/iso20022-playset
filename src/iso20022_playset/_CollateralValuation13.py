# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BaseOneRate
from . import CashCollateral4
from . import CollateralAmount1
from . import CollateralAppliedExcess1Code
from . import CollateralDirection1Code
from . import CollateralType8Code
from . import InterestComputationMethod2Code
from . import Max35Text
from . import Number
from . import OtherCollateral10
from . import SecuritiesCollateral13
from . import SettlementStatus3Code

class CollateralValuation13(base_types._BaseFieldType):

	__slots__ = ["_AdjstdRate", "_ApldXcssInd", "_CcyHrcut", "_CollDrctn", "_CollId", "_CollTp", "_CshColl", "_DayCntBsis", "_NbOfDaysAcrd", "_OthrColl", "_SctiesColl", "_SttlmSts", "_ValtnAmts", "_XchgRate"]
	@property
	def AdjstdRate(self):
		return self._AdjstdRate

	@AdjstdRate.setter
	def AdjstdRate(self, value):
		self._AdjstdRate = value if value is not None else base_types.UninitialisedField(self, 'AdjstdRate', BaseOneRate, False)

	@AdjstdRate.deleter
	def AdjstdRate(self):
		del self._AdjstdRate
		self._AdjstdRate = base_types.UninitialisedField(self, 'AdjstdRate', BaseOneRate, False)

	@property
	def ApldXcssInd(self):
		return self._ApldXcssInd

	@ApldXcssInd.setter
	def ApldXcssInd(self, value):
		self._ApldXcssInd = value if value is not None else base_types.UninitialisedField(self, 'ApldXcssInd', CollateralAppliedExcess1Code, False)

	@ApldXcssInd.deleter
	def ApldXcssInd(self):
		del self._ApldXcssInd
		self._ApldXcssInd = base_types.UninitialisedField(self, 'ApldXcssInd', CollateralAppliedExcess1Code, False)

	@property
	def CcyHrcut(self):
		return self._CcyHrcut

	@CcyHrcut.setter
	def CcyHrcut(self, value):
		self._CcyHrcut = value if value is not None else base_types.UninitialisedField(self, 'CcyHrcut', BaseOneRate, False)

	@CcyHrcut.deleter
	def CcyHrcut(self):
		del self._CcyHrcut
		self._CcyHrcut = base_types.UninitialisedField(self, 'CcyHrcut', BaseOneRate, False)

	@property
	def CollDrctn(self):
		return self._CollDrctn

	@CollDrctn.setter
	def CollDrctn(self, value):
		self._CollDrctn = value if value is not None else base_types.UninitialisedField(self, 'CollDrctn', CollateralDirection1Code, False)

	@CollDrctn.deleter
	def CollDrctn(self):
		del self._CollDrctn
		self._CollDrctn = base_types.UninitialisedField(self, 'CollDrctn', CollateralDirection1Code, False)

	@property
	def CollId(self):
		return self._CollId

	@CollId.setter
	def CollId(self, value):
		self._CollId = value if value is not None else base_types.UninitialisedField(self, 'CollId', Max35Text, False)

	@CollId.deleter
	def CollId(self):
		del self._CollId
		self._CollId = base_types.UninitialisedField(self, 'CollId', Max35Text, False)

	@property
	def CollTp(self):
		return self._CollTp

	@CollTp.setter
	def CollTp(self, value):
		self._CollTp = value if value is not None else base_types.UninitialisedField(self, 'CollTp', CollateralType8Code, False)

	@CollTp.deleter
	def CollTp(self):
		del self._CollTp
		self._CollTp = base_types.UninitialisedField(self, 'CollTp', CollateralType8Code, False)

	@property
	def CshColl(self):
		return self._CshColl

	@CshColl.setter
	def CshColl(self, value):
		self._CshColl = value if value is not None else base_types.UninitialisedField(self, 'CshColl', CashCollateral4, False)

	@CshColl.deleter
	def CshColl(self):
		del self._CshColl
		self._CshColl = base_types.UninitialisedField(self, 'CshColl', CashCollateral4, False)

	@property
	def DayCntBsis(self):
		return self._DayCntBsis

	@DayCntBsis.setter
	def DayCntBsis(self, value):
		self._DayCntBsis = value if value is not None else base_types.UninitialisedField(self, 'DayCntBsis', InterestComputationMethod2Code, False)

	@DayCntBsis.deleter
	def DayCntBsis(self):
		del self._DayCntBsis
		self._DayCntBsis = base_types.UninitialisedField(self, 'DayCntBsis', InterestComputationMethod2Code, False)

	@property
	def NbOfDaysAcrd(self):
		return self._NbOfDaysAcrd

	@NbOfDaysAcrd.setter
	def NbOfDaysAcrd(self, value):
		self._NbOfDaysAcrd = value if value is not None else base_types.UninitialisedField(self, 'NbOfDaysAcrd', Number, False)

	@NbOfDaysAcrd.deleter
	def NbOfDaysAcrd(self):
		del self._NbOfDaysAcrd
		self._NbOfDaysAcrd = base_types.UninitialisedField(self, 'NbOfDaysAcrd', Number, False)

	@property
	def OthrColl(self):
		return self._OthrColl

	@OthrColl.setter
	def OthrColl(self, value):
		self._OthrColl = value if value is not None else base_types.UninitialisedField(self, 'OthrColl', OtherCollateral10, False)

	@OthrColl.deleter
	def OthrColl(self):
		del self._OthrColl
		self._OthrColl = base_types.UninitialisedField(self, 'OthrColl', OtherCollateral10, False)

	@property
	def SctiesColl(self):
		return self._SctiesColl

	@SctiesColl.setter
	def SctiesColl(self, value):
		self._SctiesColl = value if value is not None else base_types.UninitialisedField(self, 'SctiesColl', SecuritiesCollateral13, False)

	@SctiesColl.deleter
	def SctiesColl(self):
		del self._SctiesColl
		self._SctiesColl = base_types.UninitialisedField(self, 'SctiesColl', SecuritiesCollateral13, False)

	@property
	def SttlmSts(self):
		return self._SttlmSts

	@SttlmSts.setter
	def SttlmSts(self, value):
		self._SttlmSts = value if value is not None else base_types.UninitialisedField(self, 'SttlmSts', SettlementStatus3Code, False)

	@SttlmSts.deleter
	def SttlmSts(self):
		del self._SttlmSts
		self._SttlmSts = base_types.UninitialisedField(self, 'SttlmSts', SettlementStatus3Code, False)

	@property
	def ValtnAmts(self):
		return self._ValtnAmts

	@ValtnAmts.setter
	def ValtnAmts(self, value):
		self._ValtnAmts = value if value is not None else base_types.UninitialisedField(self, 'ValtnAmts', CollateralAmount1, False)

	@ValtnAmts.deleter
	def ValtnAmts(self):
		del self._ValtnAmts
		self._ValtnAmts = base_types.UninitialisedField(self, 'ValtnAmts', CollateralAmount1, False)

	@property
	def XchgRate(self):
		return self._XchgRate

	@XchgRate.setter
	def XchgRate(self, value):
		self._XchgRate = value if value is not None else base_types.UninitialisedField(self, 'XchgRate', BaseOneRate, False)

	@XchgRate.deleter
	def XchgRate(self):
		del self._XchgRate
		self._XchgRate = base_types.UninitialisedField(self, 'XchgRate', BaseOneRate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AdjstdRate', type=BaseOneRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ApldXcssInd', type=CollateralAppliedExcess1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CcyHrcut', type=BaseOneRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollDrctn', type=CollateralDirection1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollTp', type=CollateralType8Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshColl', type=CashCollateral4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DayCntBsis', type=InterestComputationMethod2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfDaysAcrd', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrColl', type=OtherCollateral10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesColl', type=SecuritiesCollateral13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmSts', type=SettlementStatus3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValtnAmts', type=CollateralAmount1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgRate', type=BaseOneRate, min=0, max=1, mutex_group=None, array=False),
	))