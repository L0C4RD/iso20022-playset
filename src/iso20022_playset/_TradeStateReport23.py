# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CommonTradeDataReport72
from . import CounterpartySpecificData36
from . import DisseminationData1
from . import SupplementaryData1
from . import TechnicalAttributes5

class TradeStateReport23(base_types._BaseFieldType):

	__slots__ = ["_CmonTradData", "_CtrPtySpcfcData", "_PblcDssmntnData", "_SplmtryData", "_TechAttrbts"]
	@property
	def CmonTradData(self):
		return self._CmonTradData

	@CmonTradData.setter
	def CmonTradData(self, value):
		self._CmonTradData = value if value is not None else base_types.UninitialisedField(self, 'CmonTradData', CommonTradeDataReport72, False)

	@CmonTradData.deleter
	def CmonTradData(self):
		del self._CmonTradData
		self._CmonTradData = base_types.UninitialisedField(self, 'CmonTradData', CommonTradeDataReport72, False)

	@property
	def CtrPtySpcfcData(self):
		return self._CtrPtySpcfcData

	@CtrPtySpcfcData.setter
	def CtrPtySpcfcData(self, value):
		self._CtrPtySpcfcData = value if value is not None else base_types.UninitialisedField(self, 'CtrPtySpcfcData', CounterpartySpecificData36, False)

	@CtrPtySpcfcData.deleter
	def CtrPtySpcfcData(self):
		del self._CtrPtySpcfcData
		self._CtrPtySpcfcData = base_types.UninitialisedField(self, 'CtrPtySpcfcData', CounterpartySpecificData36, False)

	@property
	def PblcDssmntnData(self):
		return self._PblcDssmntnData

	@PblcDssmntnData.setter
	def PblcDssmntnData(self, value):
		self._PblcDssmntnData = value if value is not None else base_types.UninitialisedField(self, 'PblcDssmntnData', DisseminationData1, False)

	@PblcDssmntnData.deleter
	def PblcDssmntnData(self):
		del self._PblcDssmntnData
		self._PblcDssmntnData = base_types.UninitialisedField(self, 'PblcDssmntnData', DisseminationData1, False)

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
	def TechAttrbts(self):
		return self._TechAttrbts

	@TechAttrbts.setter
	def TechAttrbts(self, value):
		self._TechAttrbts = value if value is not None else base_types.UninitialisedField(self, 'TechAttrbts', TechnicalAttributes5, False)

	@TechAttrbts.deleter
	def TechAttrbts(self):
		del self._TechAttrbts
		self._TechAttrbts = base_types.UninitialisedField(self, 'TechAttrbts', TechnicalAttributes5, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CmonTradData', type=CommonTradeDataReport72, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtySpcfcData', type=CounterpartySpecificData36, min=1, max=2, mutex_group=None, array=False),
		base_types.FieldEntry(name='PblcDssmntnData', type=DisseminationData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TechAttrbts', type=TechnicalAttributes5, min=0, max=1, mutex_group=None, array=False),
	))