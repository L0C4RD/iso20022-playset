from . import base_types
from .PercentageRate import PercentageRate
from .DecimalNumber import DecimalNumber
from .BaseOneRate import BaseOneRate
from .AmountAndDirection107 import AmountAndDirection107

class SecuritiesTransactionPrice18Choice(base_types._BaseFieldType):

	__slots__ = ["_Dcml", "_BsisPts", "_Pctg", "_MntryVal"]
	@property
	def Dcml(self):
		return self._Dcml

	@Dcml.setter
	def Dcml(self, value):
		self._Dcml = value if type(value) != auto else self.make_default("Dcml")

	@Dcml.deleter
	def Dcml(self):
		del self._Dcml
		self._Dcml = None

	@property
	def BsisPts(self):
		return self._BsisPts

	@BsisPts.setter
	def BsisPts(self, value):
		self._BsisPts = value if type(value) != auto else self.make_default("BsisPts")

	@BsisPts.deleter
	def BsisPts(self):
		del self._BsisPts
		self._BsisPts = None

	@property
	def Pctg(self):
		return self._Pctg

	@Pctg.setter
	def Pctg(self, value):
		self._Pctg = value if type(value) != auto else self.make_default("Pctg")

	@Pctg.deleter
	def Pctg(self):
		del self._Pctg
		self._Pctg = None

	@property
	def MntryVal(self):
		return self._MntryVal

	@MntryVal.setter
	def MntryVal(self, value):
		self._MntryVal = value if type(value) != auto else self.make_default("MntryVal")

	@MntryVal.deleter
	def MntryVal(self):
		del self._MntryVal
		self._MntryVal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dcml', type=BaseOneRate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='BsisPts', type=DecimalNumber, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Pctg', type=PercentageRate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='MntryVal', type=AmountAndDirection107, min=0, max=1, mutex_group=1, array=False),
	))

