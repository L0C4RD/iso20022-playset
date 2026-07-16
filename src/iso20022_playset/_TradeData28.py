# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import NumberOfReportsPerStatus4
from . import ReconciliationReport8
from . import SupplementaryData1

class TradeData28(base_types._BaseFieldType):

	__slots__ = ["_PairgRcncltnSts", "_RcncltnRpt", "_SplmtryData"]
	@property
	def PairgRcncltnSts(self):
		return self._PairgRcncltnSts

	@PairgRcncltnSts.setter
	def PairgRcncltnSts(self, value):
		self._PairgRcncltnSts = value if value is not None else base_types.UninitialisedField(self, 'PairgRcncltnSts', NumberOfReportsPerStatus4, True)

	@PairgRcncltnSts.deleter
	def PairgRcncltnSts(self):
		del self._PairgRcncltnSts
		self._PairgRcncltnSts = base_types.UninitialisedField(self, 'PairgRcncltnSts', NumberOfReportsPerStatus4, True)

	@property
	def RcncltnRpt(self):
		return self._RcncltnRpt

	@RcncltnRpt.setter
	def RcncltnRpt(self, value):
		self._RcncltnRpt = value if value is not None else base_types.UninitialisedField(self, 'RcncltnRpt', ReconciliationReport8, True)

	@RcncltnRpt.deleter
	def RcncltnRpt(self):
		del self._RcncltnRpt
		self._RcncltnRpt = base_types.UninitialisedField(self, 'RcncltnRpt', ReconciliationReport8, True)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PairgRcncltnSts', type=NumberOfReportsPerStatus4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RcncltnRpt', type=ReconciliationReport8, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))