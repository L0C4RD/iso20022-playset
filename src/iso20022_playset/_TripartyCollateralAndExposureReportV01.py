# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CollateralParties9
from . import CounterpartyAggregation3
from . import ExposureTypeAggregation3
from . import OverallCollateralDetails2
from . import Pagination1
from . import Statement78
from . import SupplementaryData1
from . import TotalValueInPageAndStatement5
from . import Transaction124

class TripartyCollateralAndExposureReportV01(base_types._BaseFieldType):

	__slots__ = ["_AcctBaseCcyTtlAmts", "_CollPties", "_CtrPtyAggtn", "_OvrllCollAggtn", "_Pgntn", "_SplmtryData", "_StmtGnlDtls", "_Txs", "_XpsrTpAggtn"]
	@property
	def AcctBaseCcyTtlAmts(self):
		return self._AcctBaseCcyTtlAmts

	@AcctBaseCcyTtlAmts.setter
	def AcctBaseCcyTtlAmts(self, value):
		self._AcctBaseCcyTtlAmts = value if value is not None else base_types.UninitialisedField(self, 'AcctBaseCcyTtlAmts', TotalValueInPageAndStatement5, False)

	@AcctBaseCcyTtlAmts.deleter
	def AcctBaseCcyTtlAmts(self):
		del self._AcctBaseCcyTtlAmts
		self._AcctBaseCcyTtlAmts = base_types.UninitialisedField(self, 'AcctBaseCcyTtlAmts', TotalValueInPageAndStatement5, False)

	@property
	def CollPties(self):
		return self._CollPties

	@CollPties.setter
	def CollPties(self, value):
		self._CollPties = value if value is not None else base_types.UninitialisedField(self, 'CollPties', CollateralParties9, False)

	@CollPties.deleter
	def CollPties(self):
		del self._CollPties
		self._CollPties = base_types.UninitialisedField(self, 'CollPties', CollateralParties9, False)

	@property
	def CtrPtyAggtn(self):
		return self._CtrPtyAggtn

	@CtrPtyAggtn.setter
	def CtrPtyAggtn(self, value):
		self._CtrPtyAggtn = value if value is not None else base_types.UninitialisedField(self, 'CtrPtyAggtn', CounterpartyAggregation3, True)

	@CtrPtyAggtn.deleter
	def CtrPtyAggtn(self):
		del self._CtrPtyAggtn
		self._CtrPtyAggtn = base_types.UninitialisedField(self, 'CtrPtyAggtn', CounterpartyAggregation3, True)

	@property
	def OvrllCollAggtn(self):
		return self._OvrllCollAggtn

	@OvrllCollAggtn.setter
	def OvrllCollAggtn(self, value):
		self._OvrllCollAggtn = value if value is not None else base_types.UninitialisedField(self, 'OvrllCollAggtn', OverallCollateralDetails2, False)

	@OvrllCollAggtn.deleter
	def OvrllCollAggtn(self):
		del self._OvrllCollAggtn
		self._OvrllCollAggtn = base_types.UninitialisedField(self, 'OvrllCollAggtn', OverallCollateralDetails2, False)

	@property
	def Pgntn(self):
		return self._Pgntn

	@Pgntn.setter
	def Pgntn(self, value):
		self._Pgntn = value if value is not None else base_types.UninitialisedField(self, 'Pgntn', Pagination1, False)

	@Pgntn.deleter
	def Pgntn(self):
		del self._Pgntn
		self._Pgntn = base_types.UninitialisedField(self, 'Pgntn', Pagination1, False)

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
	def StmtGnlDtls(self):
		return self._StmtGnlDtls

	@StmtGnlDtls.setter
	def StmtGnlDtls(self, value):
		self._StmtGnlDtls = value if value is not None else base_types.UninitialisedField(self, 'StmtGnlDtls', Statement78, False)

	@StmtGnlDtls.deleter
	def StmtGnlDtls(self):
		del self._StmtGnlDtls
		self._StmtGnlDtls = base_types.UninitialisedField(self, 'StmtGnlDtls', Statement78, False)

	@property
	def Txs(self):
		return self._Txs

	@Txs.setter
	def Txs(self, value):
		self._Txs = value if value is not None else base_types.UninitialisedField(self, 'Txs', Transaction124, True)

	@Txs.deleter
	def Txs(self):
		del self._Txs
		self._Txs = base_types.UninitialisedField(self, 'Txs', Transaction124, True)

	@property
	def XpsrTpAggtn(self):
		return self._XpsrTpAggtn

	@XpsrTpAggtn.setter
	def XpsrTpAggtn(self, value):
		self._XpsrTpAggtn = value if value is not None else base_types.UninitialisedField(self, 'XpsrTpAggtn', ExposureTypeAggregation3, True)

	@XpsrTpAggtn.deleter
	def XpsrTpAggtn(self):
		del self._XpsrTpAggtn
		self._XpsrTpAggtn = base_types.UninitialisedField(self, 'XpsrTpAggtn', ExposureTypeAggregation3, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctBaseCcyTtlAmts', type=TotalValueInPageAndStatement5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollPties', type=CollateralParties9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtyAggtn', type=CounterpartyAggregation3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OvrllCollAggtn', type=OverallCollateralDetails2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pgntn', type=Pagination1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StmtGnlDtls', type=Statement78, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Txs', type=Transaction124, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='XpsrTpAggtn', type=ExposureTypeAggregation3, min=0, max=None, mutex_group=None, array=True),
	))