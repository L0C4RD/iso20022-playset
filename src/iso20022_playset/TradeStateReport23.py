import base_types
import CommonTradeDataReport72
import TechnicalAttributes5
import SupplementaryData1
import DisseminationData1
import CounterpartySpecificData36

class TradeStateReport23(base_types._BaseFieldType):

	__slots__ = ["_CmonTradData", "_SplmtryData", "_PblcDssmntnData", "_TechAttrbts", "_CtrPtySpcfcData"]
	@property
	def CmonTradData(self):
		return self._CmonTradData

	@CmonTradData.setter
	def CmonTradData(self, value):
		self._CmonTradData = value if type(value) != auto else self.make_default("CmonTradData")

	@CmonTradData.deleter
	def CmonTradData(self):
		del self._CmonTradData
		self._CmonTradData = None

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
	def PblcDssmntnData(self):
		return self._PblcDssmntnData

	@PblcDssmntnData.setter
	def PblcDssmntnData(self, value):
		self._PblcDssmntnData = value if type(value) != auto else self.make_default("PblcDssmntnData")

	@PblcDssmntnData.deleter
	def PblcDssmntnData(self):
		del self._PblcDssmntnData
		self._PblcDssmntnData = None

	@property
	def TechAttrbts(self):
		return self._TechAttrbts

	@TechAttrbts.setter
	def TechAttrbts(self, value):
		self._TechAttrbts = value if type(value) != auto else self.make_default("TechAttrbts")

	@TechAttrbts.deleter
	def TechAttrbts(self):
		del self._TechAttrbts
		self._TechAttrbts = None

	@property
	def CtrPtySpcfcData(self):
		return self._CtrPtySpcfcData

	@CtrPtySpcfcData.setter
	def CtrPtySpcfcData(self, value):
		self._CtrPtySpcfcData = value if type(value) != auto else self.make_default("CtrPtySpcfcData")

	@CtrPtySpcfcData.deleter
	def CtrPtySpcfcData(self):
		del self._CtrPtySpcfcData
		self._CtrPtySpcfcData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CmonTradData', type=CommonTradeDataReport72, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PblcDssmntnData', type=DisseminationData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TechAttrbts', type=TechnicalAttributes5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtySpcfcData', type=CounterpartySpecificData36, min=1, max=2, mutex_group=None, array=False),
	))

