import base_types
import ISODate
import CollateralType19
import SupplementaryData1
import ISODateTime
import FundingSource3
import ReconciliationFlag2
import ContractModification3
import CounterpartyData87
import Max140Text

class ReuseDataReportCorrection15(base_types._BaseFieldType):

	__slots__ = ["_RcncltnFlg", "_TechRcrdId", "_CollCmpnt", "_CtrctMod", "_CtrPty", "_SplmtryData", "_FndgSrc", "_RptgDtTm", "_EvtDay"]
	@property
	def RcncltnFlg(self):
		return self._RcncltnFlg

	@RcncltnFlg.setter
	def RcncltnFlg(self, value):
		self._RcncltnFlg = value if type(value) != auto else self.make_default("RcncltnFlg")

	@RcncltnFlg.deleter
	def RcncltnFlg(self):
		del self._RcncltnFlg
		self._RcncltnFlg = None

	@property
	def TechRcrdId(self):
		return self._TechRcrdId

	@TechRcrdId.setter
	def TechRcrdId(self, value):
		self._TechRcrdId = value if type(value) != auto else self.make_default("TechRcrdId")

	@TechRcrdId.deleter
	def TechRcrdId(self):
		del self._TechRcrdId
		self._TechRcrdId = None

	@property
	def CollCmpnt(self):
		return self._CollCmpnt

	@CollCmpnt.setter
	def CollCmpnt(self, value):
		self._CollCmpnt = value if type(value) != auto else self.make_default("CollCmpnt")

	@CollCmpnt.deleter
	def CollCmpnt(self):
		del self._CollCmpnt
		self._CollCmpnt = None

	@property
	def CtrctMod(self):
		return self._CtrctMod

	@CtrctMod.setter
	def CtrctMod(self, value):
		self._CtrctMod = value if type(value) != auto else self.make_default("CtrctMod")

	@CtrctMod.deleter
	def CtrctMod(self):
		del self._CtrctMod
		self._CtrctMod = None

	@property
	def CtrPty(self):
		return self._CtrPty

	@CtrPty.setter
	def CtrPty(self, value):
		self._CtrPty = value if type(value) != auto else self.make_default("CtrPty")

	@CtrPty.deleter
	def CtrPty(self):
		del self._CtrPty
		self._CtrPty = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def FndgSrc(self):
		return self._FndgSrc

	@FndgSrc.setter
	def FndgSrc(self, value):
		self._FndgSrc = value if type(value) != auto else self.make_default("FndgSrc")

	@FndgSrc.deleter
	def FndgSrc(self):
		del self._FndgSrc
		self._FndgSrc = None

	@property
	def RptgDtTm(self):
		return self._RptgDtTm

	@RptgDtTm.setter
	def RptgDtTm(self, value):
		self._RptgDtTm = value if type(value) != auto else self.make_default("RptgDtTm")

	@RptgDtTm.deleter
	def RptgDtTm(self):
		del self._RptgDtTm
		self._RptgDtTm = None

	@property
	def EvtDay(self):
		return self._EvtDay

	@EvtDay.setter
	def EvtDay(self, value):
		self._EvtDay = value if type(value) != auto else self.make_default("EvtDay")

	@EvtDay.deleter
	def EvtDay(self):
		del self._EvtDay
		self._EvtDay = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RcncltnFlg', type=ReconciliationFlag2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TechRcrdId', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollCmpnt', type=CollateralType19, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CtrctMod', type=ContractModification3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPty', type=CounterpartyData87, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FndgSrc', type=FundingSource3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RptgDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtDay', type=ISODate, min=1, max=1, mutex_group=None, array=False),
	))

