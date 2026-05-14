from . import base_types
from ._ATICALaxProcessing import ATICALaxProcessing
from ._Exact1NumericText import Exact1NumericText
from ._Exact2NumericText import Exact2NumericText
from ._ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount
from ._Max35Text import Max35Text

class RecurringPaymentData1(base_types._BaseFieldType):

	__slots__ = ["_Frqcy", "_MaxRcrngPmtAmt", "_NbOfRcrngPmt", "_NtlData", "_PerTxAmtInd", "_PrvtData", "_RegnRefNb", "_Tp", "_VldtnInd"]
	@property
	def Frqcy(self):
		return self._Frqcy

	@Frqcy.setter
	def Frqcy(self, value):
		self._Frqcy = value if type(value) != base_types.auto else self.make_default("Frqcy")

	@Frqcy.deleter
	def Frqcy(self):
		del self._Frqcy
		self._Frqcy = None

	@property
	def MaxRcrngPmtAmt(self):
		return self._MaxRcrngPmtAmt

	@MaxRcrngPmtAmt.setter
	def MaxRcrngPmtAmt(self, value):
		self._MaxRcrngPmtAmt = value if type(value) != base_types.auto else self.make_default("MaxRcrngPmtAmt")

	@MaxRcrngPmtAmt.deleter
	def MaxRcrngPmtAmt(self):
		del self._MaxRcrngPmtAmt
		self._MaxRcrngPmtAmt = None

	@property
	def NbOfRcrngPmt(self):
		return self._NbOfRcrngPmt

	@NbOfRcrngPmt.setter
	def NbOfRcrngPmt(self, value):
		self._NbOfRcrngPmt = value if type(value) != base_types.auto else self.make_default("NbOfRcrngPmt")

	@NbOfRcrngPmt.deleter
	def NbOfRcrngPmt(self):
		del self._NbOfRcrngPmt
		self._NbOfRcrngPmt = None

	@property
	def NtlData(self):
		return self._NtlData

	@NtlData.setter
	def NtlData(self, value):
		self._NtlData = value if type(value) != base_types.auto else self.make_default("NtlData")

	@NtlData.deleter
	def NtlData(self):
		del self._NtlData
		self._NtlData = None

	@property
	def PerTxAmtInd(self):
		return self._PerTxAmtInd

	@PerTxAmtInd.setter
	def PerTxAmtInd(self, value):
		self._PerTxAmtInd = value if type(value) != base_types.auto else self.make_default("PerTxAmtInd")

	@PerTxAmtInd.deleter
	def PerTxAmtInd(self):
		del self._PerTxAmtInd
		self._PerTxAmtInd = None

	@property
	def PrvtData(self):
		return self._PrvtData

	@PrvtData.setter
	def PrvtData(self, value):
		self._PrvtData = value if type(value) != base_types.auto else self.make_default("PrvtData")

	@PrvtData.deleter
	def PrvtData(self):
		del self._PrvtData
		self._PrvtData = None

	@property
	def RegnRefNb(self):
		return self._RegnRefNb

	@RegnRefNb.setter
	def RegnRefNb(self, value):
		self._RegnRefNb = value if type(value) != base_types.auto else self.make_default("RegnRefNb")

	@RegnRefNb.deleter
	def RegnRefNb(self):
		del self._RegnRefNb
		self._RegnRefNb = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def VldtnInd(self):
		return self._VldtnInd

	@VldtnInd.setter
	def VldtnInd(self, value):
		self._VldtnInd = value if type(value) != base_types.auto else self.make_default("VldtnInd")

	@VldtnInd.deleter
	def VldtnInd(self):
		del self._VldtnInd
		self._VldtnInd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Frqcy', type=Exact2NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxRcrngPmtAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfRcrngPmt', type=Exact2NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtlData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PerTxAmtInd', type=Exact1NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvtData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RegnRefNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=Exact1NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldtnInd', type=Exact1NumericText, min=0, max=1, mutex_group=None, array=False),
	))

