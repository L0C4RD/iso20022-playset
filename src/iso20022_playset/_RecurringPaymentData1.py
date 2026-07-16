# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATICALaxProcessing
from . import Exact1NumericText
from . import Exact2NumericText
from . import ImpliedCurrencyAndAmount
from . import Max35Text

class RecurringPaymentData1(base_types._BaseFieldType):

	__slots__ = ["_Frqcy", "_MaxRcrngPmtAmt", "_NbOfRcrngPmt", "_NtlData", "_PerTxAmtInd", "_PrvtData", "_RegnRefNb", "_Tp", "_VldtnInd"]
	@property
	def Frqcy(self):
		return self._Frqcy

	@Frqcy.setter
	def Frqcy(self, value):
		self._Frqcy = value if value is not None else base_types.UninitialisedField(self, 'Frqcy', Exact2NumericText, False)

	@Frqcy.deleter
	def Frqcy(self):
		del self._Frqcy
		self._Frqcy = base_types.UninitialisedField(self, 'Frqcy', Exact2NumericText, False)

	@property
	def MaxRcrngPmtAmt(self):
		return self._MaxRcrngPmtAmt

	@MaxRcrngPmtAmt.setter
	def MaxRcrngPmtAmt(self, value):
		self._MaxRcrngPmtAmt = value if value is not None else base_types.UninitialisedField(self, 'MaxRcrngPmtAmt', ImpliedCurrencyAndAmount, False)

	@MaxRcrngPmtAmt.deleter
	def MaxRcrngPmtAmt(self):
		del self._MaxRcrngPmtAmt
		self._MaxRcrngPmtAmt = base_types.UninitialisedField(self, 'MaxRcrngPmtAmt', ImpliedCurrencyAndAmount, False)

	@property
	def NbOfRcrngPmt(self):
		return self._NbOfRcrngPmt

	@NbOfRcrngPmt.setter
	def NbOfRcrngPmt(self, value):
		self._NbOfRcrngPmt = value if value is not None else base_types.UninitialisedField(self, 'NbOfRcrngPmt', Exact2NumericText, False)

	@NbOfRcrngPmt.deleter
	def NbOfRcrngPmt(self):
		del self._NbOfRcrngPmt
		self._NbOfRcrngPmt = base_types.UninitialisedField(self, 'NbOfRcrngPmt', Exact2NumericText, False)

	@property
	def NtlData(self):
		return self._NtlData

	@NtlData.setter
	def NtlData(self, value):
		self._NtlData = value if value is not None else base_types.UninitialisedField(self, 'NtlData', ATICALaxProcessing, True)

	@NtlData.deleter
	def NtlData(self):
		del self._NtlData
		self._NtlData = base_types.UninitialisedField(self, 'NtlData', ATICALaxProcessing, True)

	@property
	def PerTxAmtInd(self):
		return self._PerTxAmtInd

	@PerTxAmtInd.setter
	def PerTxAmtInd(self, value):
		self._PerTxAmtInd = value if value is not None else base_types.UninitialisedField(self, 'PerTxAmtInd', Exact1NumericText, False)

	@PerTxAmtInd.deleter
	def PerTxAmtInd(self):
		del self._PerTxAmtInd
		self._PerTxAmtInd = base_types.UninitialisedField(self, 'PerTxAmtInd', Exact1NumericText, False)

	@property
	def PrvtData(self):
		return self._PrvtData

	@PrvtData.setter
	def PrvtData(self, value):
		self._PrvtData = value if value is not None else base_types.UninitialisedField(self, 'PrvtData', ATICALaxProcessing, True)

	@PrvtData.deleter
	def PrvtData(self):
		del self._PrvtData
		self._PrvtData = base_types.UninitialisedField(self, 'PrvtData', ATICALaxProcessing, True)

	@property
	def RegnRefNb(self):
		return self._RegnRefNb

	@RegnRefNb.setter
	def RegnRefNb(self, value):
		self._RegnRefNb = value if value is not None else base_types.UninitialisedField(self, 'RegnRefNb', Max35Text, False)

	@RegnRefNb.deleter
	def RegnRefNb(self):
		del self._RegnRefNb
		self._RegnRefNb = base_types.UninitialisedField(self, 'RegnRefNb', Max35Text, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', Exact1NumericText, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', Exact1NumericText, False)

	@property
	def VldtnInd(self):
		return self._VldtnInd

	@VldtnInd.setter
	def VldtnInd(self, value):
		self._VldtnInd = value if value is not None else base_types.UninitialisedField(self, 'VldtnInd', Exact1NumericText, False)

	@VldtnInd.deleter
	def VldtnInd(self):
		del self._VldtnInd
		self._VldtnInd = base_types.UninitialisedField(self, 'VldtnInd', Exact1NumericText, False)

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