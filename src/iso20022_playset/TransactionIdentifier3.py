import base_types
import ISODateTime
import Max35Text

class TransactionIdentifier3(base_types._BaseFieldType):

	__slots__ = ["_HstTxDtTm", "_TxRef", "_TxDtTm"]
	@property
	def HstTxDtTm(self):
		return self._HstTxDtTm

	@HstTxDtTm.setter
	def HstTxDtTm(self, value):
		self._HstTxDtTm = value if type(value) != auto else self.make_default("HstTxDtTm")

	@HstTxDtTm.deleter
	def HstTxDtTm(self):
		del self._HstTxDtTm
		self._HstTxDtTm = None

	@property
	def TxRef(self):
		return self._TxRef

	@TxRef.setter
	def TxRef(self, value):
		self._TxRef = value if type(value) != auto else self.make_default("TxRef")

	@TxRef.deleter
	def TxRef(self):
		del self._TxRef
		self._TxRef = None

	@property
	def TxDtTm(self):
		return self._TxDtTm

	@TxDtTm.setter
	def TxDtTm(self, value):
		self._TxDtTm = value if type(value) != auto else self.make_default("TxDtTm")

	@TxDtTm.deleter
	def TxDtTm(self):
		del self._TxDtTm
		self._TxDtTm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='HstTxDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
	))

