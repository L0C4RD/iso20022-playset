# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ContractModification3
from . import Counterparty39
from . import ISODate
from . import ISODateTime
from . import Max140Text
from . import Max52Text
from . import PostedMarginOrCollateral4
from . import ReceivedMarginOrCollateral4
from . import ReconciliationFlag2
from . import SupplementaryData1

class CollateralMarginNew10(base_types._BaseFieldType):

	__slots__ = ["_CollPrtflId", "_CtrPty", "_CtrctMod", "_EvtDt", "_PstdMrgnOrColl", "_RcncltnFlg", "_RcvdMrgnOrColl", "_RptgDtTm", "_SplmtryData", "_TechRcrdId"]
	@property
	def CollPrtflId(self):
		return self._CollPrtflId

	@CollPrtflId.setter
	def CollPrtflId(self, value):
		self._CollPrtflId = value if value is not None else base_types.UninitialisedField(self, 'CollPrtflId', Max52Text, False)

	@CollPrtflId.deleter
	def CollPrtflId(self):
		del self._CollPrtflId
		self._CollPrtflId = base_types.UninitialisedField(self, 'CollPrtflId', Max52Text, False)

	@property
	def CtrPty(self):
		return self._CtrPty

	@CtrPty.setter
	def CtrPty(self, value):
		self._CtrPty = value if value is not None else base_types.UninitialisedField(self, 'CtrPty', Counterparty39, False)

	@CtrPty.deleter
	def CtrPty(self):
		del self._CtrPty
		self._CtrPty = base_types.UninitialisedField(self, 'CtrPty', Counterparty39, False)

	@property
	def CtrctMod(self):
		return self._CtrctMod

	@CtrctMod.setter
	def CtrctMod(self, value):
		self._CtrctMod = value if value is not None else base_types.UninitialisedField(self, 'CtrctMod', ContractModification3, False)

	@CtrctMod.deleter
	def CtrctMod(self):
		del self._CtrctMod
		self._CtrctMod = base_types.UninitialisedField(self, 'CtrctMod', ContractModification3, False)

	@property
	def EvtDt(self):
		return self._EvtDt

	@EvtDt.setter
	def EvtDt(self, value):
		self._EvtDt = value if value is not None else base_types.UninitialisedField(self, 'EvtDt', ISODate, False)

	@EvtDt.deleter
	def EvtDt(self):
		del self._EvtDt
		self._EvtDt = base_types.UninitialisedField(self, 'EvtDt', ISODate, False)

	@property
	def PstdMrgnOrColl(self):
		return self._PstdMrgnOrColl

	@PstdMrgnOrColl.setter
	def PstdMrgnOrColl(self, value):
		self._PstdMrgnOrColl = value if value is not None else base_types.UninitialisedField(self, 'PstdMrgnOrColl', PostedMarginOrCollateral4, False)

	@PstdMrgnOrColl.deleter
	def PstdMrgnOrColl(self):
		del self._PstdMrgnOrColl
		self._PstdMrgnOrColl = base_types.UninitialisedField(self, 'PstdMrgnOrColl', PostedMarginOrCollateral4, False)

	@property
	def RcncltnFlg(self):
		return self._RcncltnFlg

	@RcncltnFlg.setter
	def RcncltnFlg(self, value):
		self._RcncltnFlg = value if value is not None else base_types.UninitialisedField(self, 'RcncltnFlg', ReconciliationFlag2, False)

	@RcncltnFlg.deleter
	def RcncltnFlg(self):
		del self._RcncltnFlg
		self._RcncltnFlg = base_types.UninitialisedField(self, 'RcncltnFlg', ReconciliationFlag2, False)

	@property
	def RcvdMrgnOrColl(self):
		return self._RcvdMrgnOrColl

	@RcvdMrgnOrColl.setter
	def RcvdMrgnOrColl(self, value):
		self._RcvdMrgnOrColl = value if value is not None else base_types.UninitialisedField(self, 'RcvdMrgnOrColl', ReceivedMarginOrCollateral4, False)

	@RcvdMrgnOrColl.deleter
	def RcvdMrgnOrColl(self):
		del self._RcvdMrgnOrColl
		self._RcvdMrgnOrColl = base_types.UninitialisedField(self, 'RcvdMrgnOrColl', ReceivedMarginOrCollateral4, False)

	@property
	def RptgDtTm(self):
		return self._RptgDtTm

	@RptgDtTm.setter
	def RptgDtTm(self, value):
		self._RptgDtTm = value if value is not None else base_types.UninitialisedField(self, 'RptgDtTm', ISODateTime, False)

	@RptgDtTm.deleter
	def RptgDtTm(self):
		del self._RptgDtTm
		self._RptgDtTm = base_types.UninitialisedField(self, 'RptgDtTm', ISODateTime, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@property
	def TechRcrdId(self):
		return self._TechRcrdId

	@TechRcrdId.setter
	def TechRcrdId(self, value):
		self._TechRcrdId = value if value is not None else base_types.UninitialisedField(self, 'TechRcrdId', Max140Text, False)

	@TechRcrdId.deleter
	def TechRcrdId(self):
		del self._TechRcrdId
		self._TechRcrdId = base_types.UninitialisedField(self, 'TechRcrdId', Max140Text, False)

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