# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Pagination1 import Pagination1
from ._PartyIdentification253Choice import PartyIdentification253Choice
from ._SecuritiesAccount18 import SecuritiesAccount18
from ._Statement86 import Statement86
from ._SupplementaryData1 import SupplementaryData1
from ._TradeLegStatement5 import TradeLegStatement5

class TradeLegStatementV05(base_types._BaseFieldType):

	__slots__ = ["_ClrAcct", "_ClrMmb", "_Pgntn", "_SplmtryData", "_StmtDtls", "_StmtParams"]
	@property
	def ClrAcct(self):
		return self._ClrAcct

	@ClrAcct.setter
	def ClrAcct(self, value):
		self._ClrAcct = value if type(value) != base_types.auto else self.make_default("ClrAcct")

	@ClrAcct.deleter
	def ClrAcct(self):
		del self._ClrAcct
		self._ClrAcct = None

	@property
	def ClrMmb(self):
		return self._ClrMmb

	@ClrMmb.setter
	def ClrMmb(self, value):
		self._ClrMmb = value if type(value) != base_types.auto else self.make_default("ClrMmb")

	@ClrMmb.deleter
	def ClrMmb(self):
		del self._ClrMmb
		self._ClrMmb = None

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
	def StmtDtls(self):
		return self._StmtDtls

	@StmtDtls.setter
	def StmtDtls(self, value):
		self._StmtDtls = value if type(value) != base_types.auto else self.make_default("StmtDtls")

	@StmtDtls.deleter
	def StmtDtls(self):
		del self._StmtDtls
		self._StmtDtls = None

	@property
	def StmtParams(self):
		return self._StmtParams

	@StmtParams.setter
	def StmtParams(self, value):
		self._StmtParams = value if type(value) != base_types.auto else self.make_default("StmtParams")

	@StmtParams.deleter
	def StmtParams(self):
		del self._StmtParams
		self._StmtParams = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClrAcct', type=SecuritiesAccount18, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrMmb', type=PartyIdentification253Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pgntn', type=Pagination1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StmtDtls', type=TradeLegStatement5, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StmtParams', type=Statement86, min=1, max=1, mutex_group=None, array=False),
	))