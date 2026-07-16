# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Pagination1
from . import PartyIdentification253Choice
from . import SecuritiesAccount18
from . import Statement86
from . import SupplementaryData1
from . import TradeLegStatement4

class TradeLegStatementV04(base_types._BaseFieldType):

	__slots__ = ["_ClrAcct", "_ClrMmb", "_Pgntn", "_SplmtryData", "_StmtDtls", "_StmtParams"]
	@property
	def ClrAcct(self):
		return self._ClrAcct

	@ClrAcct.setter
	def ClrAcct(self, value):
		self._ClrAcct = value if value is not None else base_types.UninitialisedField(self, 'ClrAcct', SecuritiesAccount18, False)

	@ClrAcct.deleter
	def ClrAcct(self):
		del self._ClrAcct
		self._ClrAcct = base_types.UninitialisedField(self, 'ClrAcct', SecuritiesAccount18, False)

	@property
	def ClrMmb(self):
		return self._ClrMmb

	@ClrMmb.setter
	def ClrMmb(self, value):
		self._ClrMmb = value if value is not None else base_types.UninitialisedField(self, 'ClrMmb', PartyIdentification253Choice, False)

	@ClrMmb.deleter
	def ClrMmb(self):
		del self._ClrMmb
		self._ClrMmb = base_types.UninitialisedField(self, 'ClrMmb', PartyIdentification253Choice, False)

	@property
	def Pgntn(self):
		return self._Pgntn

	@Pgntn.setter
	def Pgntn(self, value):
		self._Pgntn = value if value is not None else base_types.UninitialisedField(self, 'Pgntn', Pagination1, False)

	@Pgntn.deleter
	def Pgntn(self):
		del self._Pgntn
		self._Pgntn = base_types.UninitialisedField(self, 'Pgntn', Pagination1, False)

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

	@property
	def StmtDtls(self):
		return self._StmtDtls

	@StmtDtls.setter
	def StmtDtls(self, value):
		self._StmtDtls = value if value is not None else base_types.UninitialisedField(self, 'StmtDtls', TradeLegStatement4, True)

	@StmtDtls.deleter
	def StmtDtls(self):
		del self._StmtDtls
		self._StmtDtls = base_types.UninitialisedField(self, 'StmtDtls', TradeLegStatement4, True)

	@property
	def StmtParams(self):
		return self._StmtParams

	@StmtParams.setter
	def StmtParams(self, value):
		self._StmtParams = value if value is not None else base_types.UninitialisedField(self, 'StmtParams', Statement86, False)

	@StmtParams.deleter
	def StmtParams(self):
		del self._StmtParams
		self._StmtParams = base_types.UninitialisedField(self, 'StmtParams', Statement86, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClrAcct', type=SecuritiesAccount18, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrMmb', type=PartyIdentification253Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pgntn', type=Pagination1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StmtDtls', type=TradeLegStatement4, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StmtParams', type=Statement86, min=1, max=1, mutex_group=None, array=False),
	))