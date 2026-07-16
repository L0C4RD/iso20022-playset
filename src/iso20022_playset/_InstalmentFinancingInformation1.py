# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import FinancingResult1
from . import Max70Text

class InstalmentFinancingInformation1(base_types._BaseFieldType):

	__slots__ = ["_InstlmtFincgRslt", "_InstlmtSeqId", "_InstlmtTtlAmt"]
	@property
	def InstlmtFincgRslt(self):
		return self._InstlmtFincgRslt

	@InstlmtFincgRslt.setter
	def InstlmtFincgRslt(self, value):
		self._InstlmtFincgRslt = value if value is not None else base_types.UninitialisedField(self, 'InstlmtFincgRslt', FinancingResult1, False)

	@InstlmtFincgRslt.deleter
	def InstlmtFincgRslt(self):
		del self._InstlmtFincgRslt
		self._InstlmtFincgRslt = base_types.UninitialisedField(self, 'InstlmtFincgRslt', FinancingResult1, False)

	@property
	def InstlmtSeqId(self):
		return self._InstlmtSeqId

	@InstlmtSeqId.setter
	def InstlmtSeqId(self, value):
		self._InstlmtSeqId = value if value is not None else base_types.UninitialisedField(self, 'InstlmtSeqId', Max70Text, False)

	@InstlmtSeqId.deleter
	def InstlmtSeqId(self):
		del self._InstlmtSeqId
		self._InstlmtSeqId = base_types.UninitialisedField(self, 'InstlmtSeqId', Max70Text, False)

	@property
	def InstlmtTtlAmt(self):
		return self._InstlmtTtlAmt

	@InstlmtTtlAmt.setter
	def InstlmtTtlAmt(self, value):
		self._InstlmtTtlAmt = value if value is not None else base_types.UninitialisedField(self, 'InstlmtTtlAmt', ActiveCurrencyAndAmount, False)

	@InstlmtTtlAmt.deleter
	def InstlmtTtlAmt(self):
		del self._InstlmtTtlAmt
		self._InstlmtTtlAmt = base_types.UninitialisedField(self, 'InstlmtTtlAmt', ActiveCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='InstlmtFincgRslt', type=FinancingResult1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstlmtSeqId', type=Max70Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstlmtTtlAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))