from . import base_types
from ._Pagination1 import Pagination1
from ._SecuritiesModification2 import SecuritiesModification2
from ._SecuritiesTransactionReport5 import SecuritiesTransactionReport5
from ._SupplementaryData1 import SupplementaryData1

class SecuritiesSettlementConditionsModificationRequestReportV01(base_types._BaseFieldType):

	__slots__ = ["_Mods", "_Pgntn", "_RptGnlDtls", "_SplmtryData"]
	@property
	def Mods(self):
		return self._Mods

	@Mods.setter
	def Mods(self, value):
		self._Mods = value if type(value) != base_types.auto else self.make_default("Mods")

	@Mods.deleter
	def Mods(self):
		del self._Mods
		self._Mods = None

	@property
	def Pgntn(self):
		return self._Pgntn

	@Pgntn.setter
	def Pgntn(self, value):
		self._Pgntn = value if type(value) != base_types.auto else self.make_default("Pgntn")

	@Pgntn.deleter
	def Pgntn(self):
		del self._Pgntn
		self._Pgntn = None

	@property
	def RptGnlDtls(self):
		return self._RptGnlDtls

	@RptGnlDtls.setter
	def RptGnlDtls(self, value):
		self._RptGnlDtls = value if type(value) != base_types.auto else self.make_default("RptGnlDtls")

	@RptGnlDtls.deleter
	def RptGnlDtls(self):
		del self._RptGnlDtls
		self._RptGnlDtls = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Mods', type=SecuritiesModification2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Pgntn', type=Pagination1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptGnlDtls', type=SecuritiesTransactionReport5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

