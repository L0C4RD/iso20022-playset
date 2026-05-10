from . import base_types
from ._SupplementaryData1 import SupplementaryData1
from ._NumberOfReportsPerStatus4 import NumberOfReportsPerStatus4
from ._ReconciliationReport8 import ReconciliationReport8

class TradeData28(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_RcncltnRpt", "_PairgRcncltnSts"]
	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def RcncltnRpt(self):
		return self._RcncltnRpt

	@RcncltnRpt.setter
	def RcncltnRpt(self, value):
		self._RcncltnRpt = value if type(value) != base_types.auto else self.make_default("RcncltnRpt")

	@RcncltnRpt.deleter
	def RcncltnRpt(self):
		del self._RcncltnRpt
		self._RcncltnRpt = None

	@property
	def PairgRcncltnSts(self):
		return self._PairgRcncltnSts

	@PairgRcncltnSts.setter
	def PairgRcncltnSts(self, value):
		self._PairgRcncltnSts = value if type(value) != base_types.auto else self.make_default("PairgRcncltnSts")

	@PairgRcncltnSts.deleter
	def PairgRcncltnSts(self):
		del self._PairgRcncltnSts
		self._PairgRcncltnSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RcncltnRpt', type=ReconciliationReport8, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PairgRcncltnSts', type=NumberOfReportsPerStatus4, min=0, max=None, mutex_group=None, array=True),
	))

