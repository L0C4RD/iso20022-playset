# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import TransactionTotalsSet2

class ReportGetTotalsResponse2(base_types._BaseFieldType):

	__slots__ = ["_POIRcncltnId", "_TxTtlsSet"]
	@property
	def POIRcncltnId(self):
		return self._POIRcncltnId

	@POIRcncltnId.setter
	def POIRcncltnId(self, value):
		self._POIRcncltnId = value if value is not None else base_types.UninitialisedField(self, 'POIRcncltnId', Max35Text, False)

	@POIRcncltnId.deleter
	def POIRcncltnId(self):
		del self._POIRcncltnId
		self._POIRcncltnId = base_types.UninitialisedField(self, 'POIRcncltnId', Max35Text, False)

	@property
	def TxTtlsSet(self):
		return self._TxTtlsSet

	@TxTtlsSet.setter
	def TxTtlsSet(self, value):
		self._TxTtlsSet = value if value is not None else base_types.UninitialisedField(self, 'TxTtlsSet', TransactionTotalsSet2, True)

	@TxTtlsSet.deleter
	def TxTtlsSet(self):
		del self._TxTtlsSet
		self._TxTtlsSet = base_types.UninitialisedField(self, 'TxTtlsSet', TransactionTotalsSet2, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='POIRcncltnId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTtlsSet', type=TransactionTotalsSet2, min=0, max=None, mutex_group=None, array=True),
	))