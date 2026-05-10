from . import base_types
from ._FinancialInstrumentQuantity25Choice import FinancialInstrumentQuantity25Choice
from ._MinimumExecutable1 import MinimumExecutable1
from ._TrueFalseIndicator import TrueFalseIndicator
from ._Side6Code import Side6Code
from ._OrderStatus11Code import OrderStatus11Code
from ._Max50Text import Max50Text
from ._OrderStatus10Code import OrderStatus10Code

class OrderInstructionData2(base_types._BaseFieldType):

	__slots__ = ["_RmngQty", "_RtgStrtgy", "_InitlQty", "_OrdrSts", "_BuySellInd", "_PssvOnlyInd", "_DispdQty", "_MinAccptblQty", "_OrdrVldtySts", "_SlfExctnPrvntn", "_MinExctbl"]
	@property
	def RmngQty(self):
		return self._RmngQty

	@RmngQty.setter
	def RmngQty(self, value):
		self._RmngQty = value if type(value) != base_types.auto else self.make_default("RmngQty")

	@RmngQty.deleter
	def RmngQty(self):
		del self._RmngQty
		self._RmngQty = None

	@property
	def RtgStrtgy(self):
		return self._RtgStrtgy

	@RtgStrtgy.setter
	def RtgStrtgy(self, value):
		self._RtgStrtgy = value if type(value) != base_types.auto else self.make_default("RtgStrtgy")

	@RtgStrtgy.deleter
	def RtgStrtgy(self):
		del self._RtgStrtgy
		self._RtgStrtgy = None

	@property
	def InitlQty(self):
		return self._InitlQty

	@InitlQty.setter
	def InitlQty(self, value):
		self._InitlQty = value if type(value) != base_types.auto else self.make_default("InitlQty")

	@InitlQty.deleter
	def InitlQty(self):
		del self._InitlQty
		self._InitlQty = None

	@property
	def OrdrSts(self):
		return self._OrdrSts

	@OrdrSts.setter
	def OrdrSts(self, value):
		self._OrdrSts = value if type(value) != base_types.auto else self.make_default("OrdrSts")

	@OrdrSts.deleter
	def OrdrSts(self):
		del self._OrdrSts
		self._OrdrSts = None

	@property
	def BuySellInd(self):
		return self._BuySellInd

	@BuySellInd.setter
	def BuySellInd(self, value):
		self._BuySellInd = value if type(value) != base_types.auto else self.make_default("BuySellInd")

	@BuySellInd.deleter
	def BuySellInd(self):
		del self._BuySellInd
		self._BuySellInd = None

	@property
	def PssvOnlyInd(self):
		return self._PssvOnlyInd

	@PssvOnlyInd.setter
	def PssvOnlyInd(self, value):
		self._PssvOnlyInd = value if type(value) != base_types.auto else self.make_default("PssvOnlyInd")

	@PssvOnlyInd.deleter
	def PssvOnlyInd(self):
		del self._PssvOnlyInd
		self._PssvOnlyInd = None

	@property
	def DispdQty(self):
		return self._DispdQty

	@DispdQty.setter
	def DispdQty(self, value):
		self._DispdQty = value if type(value) != base_types.auto else self.make_default("DispdQty")

	@DispdQty.deleter
	def DispdQty(self):
		del self._DispdQty
		self._DispdQty = None

	@property
	def MinAccptblQty(self):
		return self._MinAccptblQty

	@MinAccptblQty.setter
	def MinAccptblQty(self, value):
		self._MinAccptblQty = value if type(value) != base_types.auto else self.make_default("MinAccptblQty")

	@MinAccptblQty.deleter
	def MinAccptblQty(self):
		del self._MinAccptblQty
		self._MinAccptblQty = None

	@property
	def OrdrVldtySts(self):
		return self._OrdrVldtySts

	@OrdrVldtySts.setter
	def OrdrVldtySts(self, value):
		self._OrdrVldtySts = value if type(value) != base_types.auto else self.make_default("OrdrVldtySts")

	@OrdrVldtySts.deleter
	def OrdrVldtySts(self):
		del self._OrdrVldtySts
		self._OrdrVldtySts = None

	@property
	def SlfExctnPrvntn(self):
		return self._SlfExctnPrvntn

	@SlfExctnPrvntn.setter
	def SlfExctnPrvntn(self, value):
		self._SlfExctnPrvntn = value if type(value) != base_types.auto else self.make_default("SlfExctnPrvntn")

	@SlfExctnPrvntn.deleter
	def SlfExctnPrvntn(self):
		del self._SlfExctnPrvntn
		self._SlfExctnPrvntn = None

	@property
	def MinExctbl(self):
		return self._MinExctbl

	@MinExctbl.setter
	def MinExctbl(self, value):
		self._MinExctbl = value if type(value) != base_types.auto else self.make_default("MinExctbl")

	@MinExctbl.deleter
	def MinExctbl(self):
		del self._MinExctbl
		self._MinExctbl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RmngQty', type=FinancialInstrumentQuantity25Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtgStrtgy', type=Max50Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitlQty', type=FinancialInstrumentQuantity25Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrSts', type=OrderStatus11Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BuySellInd', type=Side6Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PssvOnlyInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DispdQty', type=FinancialInstrumentQuantity25Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinAccptblQty', type=FinancialInstrumentQuantity25Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrVldtySts', type=OrderStatus10Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SlfExctnPrvntn', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinExctbl', type=MinimumExecutable1, min=0, max=1, mutex_group=None, array=False),
	))

