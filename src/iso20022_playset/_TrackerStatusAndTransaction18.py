# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import TrackerPaymentTransaction14
from . import TrackerStatus4

class TrackerStatusAndTransaction18(base_types._BaseFieldType):

	__slots__ = ["_Tx", "_TxSts"]
	@property
	def Tx(self):
		return self._Tx

	@Tx.setter
	def Tx(self, value):
		self._Tx = value if value is not None else base_types.UninitialisedField(self, 'Tx', TrackerPaymentTransaction14, True)

	@Tx.deleter
	def Tx(self):
		del self._Tx
		self._Tx = base_types.UninitialisedField(self, 'Tx', TrackerPaymentTransaction14, True)

	@property
	def TxSts(self):
		return self._TxSts

	@TxSts.setter
	def TxSts(self, value):
		self._TxSts = value if value is not None else base_types.UninitialisedField(self, 'TxSts', TrackerStatus4, False)

	@TxSts.deleter
	def TxSts(self):
		del self._TxSts
		self._TxSts = base_types.UninitialisedField(self, 'TxSts', TrackerStatus4, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tx', type=TrackerPaymentTransaction14, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxSts', type=TrackerStatus4, min=1, max=1, mutex_group=None, array=False),
	))