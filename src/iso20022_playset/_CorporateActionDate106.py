# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BorrowerLendingDeadline5
from . import DateFormat43Choice
from . import DateFormat44Choice

class CorporateActionDate106(base_types._BaseFieldType):

	__slots__ = ["_BrrwrStockLndgDdln", "_CoverXprtnDdln", "_DcmnttnDdln", "_DpstryCoverXprtnDt", "_EarlyRspnDdln", "_MktDdln", "_PrtctDdln", "_RspnDdln", "_SbcptCostDbtDt", "_StockLndgDdln", "_XpryDt"]
	@property
	def BrrwrStockLndgDdln(self):
		return self._BrrwrStockLndgDdln

	@BrrwrStockLndgDdln.setter
	def BrrwrStockLndgDdln(self, value):
		self._BrrwrStockLndgDdln = value if value is not None else base_types.UninitialisedField(self, 'BrrwrStockLndgDdln', BorrowerLendingDeadline5, True)

	@BrrwrStockLndgDdln.deleter
	def BrrwrStockLndgDdln(self):
		del self._BrrwrStockLndgDdln
		self._BrrwrStockLndgDdln = base_types.UninitialisedField(self, 'BrrwrStockLndgDdln', BorrowerLendingDeadline5, True)

	@property
	def CoverXprtnDdln(self):
		return self._CoverXprtnDdln

	@CoverXprtnDdln.setter
	def CoverXprtnDdln(self, value):
		self._CoverXprtnDdln = value if value is not None else base_types.UninitialisedField(self, 'CoverXprtnDdln', DateFormat43Choice, False)

	@CoverXprtnDdln.deleter
	def CoverXprtnDdln(self):
		del self._CoverXprtnDdln
		self._CoverXprtnDdln = base_types.UninitialisedField(self, 'CoverXprtnDdln', DateFormat43Choice, False)

	@property
	def DcmnttnDdln(self):
		return self._DcmnttnDdln

	@DcmnttnDdln.setter
	def DcmnttnDdln(self, value):
		self._DcmnttnDdln = value if value is not None else base_types.UninitialisedField(self, 'DcmnttnDdln', DateFormat43Choice, False)

	@DcmnttnDdln.deleter
	def DcmnttnDdln(self):
		del self._DcmnttnDdln
		self._DcmnttnDdln = base_types.UninitialisedField(self, 'DcmnttnDdln', DateFormat43Choice, False)

	@property
	def DpstryCoverXprtnDt(self):
		return self._DpstryCoverXprtnDt

	@DpstryCoverXprtnDt.setter
	def DpstryCoverXprtnDt(self, value):
		self._DpstryCoverXprtnDt = value if value is not None else base_types.UninitialisedField(self, 'DpstryCoverXprtnDt', DateFormat43Choice, False)

	@DpstryCoverXprtnDt.deleter
	def DpstryCoverXprtnDt(self):
		del self._DpstryCoverXprtnDt
		self._DpstryCoverXprtnDt = base_types.UninitialisedField(self, 'DpstryCoverXprtnDt', DateFormat43Choice, False)

	@property
	def EarlyRspnDdln(self):
		return self._EarlyRspnDdln

	@EarlyRspnDdln.setter
	def EarlyRspnDdln(self, value):
		self._EarlyRspnDdln = value if value is not None else base_types.UninitialisedField(self, 'EarlyRspnDdln', DateFormat43Choice, False)

	@EarlyRspnDdln.deleter
	def EarlyRspnDdln(self):
		del self._EarlyRspnDdln
		self._EarlyRspnDdln = base_types.UninitialisedField(self, 'EarlyRspnDdln', DateFormat43Choice, False)

	@property
	def MktDdln(self):
		return self._MktDdln

	@MktDdln.setter
	def MktDdln(self, value):
		self._MktDdln = value if value is not None else base_types.UninitialisedField(self, 'MktDdln', DateFormat43Choice, False)

	@MktDdln.deleter
	def MktDdln(self):
		del self._MktDdln
		self._MktDdln = base_types.UninitialisedField(self, 'MktDdln', DateFormat43Choice, False)

	@property
	def PrtctDdln(self):
		return self._PrtctDdln

	@PrtctDdln.setter
	def PrtctDdln(self, value):
		self._PrtctDdln = value if value is not None else base_types.UninitialisedField(self, 'PrtctDdln', DateFormat43Choice, False)

	@PrtctDdln.deleter
	def PrtctDdln(self):
		del self._PrtctDdln
		self._PrtctDdln = base_types.UninitialisedField(self, 'PrtctDdln', DateFormat43Choice, False)

	@property
	def RspnDdln(self):
		return self._RspnDdln

	@RspnDdln.setter
	def RspnDdln(self, value):
		self._RspnDdln = value if value is not None else base_types.UninitialisedField(self, 'RspnDdln', DateFormat44Choice, False)

	@RspnDdln.deleter
	def RspnDdln(self):
		del self._RspnDdln
		self._RspnDdln = base_types.UninitialisedField(self, 'RspnDdln', DateFormat44Choice, False)

	@property
	def SbcptCostDbtDt(self):
		return self._SbcptCostDbtDt

	@SbcptCostDbtDt.setter
	def SbcptCostDbtDt(self, value):
		self._SbcptCostDbtDt = value if value is not None else base_types.UninitialisedField(self, 'SbcptCostDbtDt', DateFormat43Choice, False)

	@SbcptCostDbtDt.deleter
	def SbcptCostDbtDt(self):
		del self._SbcptCostDbtDt
		self._SbcptCostDbtDt = base_types.UninitialisedField(self, 'SbcptCostDbtDt', DateFormat43Choice, False)

	@property
	def StockLndgDdln(self):
		return self._StockLndgDdln

	@StockLndgDdln.setter
	def StockLndgDdln(self, value):
		self._StockLndgDdln = value if value is not None else base_types.UninitialisedField(self, 'StockLndgDdln', DateFormat43Choice, False)

	@StockLndgDdln.deleter
	def StockLndgDdln(self):
		del self._StockLndgDdln
		self._StockLndgDdln = base_types.UninitialisedField(self, 'StockLndgDdln', DateFormat43Choice, False)

	@property
	def XpryDt(self):
		return self._XpryDt

	@XpryDt.setter
	def XpryDt(self, value):
		self._XpryDt = value if value is not None else base_types.UninitialisedField(self, 'XpryDt', DateFormat43Choice, False)

	@XpryDt.deleter
	def XpryDt(self):
		del self._XpryDt
		self._XpryDt = base_types.UninitialisedField(self, 'XpryDt', DateFormat43Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BrrwrStockLndgDdln', type=BorrowerLendingDeadline5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CoverXprtnDdln', type=DateFormat43Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DcmnttnDdln', type=DateFormat43Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DpstryCoverXprtnDt', type=DateFormat43Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EarlyRspnDdln', type=DateFormat43Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktDdln', type=DateFormat43Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctDdln', type=DateFormat43Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnDdln', type=DateFormat44Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SbcptCostDbtDt', type=DateFormat43Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StockLndgDdln', type=DateFormat43Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpryDt', type=DateFormat43Choice, min=0, max=1, mutex_group=None, array=False),
	))