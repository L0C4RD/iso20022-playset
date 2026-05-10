import base_types
import InitialAmount1Choice
import Frequency20Choice
import YesNoIndicator
import PartyRole4Choice
import InsuranceType2Choice
import IncomePreference2Code
import ISODate
import Number
import Max35Text
import RoundingDirection1Code
import CashSettlement3
import UnitsOrAmount1Choice
import Repartition6
import PlanStatus2Choice

class InvestmentPlan17(base_types._BaseFieldType):

	__slots__ = ["_SctyDtls", "_PlanSts", "_Frqcy", "_InsrncCover", "_RndgDrctn", "_PdctId", "_IncmPref", "_CshSttlm", "_StartDt", "_EndDt", "_TtlNbOfInstlmts", "_SLAChrgAndComssnRef", "_InitlAmt", "_Qty", "_CtrctRef", "_InstlmtMgrRole", "_RltdCtrctRef", "_GrssAmtInd"]
	@property
	def SctyDtls(self):
		return self._SctyDtls

	@SctyDtls.setter
	def SctyDtls(self, value):
		self._SctyDtls = value if type(value) != auto else self.make_default("SctyDtls")

	@SctyDtls.deleter
	def SctyDtls(self):
		del self._SctyDtls
		self._SctyDtls = None

	@property
	def PlanSts(self):
		return self._PlanSts

	@PlanSts.setter
	def PlanSts(self, value):
		self._PlanSts = value if type(value) != auto else self.make_default("PlanSts")

	@PlanSts.deleter
	def PlanSts(self):
		del self._PlanSts
		self._PlanSts = None

	@property
	def Frqcy(self):
		return self._Frqcy

	@Frqcy.setter
	def Frqcy(self, value):
		self._Frqcy = value if type(value) != auto else self.make_default("Frqcy")

	@Frqcy.deleter
	def Frqcy(self):
		del self._Frqcy
		self._Frqcy = None

	@property
	def InsrncCover(self):
		return self._InsrncCover

	@InsrncCover.setter
	def InsrncCover(self, value):
		self._InsrncCover = value if type(value) != auto else self.make_default("InsrncCover")

	@InsrncCover.deleter
	def InsrncCover(self):
		del self._InsrncCover
		self._InsrncCover = None

	@property
	def RndgDrctn(self):
		return self._RndgDrctn

	@RndgDrctn.setter
	def RndgDrctn(self, value):
		self._RndgDrctn = value if type(value) != auto else self.make_default("RndgDrctn")

	@RndgDrctn.deleter
	def RndgDrctn(self):
		del self._RndgDrctn
		self._RndgDrctn = None

	@property
	def PdctId(self):
		return self._PdctId

	@PdctId.setter
	def PdctId(self, value):
		self._PdctId = value if type(value) != auto else self.make_default("PdctId")

	@PdctId.deleter
	def PdctId(self):
		del self._PdctId
		self._PdctId = None

	@property
	def IncmPref(self):
		return self._IncmPref

	@IncmPref.setter
	def IncmPref(self, value):
		self._IncmPref = value if type(value) != auto else self.make_default("IncmPref")

	@IncmPref.deleter
	def IncmPref(self):
		del self._IncmPref
		self._IncmPref = None

	@property
	def CshSttlm(self):
		return self._CshSttlm

	@CshSttlm.setter
	def CshSttlm(self, value):
		self._CshSttlm = value if type(value) != auto else self.make_default("CshSttlm")

	@CshSttlm.deleter
	def CshSttlm(self):
		del self._CshSttlm
		self._CshSttlm = None

	@property
	def StartDt(self):
		return self._StartDt

	@StartDt.setter
	def StartDt(self, value):
		self._StartDt = value if type(value) != auto else self.make_default("StartDt")

	@StartDt.deleter
	def StartDt(self):
		del self._StartDt
		self._StartDt = None

	@property
	def EndDt(self):
		return self._EndDt

	@EndDt.setter
	def EndDt(self, value):
		self._EndDt = value if type(value) != auto else self.make_default("EndDt")

	@EndDt.deleter
	def EndDt(self):
		del self._EndDt
		self._EndDt = None

	@property
	def TtlNbOfInstlmts(self):
		return self._TtlNbOfInstlmts

	@TtlNbOfInstlmts.setter
	def TtlNbOfInstlmts(self, value):
		self._TtlNbOfInstlmts = value if type(value) != auto else self.make_default("TtlNbOfInstlmts")

	@TtlNbOfInstlmts.deleter
	def TtlNbOfInstlmts(self):
		del self._TtlNbOfInstlmts
		self._TtlNbOfInstlmts = None

	@property
	def SLAChrgAndComssnRef(self):
		return self._SLAChrgAndComssnRef

	@SLAChrgAndComssnRef.setter
	def SLAChrgAndComssnRef(self, value):
		self._SLAChrgAndComssnRef = value if type(value) != auto else self.make_default("SLAChrgAndComssnRef")

	@SLAChrgAndComssnRef.deleter
	def SLAChrgAndComssnRef(self):
		del self._SLAChrgAndComssnRef
		self._SLAChrgAndComssnRef = None

	@property
	def InitlAmt(self):
		return self._InitlAmt

	@InitlAmt.setter
	def InitlAmt(self, value):
		self._InitlAmt = value if type(value) != auto else self.make_default("InitlAmt")

	@InitlAmt.deleter
	def InitlAmt(self):
		del self._InitlAmt
		self._InitlAmt = None

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if type(value) != auto else self.make_default("Qty")

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = None

	@property
	def CtrctRef(self):
		return self._CtrctRef

	@CtrctRef.setter
	def CtrctRef(self, value):
		self._CtrctRef = value if type(value) != auto else self.make_default("CtrctRef")

	@CtrctRef.deleter
	def CtrctRef(self):
		del self._CtrctRef
		self._CtrctRef = None

	@property
	def InstlmtMgrRole(self):
		return self._InstlmtMgrRole

	@InstlmtMgrRole.setter
	def InstlmtMgrRole(self, value):
		self._InstlmtMgrRole = value if type(value) != auto else self.make_default("InstlmtMgrRole")

	@InstlmtMgrRole.deleter
	def InstlmtMgrRole(self):
		del self._InstlmtMgrRole
		self._InstlmtMgrRole = None

	@property
	def RltdCtrctRef(self):
		return self._RltdCtrctRef

	@RltdCtrctRef.setter
	def RltdCtrctRef(self, value):
		self._RltdCtrctRef = value if type(value) != auto else self.make_default("RltdCtrctRef")

	@RltdCtrctRef.deleter
	def RltdCtrctRef(self):
		del self._RltdCtrctRef
		self._RltdCtrctRef = None

	@property
	def GrssAmtInd(self):
		return self._GrssAmtInd

	@GrssAmtInd.setter
	def GrssAmtInd(self, value):
		self._GrssAmtInd = value if type(value) != auto else self.make_default("GrssAmtInd")

	@GrssAmtInd.deleter
	def GrssAmtInd(self):
		del self._GrssAmtInd
		self._GrssAmtInd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SctyDtls', type=Repartition6, min=1, max=50, mutex_group=None, array=True),
		base_types.FieldEntry(name='PlanSts', type=PlanStatus2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Frqcy', type=Frequency20Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InsrncCover', type=InsuranceType2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RndgDrctn', type=RoundingDirection1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IncmPref', type=IncomePreference2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshSttlm', type=CashSettlement3, min=0, max=8, mutex_group=None, array=True),
		base_types.FieldEntry(name='StartDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EndDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNbOfInstlmts', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SLAChrgAndComssnRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitlAmt', type=InitialAmount1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=UnitsOrAmount1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstlmtMgrRole', type=PartyRole4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdCtrctRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrssAmtInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
	))

