# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CardPaymentEnvironment82
from . import CardPaymentTransaction146
from . import Max9NumericText
from . import PaymentContext30
from . import Traceability8

class CardPaymentDataSetTransaction56(base_types._BaseFieldType):

	__slots__ = ["_Cntxt", "_Envt", "_Tracblt", "_Tx", "_TxSeqCntr"]
	@property
	def Cntxt(self):
		return self._Cntxt

	@Cntxt.setter
	def Cntxt(self, value):
		self._Cntxt = value if value is not None else base_types.UninitialisedField(self, 'Cntxt', PaymentContext30, False)

	@Cntxt.deleter
	def Cntxt(self):
		del self._Cntxt
		self._Cntxt = base_types.UninitialisedField(self, 'Cntxt', PaymentContext30, False)

	@property
	def Envt(self):
		return self._Envt

	@Envt.setter
	def Envt(self, value):
		self._Envt = value if value is not None else base_types.UninitialisedField(self, 'Envt', CardPaymentEnvironment82, False)

	@Envt.deleter
	def Envt(self):
		del self._Envt
		self._Envt = base_types.UninitialisedField(self, 'Envt', CardPaymentEnvironment82, False)

	@property
	def Tracblt(self):
		return self._Tracblt

	@Tracblt.setter
	def Tracblt(self, value):
		self._Tracblt = value if value is not None else base_types.UninitialisedField(self, 'Tracblt', Traceability8, True)

	@Tracblt.deleter
	def Tracblt(self):
		del self._Tracblt
		self._Tracblt = base_types.UninitialisedField(self, 'Tracblt', Traceability8, True)

	@property
	def Tx(self):
		return self._Tx

	@Tx.setter
	def Tx(self, value):
		self._Tx = value if value is not None else base_types.UninitialisedField(self, 'Tx', CardPaymentTransaction146, False)

	@Tx.deleter
	def Tx(self):
		del self._Tx
		self._Tx = base_types.UninitialisedField(self, 'Tx', CardPaymentTransaction146, False)

	@property
	def TxSeqCntr(self):
		return self._TxSeqCntr

	@TxSeqCntr.setter
	def TxSeqCntr(self, value):
		self._TxSeqCntr = value if value is not None else base_types.UninitialisedField(self, 'TxSeqCntr', Max9NumericText, False)

	@TxSeqCntr.deleter
	def TxSeqCntr(self):
		del self._TxSeqCntr
		self._TxSeqCntr = base_types.UninitialisedField(self, 'TxSeqCntr', Max9NumericText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cntxt', type=PaymentContext30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Envt', type=CardPaymentEnvironment82, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tracblt', type=Traceability8, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tx', type=CardPaymentTransaction146, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxSeqCntr', type=Max9NumericText, min=1, max=1, mutex_group=None, array=False),
	))