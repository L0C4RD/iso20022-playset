import base_types
import TrackerStatus1
import TrackerPaymentTransaction14

class TrackerStatusAndTransaction19(base_types._BaseFieldType):

	__slots__ = ["_Tx", "_TxSts"]
	@property
	def Tx(self):
		return self._Tx

	@Tx.setter
	def Tx(self, value):
		self._Tx = value if type(value) != auto else self.make_default("Tx")

	@Tx.deleter
	def Tx(self):
		del self._Tx
		self._Tx = None

	@property
	def TxSts(self):
		return self._TxSts

	@TxSts.setter
	def TxSts(self, value):
		self._TxSts = value if type(value) != auto else self.make_default("TxSts")

	@TxSts.deleter
	def TxSts(self):
		del self._TxSts
		self._TxSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tx', type=TrackerPaymentTransaction14, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxSts', type=TrackerStatus1, min=1, max=1, mutex_group=None, array=False),
	))

