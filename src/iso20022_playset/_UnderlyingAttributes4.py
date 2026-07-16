# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import Max35Text
from . import PercentageRate
from . import Price8
from . import SettlementType3Choice
from . import UnitOrFaceAmount1Choice

class UnderlyingAttributes4(base_types._BaseFieldType):

	__slots__ = ["_AdjstdQty", "_AllcnPctg", "_CapVal", "_CshAmt", "_CshTp", "_CurVal", "_DrtyPric", "_EndPric", "_EndVal", "_Pric", "_Qty", "_StartVal", "_SttlmTp", "_XchgRate"]
	@property
	def AdjstdQty(self):
		return self._AdjstdQty

	@AdjstdQty.setter
	def AdjstdQty(self, value):
		self._AdjstdQty = value if value is not None else base_types.UninitialisedField(self, 'AdjstdQty', UnitOrFaceAmount1Choice, False)

	@AdjstdQty.deleter
	def AdjstdQty(self):
		del self._AdjstdQty
		self._AdjstdQty = base_types.UninitialisedField(self, 'AdjstdQty', UnitOrFaceAmount1Choice, False)

	@property
	def AllcnPctg(self):
		return self._AllcnPctg

	@AllcnPctg.setter
	def AllcnPctg(self, value):
		self._AllcnPctg = value if value is not None else base_types.UninitialisedField(self, 'AllcnPctg', PercentageRate, False)

	@AllcnPctg.deleter
	def AllcnPctg(self):
		del self._AllcnPctg
		self._AllcnPctg = base_types.UninitialisedField(self, 'AllcnPctg', PercentageRate, False)

	@property
	def CapVal(self):
		return self._CapVal

	@CapVal.setter
	def CapVal(self, value):
		self._CapVal = value if value is not None else base_types.UninitialisedField(self, 'CapVal', ActiveCurrencyAndAmount, False)

	@CapVal.deleter
	def CapVal(self):
		del self._CapVal
		self._CapVal = base_types.UninitialisedField(self, 'CapVal', ActiveCurrencyAndAmount, False)

	@property
	def CshAmt(self):
		return self._CshAmt

	@CshAmt.setter
	def CshAmt(self, value):
		self._CshAmt = value if value is not None else base_types.UninitialisedField(self, 'CshAmt', ActiveCurrencyAndAmount, False)

	@CshAmt.deleter
	def CshAmt(self):
		del self._CshAmt
		self._CshAmt = base_types.UninitialisedField(self, 'CshAmt', ActiveCurrencyAndAmount, False)

	@property
	def CshTp(self):
		return self._CshTp

	@CshTp.setter
	def CshTp(self, value):
		self._CshTp = value if value is not None else base_types.UninitialisedField(self, 'CshTp', Max35Text, False)

	@CshTp.deleter
	def CshTp(self):
		del self._CshTp
		self._CshTp = base_types.UninitialisedField(self, 'CshTp', Max35Text, False)

	@property
	def CurVal(self):
		return self._CurVal

	@CurVal.setter
	def CurVal(self, value):
		self._CurVal = value if value is not None else base_types.UninitialisedField(self, 'CurVal', ActiveCurrencyAndAmount, False)

	@CurVal.deleter
	def CurVal(self):
		del self._CurVal
		self._CurVal = base_types.UninitialisedField(self, 'CurVal', ActiveCurrencyAndAmount, False)

	@property
	def DrtyPric(self):
		return self._DrtyPric

	@DrtyPric.setter
	def DrtyPric(self, value):
		self._DrtyPric = value if value is not None else base_types.UninitialisedField(self, 'DrtyPric', Price8, False)

	@DrtyPric.deleter
	def DrtyPric(self):
		del self._DrtyPric
		self._DrtyPric = base_types.UninitialisedField(self, 'DrtyPric', Price8, False)

	@property
	def EndPric(self):
		return self._EndPric

	@EndPric.setter
	def EndPric(self, value):
		self._EndPric = value if value is not None else base_types.UninitialisedField(self, 'EndPric', Price8, False)

	@EndPric.deleter
	def EndPric(self):
		del self._EndPric
		self._EndPric = base_types.UninitialisedField(self, 'EndPric', Price8, False)

	@property
	def EndVal(self):
		return self._EndVal

	@EndVal.setter
	def EndVal(self, value):
		self._EndVal = value if value is not None else base_types.UninitialisedField(self, 'EndVal', ActiveCurrencyAndAmount, False)

	@EndVal.deleter
	def EndVal(self):
		del self._EndVal
		self._EndVal = base_types.UninitialisedField(self, 'EndVal', ActiveCurrencyAndAmount, False)

	@property
	def Pric(self):
		return self._Pric

	@Pric.setter
	def Pric(self, value):
		self._Pric = value if value is not None else base_types.UninitialisedField(self, 'Pric', Price8, False)

	@Pric.deleter
	def Pric(self):
		del self._Pric
		self._Pric = base_types.UninitialisedField(self, 'Pric', Price8, False)

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if value is not None else base_types.UninitialisedField(self, 'Qty', UnitOrFaceAmount1Choice, False)

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = base_types.UninitialisedField(self, 'Qty', UnitOrFaceAmount1Choice, False)

	@property
	def StartVal(self):
		return self._StartVal

	@StartVal.setter
	def StartVal(self, value):
		self._StartVal = value if value is not None else base_types.UninitialisedField(self, 'StartVal', ActiveCurrencyAndAmount, False)

	@StartVal.deleter
	def StartVal(self):
		del self._StartVal
		self._StartVal = base_types.UninitialisedField(self, 'StartVal', ActiveCurrencyAndAmount, False)

	@property
	def SttlmTp(self):
		return self._SttlmTp

	@SttlmTp.setter
	def SttlmTp(self, value):
		self._SttlmTp = value if value is not None else base_types.UninitialisedField(self, 'SttlmTp', SettlementType3Choice, False)

	@SttlmTp.deleter
	def SttlmTp(self):
		del self._SttlmTp
		self._SttlmTp = base_types.UninitialisedField(self, 'SttlmTp', SettlementType3Choice, False)

	@property
	def XchgRate(self):
		return self._XchgRate

	@XchgRate.setter
	def XchgRate(self, value):
		self._XchgRate = value if value is not None else base_types.UninitialisedField(self, 'XchgRate', PercentageRate, False)

	@XchgRate.deleter
	def XchgRate(self):
		del self._XchgRate
		self._XchgRate = base_types.UninitialisedField(self, 'XchgRate', PercentageRate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AdjstdQty', type=UnitOrFaceAmount1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AllcnPctg', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CapVal', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CurVal', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DrtyPric', type=Price8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EndPric', type=Price8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EndVal', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pric', type=Price8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=UnitOrFaceAmount1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StartVal', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmTp', type=SettlementType3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
	))