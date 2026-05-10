from . import base_types
import TransactionTotalsSet2
import Max35Text

class ReportGetTotalsResponse2(base_types._BaseFieldType):

	__slots__ = ["_POIRcncltnId", "_TxTtlsSet"]
	@property
	def POIRcncltnId(self):
		return self._POIRcncltnId

	@POIRcncltnId.setter
	def POIRcncltnId(self, value):
		self._POIRcncltnId = value if type(value) != auto else self.make_default("POIRcncltnId")

	@POIRcncltnId.deleter
	def POIRcncltnId(self):
		del self._POIRcncltnId
		self._POIRcncltnId = None

	@property
	def TxTtlsSet(self):
		return self._TxTtlsSet

	@TxTtlsSet.setter
	def TxTtlsSet(self, value):
		self._TxTtlsSet = value if type(value) != auto else self.make_default("TxTtlsSet")

	@TxTtlsSet.deleter
	def TxTtlsSet(self):
		del self._TxTtlsSet
		self._TxTtlsSet = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='POIRcncltnId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTtlsSet', type=TransactionTotalsSet2, min=0, max=None, mutex_group=None, array=True),
	))

