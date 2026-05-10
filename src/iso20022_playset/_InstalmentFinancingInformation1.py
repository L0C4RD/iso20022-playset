from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._FinancingResult1 import FinancingResult1
from ._Max70Text import Max70Text

class InstalmentFinancingInformation1(base_types._BaseFieldType):

	__slots__ = ["_InstlmtFincgRslt", "_InstlmtSeqId", "_InstlmtTtlAmt"]
	@property
	def InstlmtFincgRslt(self):
		return self._InstlmtFincgRslt

	@InstlmtFincgRslt.setter
	def InstlmtFincgRslt(self, value):
		self._InstlmtFincgRslt = value if type(value) != base_types.auto else self.make_default("InstlmtFincgRslt")

	@InstlmtFincgRslt.deleter
	def InstlmtFincgRslt(self):
		del self._InstlmtFincgRslt
		self._InstlmtFincgRslt = None

	@property
	def InstlmtSeqId(self):
		return self._InstlmtSeqId

	@InstlmtSeqId.setter
	def InstlmtSeqId(self, value):
		self._InstlmtSeqId = value if type(value) != base_types.auto else self.make_default("InstlmtSeqId")

	@InstlmtSeqId.deleter
	def InstlmtSeqId(self):
		del self._InstlmtSeqId
		self._InstlmtSeqId = None

	@property
	def InstlmtTtlAmt(self):
		return self._InstlmtTtlAmt

	@InstlmtTtlAmt.setter
	def InstlmtTtlAmt(self, value):
		self._InstlmtTtlAmt = value if type(value) != base_types.auto else self.make_default("InstlmtTtlAmt")

	@InstlmtTtlAmt.deleter
	def InstlmtTtlAmt(self):
		del self._InstlmtTtlAmt
		self._InstlmtTtlAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='InstlmtFincgRslt', type=FinancingResult1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstlmtSeqId', type=Max70Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstlmtTtlAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))

