import base_types
import Max35Text
import TransactionIdentifier3
import Max70Text
import CurrencyAndAmount
import FailureReason8Code

class ATMTransaction40(base_types._BaseFieldType):

	__slots__ = ["_Xcptn", "_TxId", "_RcncltnId", "_XcptnDtl", "_ElctrncPrsBal"]
	@property
	def Xcptn(self):
		return self._Xcptn

	@Xcptn.setter
	def Xcptn(self, value):
		self._Xcptn = value if type(value) != auto else self.make_default("Xcptn")

	@Xcptn.deleter
	def Xcptn(self):
		del self._Xcptn
		self._Xcptn = None

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if type(value) != auto else self.make_default("TxId")

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = None

	@property
	def RcncltnId(self):
		return self._RcncltnId

	@RcncltnId.setter
	def RcncltnId(self, value):
		self._RcncltnId = value if type(value) != auto else self.make_default("RcncltnId")

	@RcncltnId.deleter
	def RcncltnId(self):
		del self._RcncltnId
		self._RcncltnId = None

	@property
	def XcptnDtl(self):
		return self._XcptnDtl

	@XcptnDtl.setter
	def XcptnDtl(self, value):
		self._XcptnDtl = value if type(value) != auto else self.make_default("XcptnDtl")

	@XcptnDtl.deleter
	def XcptnDtl(self):
		del self._XcptnDtl
		self._XcptnDtl = None

	@property
	def ElctrncPrsBal(self):
		return self._ElctrncPrsBal

	@ElctrncPrsBal.setter
	def ElctrncPrsBal(self, value):
		self._ElctrncPrsBal = value if type(value) != auto else self.make_default("ElctrncPrsBal")

	@ElctrncPrsBal.deleter
	def ElctrncPrsBal(self):
		del self._ElctrncPrsBal
		self._ElctrncPrsBal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Xcptn', type=FailureReason8Code, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxId', type=TransactionIdentifier3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XcptnDtl', type=Max70Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ElctrncPrsBal', type=CurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))

