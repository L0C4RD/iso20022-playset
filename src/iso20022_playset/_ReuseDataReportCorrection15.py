# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CollateralType19
from . import ContractModification3
from . import CounterpartyData87
from . import FundingSource3
from . import ISODate
from . import ISODateTime
from . import Max140Text
from . import ReconciliationFlag2
from . import SupplementaryData1

class ReuseDataReportCorrection15(base_types._BaseFieldType):

	__slots__ = ["_CollCmpnt", "_CtrPty", "_CtrctMod", "_EvtDay", "_FndgSrc", "_RcncltnFlg", "_RptgDtTm", "_SplmtryData", "_TechRcrdId"]
	@property
	def CollCmpnt(self):
		return self._CollCmpnt

	@CollCmpnt.setter
	def CollCmpnt(self, value):
		self._CollCmpnt = value if value is not None else base_types.UninitialisedField(self, 'CollCmpnt', CollateralType19, True)

	@CollCmpnt.deleter
	def CollCmpnt(self):
		del self._CollCmpnt
		self._CollCmpnt = base_types.UninitialisedField(self, 'CollCmpnt', CollateralType19, True)

	@property
	def CtrPty(self):
		return self._CtrPty

	@CtrPty.setter
	def CtrPty(self, value):
		self._CtrPty = value if value is not None else base_types.UninitialisedField(self, 'CtrPty', CounterpartyData87, False)

	@CtrPty.deleter
	def CtrPty(self):
		del self._CtrPty
		self._CtrPty = base_types.UninitialisedField(self, 'CtrPty', CounterpartyData87, False)

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
	def EvtDay(self):
		return self._EvtDay

	@EvtDay.setter
	def EvtDay(self, value):
		self._EvtDay = value if value is not None else base_types.UninitialisedField(self, 'EvtDay', ISODate, False)

	@EvtDay.deleter
	def EvtDay(self):
		del self._EvtDay
		self._EvtDay = base_types.UninitialisedField(self, 'EvtDay', ISODate, False)

	@property
	def FndgSrc(self):
		return self._FndgSrc

	@FndgSrc.setter
	def FndgSrc(self, value):
		self._FndgSrc = value if value is not None else base_types.UninitialisedField(self, 'FndgSrc', FundingSource3, True)

	@FndgSrc.deleter
	def FndgSrc(self):
		del self._FndgSrc
		self._FndgSrc = base_types.UninitialisedField(self, 'FndgSrc', FundingSource3, True)

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
		base_types.FieldEntry(name='CollCmpnt', type=CollateralType19, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CtrPty', type=CounterpartyData87, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctMod', type=ContractModification3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtDay', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FndgSrc', type=FundingSource3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RcncltnFlg', type=ReconciliationFlag2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TechRcrdId', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
	))