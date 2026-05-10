from . import base_types
from .SecuritiesTransactionReport2 import SecuritiesTransactionReport2
from .SupplementaryData1 import SupplementaryData1
from .SecuritiesTransactionReport7 import SecuritiesTransactionReport7

class ReportingTransactionType3Choice(base_types._BaseFieldType):

	__slots__ = ["_New", "_Cxl", "_SplmtryData"]
	@property
	def New(self):
		return self._New

	@New.setter
	def New(self, value):
		self._New = value if type(value) != auto else self.make_default("New")

	@New.deleter
	def New(self):
		del self._New
		self._New = None

	@property
	def Cxl(self):
		return self._Cxl

	@Cxl.setter
	def Cxl(self, value):
		self._Cxl = value if type(value) != auto else self.make_default("Cxl")

	@Cxl.deleter
	def Cxl(self):
		del self._Cxl
		self._Cxl = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='New', type=SecuritiesTransactionReport7, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Cxl', type=SecuritiesTransactionReport2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=1, array=True),
	))

