import base_types
import ExposureTypeAggregation3
import Transaction124
import OverallCollateralDetails2
import SupplementaryData1
import Pagination1
import TotalValueInPageAndStatement5
import CollateralParties9
import Statement78
import CounterpartyAggregation3

class TripartyCollateralAndExposureReportV01(base_types._BaseFieldType):

	__slots__ = ["_XpsrTpAggtn", "_CollPties", "_Txs", "_AcctBaseCcyTtlAmts", "_SplmtryData", "_CtrPtyAggtn", "_StmtGnlDtls", "_OvrllCollAggtn", "_Pgntn"]
	@property
	def XpsrTpAggtn(self):
		return self._XpsrTpAggtn

	@XpsrTpAggtn.setter
	def XpsrTpAggtn(self, value):
		self._XpsrTpAggtn = value if type(value) != auto else self.make_default("XpsrTpAggtn")

	@XpsrTpAggtn.deleter
	def XpsrTpAggtn(self):
		del self._XpsrTpAggtn
		self._XpsrTpAggtn = None

	@property
	def CollPties(self):
		return self._CollPties

	@CollPties.setter
	def CollPties(self, value):
		self._CollPties = value if type(value) != auto else self.make_default("CollPties")

	@CollPties.deleter
	def CollPties(self):
		del self._CollPties
		self._CollPties = None

	@property
	def Txs(self):
		return self._Txs

	@Txs.setter
	def Txs(self, value):
		self._Txs = value if type(value) != auto else self.make_default("Txs")

	@Txs.deleter
	def Txs(self):
		del self._Txs
		self._Txs = None

	@property
	def AcctBaseCcyTtlAmts(self):
		return self._AcctBaseCcyTtlAmts

	@AcctBaseCcyTtlAmts.setter
	def AcctBaseCcyTtlAmts(self, value):
		self._AcctBaseCcyTtlAmts = value if type(value) != auto else self.make_default("AcctBaseCcyTtlAmts")

	@AcctBaseCcyTtlAmts.deleter
	def AcctBaseCcyTtlAmts(self):
		del self._AcctBaseCcyTtlAmts
		self._AcctBaseCcyTtlAmts = None

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
	def CtrPtyAggtn(self):
		return self._CtrPtyAggtn

	@CtrPtyAggtn.setter
	def CtrPtyAggtn(self, value):
		self._CtrPtyAggtn = value if type(value) != auto else self.make_default("CtrPtyAggtn")

	@CtrPtyAggtn.deleter
	def CtrPtyAggtn(self):
		del self._CtrPtyAggtn
		self._CtrPtyAggtn = None

	@property
	def StmtGnlDtls(self):
		return self._StmtGnlDtls

	@StmtGnlDtls.setter
	def StmtGnlDtls(self, value):
		self._StmtGnlDtls = value if type(value) != auto else self.make_default("StmtGnlDtls")

	@StmtGnlDtls.deleter
	def StmtGnlDtls(self):
		del self._StmtGnlDtls
		self._StmtGnlDtls = None

	@property
	def OvrllCollAggtn(self):
		return self._OvrllCollAggtn

	@OvrllCollAggtn.setter
	def OvrllCollAggtn(self, value):
		self._OvrllCollAggtn = value if type(value) != auto else self.make_default("OvrllCollAggtn")

	@OvrllCollAggtn.deleter
	def OvrllCollAggtn(self):
		del self._OvrllCollAggtn
		self._OvrllCollAggtn = None

	@property
	def Pgntn(self):
		return self._Pgntn

	@Pgntn.setter
	def Pgntn(self, value):
		self._Pgntn = value if type(value) != auto else self.make_default("Pgntn")

	@Pgntn.deleter
	def Pgntn(self):
		del self._Pgntn
		self._Pgntn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='XpsrTpAggtn', type=ExposureTypeAggregation3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CollPties', type=CollateralParties9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Txs', type=Transaction124, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctBaseCcyTtlAmts', type=TotalValueInPageAndStatement5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CtrPtyAggtn', type=CounterpartyAggregation3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StmtGnlDtls', type=Statement78, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OvrllCollAggtn', type=OverallCollateralDetails2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pgntn', type=Pagination1, min=1, max=1, mutex_group=None, array=False),
	))

