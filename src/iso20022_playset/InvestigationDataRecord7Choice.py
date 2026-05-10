import base_types
import BookingConfirmation5
import PaymentTransactionStatus1
import Max500Text
import CompensationResponse1
import TransactionAmendment1
import DebitAuthorisationConfirmation3
import AdjustmentCompensation1

class InvestigationDataRecord7Choice(base_types._BaseFieldType):

	__slots__ = ["_RspnNrrtv", "_TxData", "_TxSts", "_Valtn", "_Conf", "_Compstn", "_DbtAuthstn"]
	@property
	def RspnNrrtv(self):
		return self._RspnNrrtv

	@RspnNrrtv.setter
	def RspnNrrtv(self, value):
		self._RspnNrrtv = value if type(value) != auto else self.make_default("RspnNrrtv")

	@RspnNrrtv.deleter
	def RspnNrrtv(self):
		del self._RspnNrrtv
		self._RspnNrrtv = None

	@property
	def TxData(self):
		return self._TxData

	@TxData.setter
	def TxData(self, value):
		self._TxData = value if type(value) != auto else self.make_default("TxData")

	@TxData.deleter
	def TxData(self):
		del self._TxData
		self._TxData = None

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

	@property
	def Valtn(self):
		return self._Valtn

	@Valtn.setter
	def Valtn(self, value):
		self._Valtn = value if type(value) != auto else self.make_default("Valtn")

	@Valtn.deleter
	def Valtn(self):
		del self._Valtn
		self._Valtn = None

	@property
	def Conf(self):
		return self._Conf

	@Conf.setter
	def Conf(self, value):
		self._Conf = value if type(value) != auto else self.make_default("Conf")

	@Conf.deleter
	def Conf(self):
		del self._Conf
		self._Conf = None

	@property
	def Compstn(self):
		return self._Compstn

	@Compstn.setter
	def Compstn(self, value):
		self._Compstn = value if type(value) != auto else self.make_default("Compstn")

	@Compstn.deleter
	def Compstn(self):
		del self._Compstn
		self._Compstn = None

	@property
	def DbtAuthstn(self):
		return self._DbtAuthstn

	@DbtAuthstn.setter
	def DbtAuthstn(self, value):
		self._DbtAuthstn = value if type(value) != auto else self.make_default("DbtAuthstn")

	@DbtAuthstn.deleter
	def DbtAuthstn(self):
		del self._DbtAuthstn
		self._DbtAuthstn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RspnNrrtv', type=Max500Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TxData', type=TransactionAmendment1, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='TxSts', type=PaymentTransactionStatus1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Valtn', type=AdjustmentCompensation1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Conf', type=BookingConfirmation5, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Compstn', type=CompensationResponse1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DbtAuthstn', type=DebitAuthorisationConfirmation3, min=0, max=1, mutex_group=1, array=False),
	))

