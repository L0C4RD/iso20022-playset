from . import base_types
from ._ContractModification3 import ContractModification3
from ._Counterparty39 import Counterparty39
from ._ISODate import ISODate
from ._ISODateTime import ISODateTime
from ._Max140Text import Max140Text
from ._Max52Text import Max52Text
from ._PostedMarginOrCollateral4 import PostedMarginOrCollateral4
from ._ReceivedMarginOrCollateral4 import ReceivedMarginOrCollateral4
from ._ReconciliationFlag2 import ReconciliationFlag2
from ._SupplementaryData1 import SupplementaryData1

class CollateralMarginNew10(base_types._BaseFieldType):

	__slots__ = ["_CollPrtflId", "_CtrPty", "_CtrctMod", "_EvtDt", "_PstdMrgnOrColl", "_RcncltnFlg", "_RcvdMrgnOrColl", "_RptgDtTm", "_SplmtryData", "_TechRcrdId"]
	@property
	def CollPrtflId(self):
		return self._CollPrtflId

	@CollPrtflId.setter
	def CollPrtflId(self, value):
		self._CollPrtflId = value if type(value) != base_types.auto else self.make_default("CollPrtflId")

	@CollPrtflId.deleter
	def CollPrtflId(self):
		del self._CollPrtflId
		self._CollPrtflId = None

	@property
	def CtrPty(self):
		return self._CtrPty

	@CtrPty.setter
	def CtrPty(self, value):
		self._CtrPty = value if type(value) != base_types.auto else self.make_default("CtrPty")

	@CtrPty.deleter
	def CtrPty(self):
		del self._CtrPty
		self._CtrPty = None

	@property
	def CtrctMod(self):
		return self._CtrctMod

	@CtrctMod.setter
	def CtrctMod(self, value):
		self._CtrctMod = value if type(value) != base_types.auto else self.make_default("CtrctMod")

	@CtrctMod.deleter
	def CtrctMod(self):
		del self._CtrctMod
		self._CtrctMod = None

	@property
	def EvtDt(self):
		return self._EvtDt

	@EvtDt.setter
	def EvtDt(self, value):
		self._EvtDt = value if type(value) != base_types.auto else self.make_default("EvtDt")

	@EvtDt.deleter
	def EvtDt(self):
		del self._EvtDt
		self._EvtDt = None

	@property
	def PstdMrgnOrColl(self):
		return self._PstdMrgnOrColl

	@PstdMrgnOrColl.setter
	def PstdMrgnOrColl(self, value):
		self._PstdMrgnOrColl = value if type(value) != base_types.auto else self.make_default("PstdMrgnOrColl")

	@PstdMrgnOrColl.deleter
	def PstdMrgnOrColl(self):
		del self._PstdMrgnOrColl
		self._PstdMrgnOrColl = None

	@property
	def RcncltnFlg(self):
		return self._RcncltnFlg

	@RcncltnFlg.setter
	def RcncltnFlg(self, value):
		self._RcncltnFlg = value if type(value) != base_types.auto else self.make_default("RcncltnFlg")

	@RcncltnFlg.deleter
	def RcncltnFlg(self):
		del self._RcncltnFlg
		self._RcncltnFlg = None

	@property
	def RcvdMrgnOrColl(self):
		return self._RcvdMrgnOrColl

	@RcvdMrgnOrColl.setter
	def RcvdMrgnOrColl(self, value):
		self._RcvdMrgnOrColl = value if type(value) != base_types.auto else self.make_default("RcvdMrgnOrColl")

	@RcvdMrgnOrColl.deleter
	def RcvdMrgnOrColl(self):
		del self._RcvdMrgnOrColl
		self._RcvdMrgnOrColl = None

	@property
	def RptgDtTm(self):
		return self._RptgDtTm

	@RptgDtTm.setter
	def RptgDtTm(self, value):
		self._RptgDtTm = value if type(value) != base_types.auto else self.make_default("RptgDtTm")

	@RptgDtTm.deleter
	def RptgDtTm(self):
		del self._RptgDtTm
		self._RptgDtTm = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def TechRcrdId(self):
		return self._TechRcrdId

	@TechRcrdId.setter
	def TechRcrdId(self, value):
		self._TechRcrdId = value if type(value) != base_types.auto else self.make_default("TechRcrdId")

	@TechRcrdId.deleter
	def TechRcrdId(self):
		del self._TechRcrdId
		self._TechRcrdId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollPrtflId', type=Max52Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPty', type=Counterparty39, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctMod', type=ContractModification3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstdMrgnOrColl', type=PostedMarginOrCollateral4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnFlg', type=ReconciliationFlag2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcvdMrgnOrColl', type=ReceivedMarginOrCollateral4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TechRcrdId', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
	))

