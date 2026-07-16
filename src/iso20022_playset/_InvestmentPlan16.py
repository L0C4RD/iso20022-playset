# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CashSettlement4
from . import Frequency20Choice
from . import ISODate
from . import IncomePreference2Code
from . import InitialAmount1Choice
from . import InsuranceType2Choice
from . import Max35Text
from . import Number
from . import PartyRole4Choice
from . import PlanStatus2Choice
from . import Repartition6
from . import RoundingDirection1Code
from . import UnitsOrAmount1Choice
from . import YesNoIndicator

class InvestmentPlan16(base_types._BaseFieldType):

	__slots__ = ["_CtrctRef", "_EndDt", "_Frqcy", "_GrssAmtInd", "_IncmPref", "_InitlAmt", "_InsrncCover", "_InstlmtMgrRole", "_ModfdCshSttlm", "_PdctId", "_PlanSts", "_Qty", "_RltdCtrctRef", "_RndgDrctn", "_SLAChrgAndComssnRef", "_SctyDtls", "_StartDt", "_TtlNbOfInstlmts"]
	@property
	def CtrctRef(self):
		return self._CtrctRef

	@CtrctRef.setter
	def CtrctRef(self, value):
		self._CtrctRef = value if value is not None else base_types.UninitialisedField(self, 'CtrctRef', Max35Text, False)

	@CtrctRef.deleter
	def CtrctRef(self):
		del self._CtrctRef
		self._CtrctRef = base_types.UninitialisedField(self, 'CtrctRef', Max35Text, False)

	@property
	def EndDt(self):
		return self._EndDt

	@EndDt.setter
	def EndDt(self, value):
		self._EndDt = value if value is not None else base_types.UninitialisedField(self, 'EndDt', ISODate, False)

	@EndDt.deleter
	def EndDt(self):
		del self._EndDt
		self._EndDt = base_types.UninitialisedField(self, 'EndDt', ISODate, False)

	@property
	def Frqcy(self):
		return self._Frqcy

	@Frqcy.setter
	def Frqcy(self, value):
		self._Frqcy = value if value is not None else base_types.UninitialisedField(self, 'Frqcy', Frequency20Choice, False)

	@Frqcy.deleter
	def Frqcy(self):
		del self._Frqcy
		self._Frqcy = base_types.UninitialisedField(self, 'Frqcy', Frequency20Choice, False)

	@property
	def GrssAmtInd(self):
		return self._GrssAmtInd

	@GrssAmtInd.setter
	def GrssAmtInd(self, value):
		self._GrssAmtInd = value if value is not None else base_types.UninitialisedField(self, 'GrssAmtInd', YesNoIndicator, False)

	@GrssAmtInd.deleter
	def GrssAmtInd(self):
		del self._GrssAmtInd
		self._GrssAmtInd = base_types.UninitialisedField(self, 'GrssAmtInd', YesNoIndicator, False)

	@property
	def IncmPref(self):
		return self._IncmPref

	@IncmPref.setter
	def IncmPref(self, value):
		self._IncmPref = value if value is not None else base_types.UninitialisedField(self, 'IncmPref', IncomePreference2Code, False)

	@IncmPref.deleter
	def IncmPref(self):
		del self._IncmPref
		self._IncmPref = base_types.UninitialisedField(self, 'IncmPref', IncomePreference2Code, False)

	@property
	def InitlAmt(self):
		return self._InitlAmt

	@InitlAmt.setter
	def InitlAmt(self, value):
		self._InitlAmt = value if value is not None else base_types.UninitialisedField(self, 'InitlAmt', InitialAmount1Choice, False)

	@InitlAmt.deleter
	def InitlAmt(self):
		del self._InitlAmt
		self._InitlAmt = base_types.UninitialisedField(self, 'InitlAmt', InitialAmount1Choice, False)

	@property
	def InsrncCover(self):
		return self._InsrncCover

	@InsrncCover.setter
	def InsrncCover(self, value):
		self._InsrncCover = value if value is not None else base_types.UninitialisedField(self, 'InsrncCover', InsuranceType2Choice, False)

	@InsrncCover.deleter
	def InsrncCover(self):
		del self._InsrncCover
		self._InsrncCover = base_types.UninitialisedField(self, 'InsrncCover', InsuranceType2Choice, False)

	@property
	def InstlmtMgrRole(self):
		return self._InstlmtMgrRole

	@InstlmtMgrRole.setter
	def InstlmtMgrRole(self, value):
		self._InstlmtMgrRole = value if value is not None else base_types.UninitialisedField(self, 'InstlmtMgrRole', PartyRole4Choice, False)

	@InstlmtMgrRole.deleter
	def InstlmtMgrRole(self):
		del self._InstlmtMgrRole
		self._InstlmtMgrRole = base_types.UninitialisedField(self, 'InstlmtMgrRole', PartyRole4Choice, False)

	@property
	def ModfdCshSttlm(self):
		return self._ModfdCshSttlm

	@ModfdCshSttlm.setter
	def ModfdCshSttlm(self, value):
		self._ModfdCshSttlm = value if value is not None else base_types.UninitialisedField(self, 'ModfdCshSttlm', CashSettlement4, True)

	@ModfdCshSttlm.deleter
	def ModfdCshSttlm(self):
		del self._ModfdCshSttlm
		self._ModfdCshSttlm = base_types.UninitialisedField(self, 'ModfdCshSttlm', CashSettlement4, True)

	@property
	def PdctId(self):
		return self._PdctId

	@PdctId.setter
	def PdctId(self, value):
		self._PdctId = value if value is not None else base_types.UninitialisedField(self, 'PdctId', Max35Text, False)

	@PdctId.deleter
	def PdctId(self):
		del self._PdctId
		self._PdctId = base_types.UninitialisedField(self, 'PdctId', Max35Text, False)

	@property
	def PlanSts(self):
		return self._PlanSts

	@PlanSts.setter
	def PlanSts(self, value):
		self._PlanSts = value if value is not None else base_types.UninitialisedField(self, 'PlanSts', PlanStatus2Choice, False)

	@PlanSts.deleter
	def PlanSts(self):
		del self._PlanSts
		self._PlanSts = base_types.UninitialisedField(self, 'PlanSts', PlanStatus2Choice, False)

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if value is not None else base_types.UninitialisedField(self, 'Qty', UnitsOrAmount1Choice, False)

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = base_types.UninitialisedField(self, 'Qty', UnitsOrAmount1Choice, False)

	@property
	def RltdCtrctRef(self):
		return self._RltdCtrctRef

	@RltdCtrctRef.setter
	def RltdCtrctRef(self, value):
		self._RltdCtrctRef = value if value is not None else base_types.UninitialisedField(self, 'RltdCtrctRef', Max35Text, False)

	@RltdCtrctRef.deleter
	def RltdCtrctRef(self):
		del self._RltdCtrctRef
		self._RltdCtrctRef = base_types.UninitialisedField(self, 'RltdCtrctRef', Max35Text, False)

	@property
	def RndgDrctn(self):
		return self._RndgDrctn

	@RndgDrctn.setter
	def RndgDrctn(self, value):
		self._RndgDrctn = value if value is not None else base_types.UninitialisedField(self, 'RndgDrctn', RoundingDirection1Code, False)

	@RndgDrctn.deleter
	def RndgDrctn(self):
		del self._RndgDrctn
		self._RndgDrctn = base_types.UninitialisedField(self, 'RndgDrctn', RoundingDirection1Code, False)

	@property
	def SLAChrgAndComssnRef(self):
		return self._SLAChrgAndComssnRef

	@SLAChrgAndComssnRef.setter
	def SLAChrgAndComssnRef(self, value):
		self._SLAChrgAndComssnRef = value if value is not None else base_types.UninitialisedField(self, 'SLAChrgAndComssnRef', Max35Text, False)

	@SLAChrgAndComssnRef.deleter
	def SLAChrgAndComssnRef(self):
		del self._SLAChrgAndComssnRef
		self._SLAChrgAndComssnRef = base_types.UninitialisedField(self, 'SLAChrgAndComssnRef', Max35Text, False)

	@property
	def SctyDtls(self):
		return self._SctyDtls

	@SctyDtls.setter
	def SctyDtls(self, value):
		self._SctyDtls = value if value is not None else base_types.UninitialisedField(self, 'SctyDtls', Repartition6, True)

	@SctyDtls.deleter
	def SctyDtls(self):
		del self._SctyDtls
		self._SctyDtls = base_types.UninitialisedField(self, 'SctyDtls', Repartition6, True)

	@property
	def StartDt(self):
		return self._StartDt

	@StartDt.setter
	def StartDt(self, value):
		self._StartDt = value if value is not None else base_types.UninitialisedField(self, 'StartDt', ISODate, False)

	@StartDt.deleter
	def StartDt(self):
		del self._StartDt
		self._StartDt = base_types.UninitialisedField(self, 'StartDt', ISODate, False)

	@property
	def TtlNbOfInstlmts(self):
		return self._TtlNbOfInstlmts

	@TtlNbOfInstlmts.setter
	def TtlNbOfInstlmts(self, value):
		self._TtlNbOfInstlmts = value if value is not None else base_types.UninitialisedField(self, 'TtlNbOfInstlmts', Number, False)

	@TtlNbOfInstlmts.deleter
	def TtlNbOfInstlmts(self):
		del self._TtlNbOfInstlmts
		self._TtlNbOfInstlmts = base_types.UninitialisedField(self, 'TtlNbOfInstlmts', Number, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtrctRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EndDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Frqcy', type=Frequency20Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrssAmtInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IncmPref', type=IncomePreference2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitlAmt', type=InitialAmount1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InsrncCover', type=InsuranceType2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstlmtMgrRole', type=PartyRole4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ModfdCshSttlm', type=CashSettlement4, min=0, max=8, mutex_group=None, array=True),
		base_types.FieldEntry(name='PdctId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlanSts', type=PlanStatus2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=UnitsOrAmount1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdCtrctRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RndgDrctn', type=RoundingDirection1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SLAChrgAndComssnRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyDtls', type=Repartition6, min=1, max=50, mutex_group=None, array=True),
		base_types.FieldEntry(name='StartDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNbOfInstlmts', type=Number, min=0, max=1, mutex_group=None, array=False),
	))