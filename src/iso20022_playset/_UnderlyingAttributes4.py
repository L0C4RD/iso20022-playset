from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._UnitOrFaceAmount1Choice import UnitOrFaceAmount1Choice
from ._SettlementType3Choice import SettlementType3Choice
from ._Max35Text import Max35Text
from ._PercentageRate import PercentageRate
from ._Price8 import Price8

class UnderlyingAttributes4(base_types._BaseFieldType):

	__slots__ = ["_AdjstdQty", "_SttlmTp", "_CurVal", "_CshAmt", "_EndVal", "_CshTp", "_EndPric", "_Qty", "_XchgRate", "_CapVal", "_AllcnPctg", "_StartVal", "_DrtyPric", "_Pric"]
	@property
	def AdjstdQty(self):
		return self._AdjstdQty

	@AdjstdQty.setter
	def AdjstdQty(self, value):
		self._AdjstdQty = value if type(value) != base_types.auto else self.make_default("AdjstdQty")

	@AdjstdQty.deleter
	def AdjstdQty(self):
		del self._AdjstdQty
		self._AdjstdQty = None

	@property
	def SttlmTp(self):
		return self._SttlmTp

	@SttlmTp.setter
	def SttlmTp(self, value):
		self._SttlmTp = value if type(value) != base_types.auto else self.make_default("SttlmTp")

	@SttlmTp.deleter
	def SttlmTp(self):
		del self._SttlmTp
		self._SttlmTp = None

	@property
	def CurVal(self):
		return self._CurVal

	@CurVal.setter
	def CurVal(self, value):
		self._CurVal = value if type(value) != base_types.auto else self.make_default("CurVal")

	@CurVal.deleter
	def CurVal(self):
		del self._CurVal
		self._CurVal = None

	@property
	def CshAmt(self):
		return self._CshAmt

	@CshAmt.setter
	def CshAmt(self, value):
		self._CshAmt = value if type(value) != base_types.auto else self.make_default("CshAmt")

	@CshAmt.deleter
	def CshAmt(self):
		del self._CshAmt
		self._CshAmt = None

	@property
	def EndVal(self):
		return self._EndVal

	@EndVal.setter
	def EndVal(self, value):
		self._EndVal = value if type(value) != base_types.auto else self.make_default("EndVal")

	@EndVal.deleter
	def EndVal(self):
		del self._EndVal
		self._EndVal = None

	@property
	def CshTp(self):
		return self._CshTp

	@CshTp.setter
	def CshTp(self, value):
		self._CshTp = value if type(value) != base_types.auto else self.make_default("CshTp")

	@CshTp.deleter
	def CshTp(self):
		del self._CshTp
		self._CshTp = None

	@property
	def EndPric(self):
		return self._EndPric

	@EndPric.setter
	def EndPric(self, value):
		self._EndPric = value if type(value) != base_types.auto else self.make_default("EndPric")

	@EndPric.deleter
	def EndPric(self):
		del self._EndPric
		self._EndPric = None

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if type(value) != base_types.auto else self.make_default("Qty")

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = None

	@property
	def XchgRate(self):
		return self._XchgRate

	@XchgRate.setter
	def XchgRate(self, value):
		self._XchgRate = value if type(value) != base_types.auto else self.make_default("XchgRate")

	@XchgRate.deleter
	def XchgRate(self):
		del self._XchgRate
		self._XchgRate = None

	@property
	def CapVal(self):
		return self._CapVal

	@CapVal.setter
	def CapVal(self, value):
		self._CapVal = value if type(value) != base_types.auto else self.make_default("CapVal")

	@CapVal.deleter
	def CapVal(self):
		del self._CapVal
		self._CapVal = None

	@property
	def AllcnPctg(self):
		return self._AllcnPctg

	@AllcnPctg.setter
	def AllcnPctg(self, value):
		self._AllcnPctg = value if type(value) != base_types.auto else self.make_default("AllcnPctg")

	@AllcnPctg.deleter
	def AllcnPctg(self):
		del self._AllcnPctg
		self._AllcnPctg = None

	@property
	def StartVal(self):
		return self._StartVal

	@StartVal.setter
	def StartVal(self, value):
		self._StartVal = value if type(value) != base_types.auto else self.make_default("StartVal")

	@StartVal.deleter
	def StartVal(self):
		del self._StartVal
		self._StartVal = None

	@property
	def DrtyPric(self):
		return self._DrtyPric

	@DrtyPric.setter
	def DrtyPric(self, value):
		self._DrtyPric = value if type(value) != base_types.auto else self.make_default("DrtyPric")

	@DrtyPric.deleter
	def DrtyPric(self):
		del self._DrtyPric
		self._DrtyPric = None

	@property
	def Pric(self):
		return self._Pric

	@Pric.setter
	def Pric(self, value):
		self._Pric = value if type(value) != base_types.auto else self.make_default("Pric")

	@Pric.deleter
	def Pric(self):
		del self._Pric
		self._Pric = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AdjstdQty', type=UnitOrFaceAmount1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmTp', type=SettlementType3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CurVal', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EndVal', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EndPric', type=Price8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=UnitOrFaceAmount1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CapVal', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AllcnPctg', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StartVal', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DrtyPric', type=Price8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pric', type=Price8, min=0, max=1, mutex_group=None, array=False),
	))

