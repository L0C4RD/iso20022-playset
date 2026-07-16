# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max20PositiveNumber
from . import RejectionReason71

class DetailedTransactionStatistics30(base_types._BaseFieldType):

	__slots__ = ["_TtlCrrctdRjctns", "_TtlNbOfTxs", "_TtlNbOfTxsAccptd", "_TtlNbOfTxsRjctd", "_TxsRjctnsRsn"]
	@property
	def TtlCrrctdRjctns(self):
		return self._TtlCrrctdRjctns

	@TtlCrrctdRjctns.setter
	def TtlCrrctdRjctns(self, value):
		self._TtlCrrctdRjctns = value if value is not None else base_types.UninitialisedField(self, 'TtlCrrctdRjctns', Max20PositiveNumber, False)

	@TtlCrrctdRjctns.deleter
	def TtlCrrctdRjctns(self):
		del self._TtlCrrctdRjctns
		self._TtlCrrctdRjctns = base_types.UninitialisedField(self, 'TtlCrrctdRjctns', Max20PositiveNumber, False)

	@property
	def TtlNbOfTxs(self):
		return self._TtlNbOfTxs

	@TtlNbOfTxs.setter
	def TtlNbOfTxs(self, value):
		self._TtlNbOfTxs = value if value is not None else base_types.UninitialisedField(self, 'TtlNbOfTxs', Max20PositiveNumber, False)

	@TtlNbOfTxs.deleter
	def TtlNbOfTxs(self):
		del self._TtlNbOfTxs
		self._TtlNbOfTxs = base_types.UninitialisedField(self, 'TtlNbOfTxs', Max20PositiveNumber, False)

	@property
	def TtlNbOfTxsAccptd(self):
		return self._TtlNbOfTxsAccptd

	@TtlNbOfTxsAccptd.setter
	def TtlNbOfTxsAccptd(self, value):
		self._TtlNbOfTxsAccptd = value if value is not None else base_types.UninitialisedField(self, 'TtlNbOfTxsAccptd', Max20PositiveNumber, False)

	@TtlNbOfTxsAccptd.deleter
	def TtlNbOfTxsAccptd(self):
		del self._TtlNbOfTxsAccptd
		self._TtlNbOfTxsAccptd = base_types.UninitialisedField(self, 'TtlNbOfTxsAccptd', Max20PositiveNumber, False)

	@property
	def TtlNbOfTxsRjctd(self):
		return self._TtlNbOfTxsRjctd

	@TtlNbOfTxsRjctd.setter
	def TtlNbOfTxsRjctd(self, value):
		self._TtlNbOfTxsRjctd = value if value is not None else base_types.UninitialisedField(self, 'TtlNbOfTxsRjctd', Max20PositiveNumber, False)

	@TtlNbOfTxsRjctd.deleter
	def TtlNbOfTxsRjctd(self):
		del self._TtlNbOfTxsRjctd
		self._TtlNbOfTxsRjctd = base_types.UninitialisedField(self, 'TtlNbOfTxsRjctd', Max20PositiveNumber, False)

	@property
	def TxsRjctnsRsn(self):
		return self._TxsRjctnsRsn

	@TxsRjctnsRsn.setter
	def TxsRjctnsRsn(self, value):
		self._TxsRjctnsRsn = value if value is not None else base_types.UninitialisedField(self, 'TxsRjctnsRsn', RejectionReason71, True)

	@TxsRjctnsRsn.deleter
	def TxsRjctnsRsn(self):
		del self._TxsRjctnsRsn
		self._TxsRjctnsRsn = base_types.UninitialisedField(self, 'TxsRjctnsRsn', RejectionReason71, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='TtlCrrctdRjctns', type=Max20PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNbOfTxs', type=Max20PositiveNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNbOfTxsAccptd', type=Max20PositiveNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNbOfTxsRjctd', type=Max20PositiveNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxsRjctnsRsn', type=RejectionReason71, min=0, max=None, mutex_group=None, array=True),
	))