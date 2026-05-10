import base_types
import BorrowerLendingDeadline6
import DateFormat54Choice
import DateFormat49Choice

class CorporateActionDate107(base_types._BaseFieldType):

	__slots__ = ["_PrtctDdln", "_BrrwrStockLndgDdln", "_XpryDt", "_StockLndgDdln", "_SbcptCostDbtDt", "_CoverXprtnDdln", "_RspnDdln", "_DcmnttnDdln", "_EarlyRspnDdln", "_MktDdln", "_DpstryCoverXprtnDt"]
	@property
	def PrtctDdln(self):
		return self._PrtctDdln

	@PrtctDdln.setter
	def PrtctDdln(self, value):
		self._PrtctDdln = value if type(value) != auto else self.make_default("PrtctDdln")

	@PrtctDdln.deleter
	def PrtctDdln(self):
		del self._PrtctDdln
		self._PrtctDdln = None

	@property
	def BrrwrStockLndgDdln(self):
		return self._BrrwrStockLndgDdln

	@BrrwrStockLndgDdln.setter
	def BrrwrStockLndgDdln(self, value):
		self._BrrwrStockLndgDdln = value if type(value) != auto else self.make_default("BrrwrStockLndgDdln")

	@BrrwrStockLndgDdln.deleter
	def BrrwrStockLndgDdln(self):
		del self._BrrwrStockLndgDdln
		self._BrrwrStockLndgDdln = None

	@property
	def XpryDt(self):
		return self._XpryDt

	@XpryDt.setter
	def XpryDt(self, value):
		self._XpryDt = value if type(value) != auto else self.make_default("XpryDt")

	@XpryDt.deleter
	def XpryDt(self):
		del self._XpryDt
		self._XpryDt = None

	@property
	def StockLndgDdln(self):
		return self._StockLndgDdln

	@StockLndgDdln.setter
	def StockLndgDdln(self, value):
		self._StockLndgDdln = value if type(value) != auto else self.make_default("StockLndgDdln")

	@StockLndgDdln.deleter
	def StockLndgDdln(self):
		del self._StockLndgDdln
		self._StockLndgDdln = None

	@property
	def SbcptCostDbtDt(self):
		return self._SbcptCostDbtDt

	@SbcptCostDbtDt.setter
	def SbcptCostDbtDt(self, value):
		self._SbcptCostDbtDt = value if type(value) != auto else self.make_default("SbcptCostDbtDt")

	@SbcptCostDbtDt.deleter
	def SbcptCostDbtDt(self):
		del self._SbcptCostDbtDt
		self._SbcptCostDbtDt = None

	@property
	def CoverXprtnDdln(self):
		return self._CoverXprtnDdln

	@CoverXprtnDdln.setter
	def CoverXprtnDdln(self, value):
		self._CoverXprtnDdln = value if type(value) != auto else self.make_default("CoverXprtnDdln")

	@CoverXprtnDdln.deleter
	def CoverXprtnDdln(self):
		del self._CoverXprtnDdln
		self._CoverXprtnDdln = None

	@property
	def RspnDdln(self):
		return self._RspnDdln

	@RspnDdln.setter
	def RspnDdln(self, value):
		self._RspnDdln = value if type(value) != auto else self.make_default("RspnDdln")

	@RspnDdln.deleter
	def RspnDdln(self):
		del self._RspnDdln
		self._RspnDdln = None

	@property
	def DcmnttnDdln(self):
		return self._DcmnttnDdln

	@DcmnttnDdln.setter
	def DcmnttnDdln(self, value):
		self._DcmnttnDdln = value if type(value) != auto else self.make_default("DcmnttnDdln")

	@DcmnttnDdln.deleter
	def DcmnttnDdln(self):
		del self._DcmnttnDdln
		self._DcmnttnDdln = None

	@property
	def EarlyRspnDdln(self):
		return self._EarlyRspnDdln

	@EarlyRspnDdln.setter
	def EarlyRspnDdln(self, value):
		self._EarlyRspnDdln = value if type(value) != auto else self.make_default("EarlyRspnDdln")

	@EarlyRspnDdln.deleter
	def EarlyRspnDdln(self):
		del self._EarlyRspnDdln
		self._EarlyRspnDdln = None

	@property
	def MktDdln(self):
		return self._MktDdln

	@MktDdln.setter
	def MktDdln(self, value):
		self._MktDdln = value if type(value) != auto else self.make_default("MktDdln")

	@MktDdln.deleter
	def MktDdln(self):
		del self._MktDdln
		self._MktDdln = None

	@property
	def DpstryCoverXprtnDt(self):
		return self._DpstryCoverXprtnDt

	@DpstryCoverXprtnDt.setter
	def DpstryCoverXprtnDt(self, value):
		self._DpstryCoverXprtnDt = value if type(value) != auto else self.make_default("DpstryCoverXprtnDt")

	@DpstryCoverXprtnDt.deleter
	def DpstryCoverXprtnDt(self):
		del self._DpstryCoverXprtnDt
		self._DpstryCoverXprtnDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrtctDdln', type=DateFormat49Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BrrwrStockLndgDdln', type=BorrowerLendingDeadline6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='XpryDt', type=DateFormat49Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StockLndgDdln', type=DateFormat49Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SbcptCostDbtDt', type=DateFormat49Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CoverXprtnDdln', type=DateFormat49Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnDdln', type=DateFormat54Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DcmnttnDdln', type=DateFormat49Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EarlyRspnDdln', type=DateFormat49Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktDdln', type=DateFormat49Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DpstryCoverXprtnDt', type=DateFormat49Choice, min=0, max=1, mutex_group=None, array=False),
	))

