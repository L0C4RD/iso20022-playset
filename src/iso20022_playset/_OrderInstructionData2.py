# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrumentQuantity25Choice
from . import Max50Text
from . import MinimumExecutable1
from . import OrderStatus10Code
from . import OrderStatus11Code
from . import Side6Code
from . import TrueFalseIndicator

class OrderInstructionData2(base_types._BaseFieldType):

	__slots__ = ["_BuySellInd", "_DispdQty", "_InitlQty", "_MinAccptblQty", "_MinExctbl", "_OrdrSts", "_OrdrVldtySts", "_PssvOnlyInd", "_RmngQty", "_RtgStrtgy", "_SlfExctnPrvntn"]
	@property
	def BuySellInd(self):
		return self._BuySellInd

	@BuySellInd.setter
	def BuySellInd(self, value):
		self._BuySellInd = value if value is not None else base_types.UninitialisedField(self, 'BuySellInd', Side6Code, False)

	@BuySellInd.deleter
	def BuySellInd(self):
		del self._BuySellInd
		self._BuySellInd = base_types.UninitialisedField(self, 'BuySellInd', Side6Code, False)

	@property
	def DispdQty(self):
		return self._DispdQty

	@DispdQty.setter
	def DispdQty(self, value):
		self._DispdQty = value if value is not None else base_types.UninitialisedField(self, 'DispdQty', FinancialInstrumentQuantity25Choice, False)

	@DispdQty.deleter
	def DispdQty(self):
		del self._DispdQty
		self._DispdQty = base_types.UninitialisedField(self, 'DispdQty', FinancialInstrumentQuantity25Choice, False)

	@property
	def InitlQty(self):
		return self._InitlQty

	@InitlQty.setter
	def InitlQty(self, value):
		self._InitlQty = value if value is not None else base_types.UninitialisedField(self, 'InitlQty', FinancialInstrumentQuantity25Choice, False)

	@InitlQty.deleter
	def InitlQty(self):
		del self._InitlQty
		self._InitlQty = base_types.UninitialisedField(self, 'InitlQty', FinancialInstrumentQuantity25Choice, False)

	@property
	def MinAccptblQty(self):
		return self._MinAccptblQty

	@MinAccptblQty.setter
	def MinAccptblQty(self, value):
		self._MinAccptblQty = value if value is not None else base_types.UninitialisedField(self, 'MinAccptblQty', FinancialInstrumentQuantity25Choice, False)

	@MinAccptblQty.deleter
	def MinAccptblQty(self):
		del self._MinAccptblQty
		self._MinAccptblQty = base_types.UninitialisedField(self, 'MinAccptblQty', FinancialInstrumentQuantity25Choice, False)

	@property
	def MinExctbl(self):
		return self._MinExctbl

	@MinExctbl.setter
	def MinExctbl(self, value):
		self._MinExctbl = value if value is not None else base_types.UninitialisedField(self, 'MinExctbl', MinimumExecutable1, False)

	@MinExctbl.deleter
	def MinExctbl(self):
		del self._MinExctbl
		self._MinExctbl = base_types.UninitialisedField(self, 'MinExctbl', MinimumExecutable1, False)

	@property
	def OrdrSts(self):
		return self._OrdrSts

	@OrdrSts.setter
	def OrdrSts(self, value):
		self._OrdrSts = value if value is not None else base_types.UninitialisedField(self, 'OrdrSts', OrderStatus11Code, True)

	@OrdrSts.deleter
	def OrdrSts(self):
		del self._OrdrSts
		self._OrdrSts = base_types.UninitialisedField(self, 'OrdrSts', OrderStatus11Code, True)

	@property
	def OrdrVldtySts(self):
		return self._OrdrVldtySts

	@OrdrVldtySts.setter
	def OrdrVldtySts(self, value):
		self._OrdrVldtySts = value if value is not None else base_types.UninitialisedField(self, 'OrdrVldtySts', OrderStatus10Code, False)

	@OrdrVldtySts.deleter
	def OrdrVldtySts(self):
		del self._OrdrVldtySts
		self._OrdrVldtySts = base_types.UninitialisedField(self, 'OrdrVldtySts', OrderStatus10Code, False)

	@property
	def PssvOnlyInd(self):
		return self._PssvOnlyInd

	@PssvOnlyInd.setter
	def PssvOnlyInd(self, value):
		self._PssvOnlyInd = value if value is not None else base_types.UninitialisedField(self, 'PssvOnlyInd', TrueFalseIndicator, False)

	@PssvOnlyInd.deleter
	def PssvOnlyInd(self):
		del self._PssvOnlyInd
		self._PssvOnlyInd = base_types.UninitialisedField(self, 'PssvOnlyInd', TrueFalseIndicator, False)

	@property
	def RmngQty(self):
		return self._RmngQty

	@RmngQty.setter
	def RmngQty(self, value):
		self._RmngQty = value if value is not None else base_types.UninitialisedField(self, 'RmngQty', FinancialInstrumentQuantity25Choice, False)

	@RmngQty.deleter
	def RmngQty(self):
		del self._RmngQty
		self._RmngQty = base_types.UninitialisedField(self, 'RmngQty', FinancialInstrumentQuantity25Choice, False)

	@property
	def RtgStrtgy(self):
		return self._RtgStrtgy

	@RtgStrtgy.setter
	def RtgStrtgy(self, value):
		self._RtgStrtgy = value if value is not None else base_types.UninitialisedField(self, 'RtgStrtgy', Max50Text, False)

	@RtgStrtgy.deleter
	def RtgStrtgy(self):
		del self._RtgStrtgy
		self._RtgStrtgy = base_types.UninitialisedField(self, 'RtgStrtgy', Max50Text, False)

	@property
	def SlfExctnPrvntn(self):
		return self._SlfExctnPrvntn

	@SlfExctnPrvntn.setter
	def SlfExctnPrvntn(self, value):
		self._SlfExctnPrvntn = value if value is not None else base_types.UninitialisedField(self, 'SlfExctnPrvntn', TrueFalseIndicator, False)

	@SlfExctnPrvntn.deleter
	def SlfExctnPrvntn(self):
		del self._SlfExctnPrvntn
		self._SlfExctnPrvntn = base_types.UninitialisedField(self, 'SlfExctnPrvntn', TrueFalseIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BuySellInd', type=Side6Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DispdQty', type=FinancialInstrumentQuantity25Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitlQty', type=FinancialInstrumentQuantity25Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinAccptblQty', type=FinancialInstrumentQuantity25Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinExctbl', type=MinimumExecutable1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrSts', type=OrderStatus11Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrdrVldtySts', type=OrderStatus10Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PssvOnlyInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmngQty', type=FinancialInstrumentQuantity25Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtgStrtgy', type=Max50Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SlfExctnPrvntn', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
	))