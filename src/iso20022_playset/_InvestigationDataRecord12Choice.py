# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdjustmentCompensation1
from . import BookingConfirmation8
from . import CompensationResponse1
from . import DebitAuthorisationConfirmation3
from . import Max500Text
from . import PaymentTransactionStatus1
from . import TransactionAmendment1

class InvestigationDataRecord12Choice(base_types._BaseFieldType):

	__slots__ = ["_Compstn", "_Conf", "_DbtAuthstn", "_RspnNrrtv", "_TxData", "_TxSts", "_Valtn"]
	@property
	def Compstn(self):
		return self._Compstn

	@Compstn.setter
	def Compstn(self, value):
		self._Compstn = value if value is not None else base_types.UninitialisedField(self, 'Compstn', CompensationResponse1, False)

	@Compstn.deleter
	def Compstn(self):
		del self._Compstn
		self._Compstn = base_types.UninitialisedField(self, 'Compstn', CompensationResponse1, False)

	@property
	def Conf(self):
		return self._Conf

	@Conf.setter
	def Conf(self, value):
		self._Conf = value if value is not None else base_types.UninitialisedField(self, 'Conf', BookingConfirmation8, False)

	@Conf.deleter
	def Conf(self):
		del self._Conf
		self._Conf = base_types.UninitialisedField(self, 'Conf', BookingConfirmation8, False)

	@property
	def DbtAuthstn(self):
		return self._DbtAuthstn

	@DbtAuthstn.setter
	def DbtAuthstn(self, value):
		self._DbtAuthstn = value if value is not None else base_types.UninitialisedField(self, 'DbtAuthstn', DebitAuthorisationConfirmation3, False)

	@DbtAuthstn.deleter
	def DbtAuthstn(self):
		del self._DbtAuthstn
		self._DbtAuthstn = base_types.UninitialisedField(self, 'DbtAuthstn', DebitAuthorisationConfirmation3, False)

	@property
	def RspnNrrtv(self):
		return self._RspnNrrtv

	@RspnNrrtv.setter
	def RspnNrrtv(self, value):
		self._RspnNrrtv = value if value is not None else base_types.UninitialisedField(self, 'RspnNrrtv', Max500Text, False)

	@RspnNrrtv.deleter
	def RspnNrrtv(self):
		del self._RspnNrrtv
		self._RspnNrrtv = base_types.UninitialisedField(self, 'RspnNrrtv', Max500Text, False)

	@property
	def TxData(self):
		return self._TxData

	@TxData.setter
	def TxData(self, value):
		self._TxData = value if value is not None else base_types.UninitialisedField(self, 'TxData', TransactionAmendment1, True)

	@TxData.deleter
	def TxData(self):
		del self._TxData
		self._TxData = base_types.UninitialisedField(self, 'TxData', TransactionAmendment1, True)

	@property
	def TxSts(self):
		return self._TxSts

	@TxSts.setter
	def TxSts(self, value):
		self._TxSts = value if value is not None else base_types.UninitialisedField(self, 'TxSts', PaymentTransactionStatus1, False)

	@TxSts.deleter
	def TxSts(self):
		del self._TxSts
		self._TxSts = base_types.UninitialisedField(self, 'TxSts', PaymentTransactionStatus1, False)

	@property
	def Valtn(self):
		return self._Valtn

	@Valtn.setter
	def Valtn(self, value):
		self._Valtn = value if value is not None else base_types.UninitialisedField(self, 'Valtn', AdjustmentCompensation1, False)

	@Valtn.deleter
	def Valtn(self):
		del self._Valtn
		self._Valtn = base_types.UninitialisedField(self, 'Valtn', AdjustmentCompensation1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Compstn', type=CompensationResponse1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Conf', type=BookingConfirmation8, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DbtAuthstn', type=DebitAuthorisationConfirmation3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RspnNrrtv', type=Max500Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TxData', type=TransactionAmendment1, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='TxSts', type=PaymentTransactionStatus1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Valtn', type=AdjustmentCompensation1, min=0, max=1, mutex_group=1, array=False),
	))