from . import base_types
from .Max15NumericText import Max15NumericText
from .RejectionReason53 import RejectionReason53

class DetailedTransactionStatistics13(base_types._BaseFieldType):

	__slots__ = ["_TtlNbOfTxs", "_TtlNbOfTxsRjctd", "_TxsRjctnsRsn", "_TtlNbOfTxsAccptd"]
	@property
	def TtlNbOfTxs(self):
		return self._TtlNbOfTxs

	@TtlNbOfTxs.setter
	def TtlNbOfTxs(self, value):
		self._TtlNbOfTxs = value if type(value) != auto else self.make_default("TtlNbOfTxs")

	@TtlNbOfTxs.deleter
	def TtlNbOfTxs(self):
		del self._TtlNbOfTxs
		self._TtlNbOfTxs = None

	@property
	def TtlNbOfTxsRjctd(self):
		return self._TtlNbOfTxsRjctd

	@TtlNbOfTxsRjctd.setter
	def TtlNbOfTxsRjctd(self, value):
		self._TtlNbOfTxsRjctd = value if type(value) != auto else self.make_default("TtlNbOfTxsRjctd")

	@TtlNbOfTxsRjctd.deleter
	def TtlNbOfTxsRjctd(self):
		del self._TtlNbOfTxsRjctd
		self._TtlNbOfTxsRjctd = None

	@property
	def TxsRjctnsRsn(self):
		return self._TxsRjctnsRsn

	@TxsRjctnsRsn.setter
	def TxsRjctnsRsn(self, value):
		self._TxsRjctnsRsn = value if type(value) != auto else self.make_default("TxsRjctnsRsn")

	@TxsRjctnsRsn.deleter
	def TxsRjctnsRsn(self):
		del self._TxsRjctnsRsn
		self._TxsRjctnsRsn = None

	@property
	def TtlNbOfTxsAccptd(self):
		return self._TtlNbOfTxsAccptd

	@TtlNbOfTxsAccptd.setter
	def TtlNbOfTxsAccptd(self, value):
		self._TtlNbOfTxsAccptd = value if type(value) != auto else self.make_default("TtlNbOfTxsAccptd")

	@TtlNbOfTxsAccptd.deleter
	def TtlNbOfTxsAccptd(self):
		del self._TtlNbOfTxsAccptd
		self._TtlNbOfTxsAccptd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TtlNbOfTxs', type=Max15NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNbOfTxsRjctd', type=Max15NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxsRjctnsRsn', type=RejectionReason53, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlNbOfTxsAccptd', type=Max15NumericText, min=1, max=1, mutex_group=None, array=False),
	))

