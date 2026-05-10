from . import base_types
from .TransactionIdentifier3 import TransactionIdentifier3
from .Max10000Binary import Max10000Binary
from .TrueFalseIndicator import TrueFalseIndicator
from .Max35Text import Max35Text
from .FailureReason9Code import FailureReason9Code
from .ATMTransactionStatus1Code import ATMTransactionStatus1Code
from .Max70Text import Max70Text
from .AuthorisationResult20 import AuthorisationResult20

class ATMTransaction47(base_types._BaseFieldType):

	__slots__ = ["_ReqdRct", "_AuthstnRslt", "_RcncltnId", "_CstmrCnsnt", "_ICCRltdData", "_RctPrtd", "_Incdnt", "_TxId", "_TxSts", "_IncdntDtl"]
	@property
	def ReqdRct(self):
		return self._ReqdRct

	@ReqdRct.setter
	def ReqdRct(self, value):
		self._ReqdRct = value if type(value) != base_types.auto else self.make_default("ReqdRct")

	@ReqdRct.deleter
	def ReqdRct(self):
		del self._ReqdRct
		self._ReqdRct = None

	@property
	def AuthstnRslt(self):
		return self._AuthstnRslt

	@AuthstnRslt.setter
	def AuthstnRslt(self, value):
		self._AuthstnRslt = value if type(value) != base_types.auto else self.make_default("AuthstnRslt")

	@AuthstnRslt.deleter
	def AuthstnRslt(self):
		del self._AuthstnRslt
		self._AuthstnRslt = None

	@property
	def RcncltnId(self):
		return self._RcncltnId

	@RcncltnId.setter
	def RcncltnId(self, value):
		self._RcncltnId = value if type(value) != base_types.auto else self.make_default("RcncltnId")

	@RcncltnId.deleter
	def RcncltnId(self):
		del self._RcncltnId
		self._RcncltnId = None

	@property
	def CstmrCnsnt(self):
		return self._CstmrCnsnt

	@CstmrCnsnt.setter
	def CstmrCnsnt(self, value):
		self._CstmrCnsnt = value if type(value) != base_types.auto else self.make_default("CstmrCnsnt")

	@CstmrCnsnt.deleter
	def CstmrCnsnt(self):
		del self._CstmrCnsnt
		self._CstmrCnsnt = None

	@property
	def ICCRltdData(self):
		return self._ICCRltdData

	@ICCRltdData.setter
	def ICCRltdData(self, value):
		self._ICCRltdData = value if type(value) != base_types.auto else self.make_default("ICCRltdData")

	@ICCRltdData.deleter
	def ICCRltdData(self):
		del self._ICCRltdData
		self._ICCRltdData = None

	@property
	def RctPrtd(self):
		return self._RctPrtd

	@RctPrtd.setter
	def RctPrtd(self, value):
		self._RctPrtd = value if type(value) != base_types.auto else self.make_default("RctPrtd")

	@RctPrtd.deleter
	def RctPrtd(self):
		del self._RctPrtd
		self._RctPrtd = None

	@property
	def Incdnt(self):
		return self._Incdnt

	@Incdnt.setter
	def Incdnt(self, value):
		self._Incdnt = value if type(value) != base_types.auto else self.make_default("Incdnt")

	@Incdnt.deleter
	def Incdnt(self):
		del self._Incdnt
		self._Incdnt = None

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if type(value) != base_types.auto else self.make_default("TxId")

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = None

	@property
	def TxSts(self):
		return self._TxSts

	@TxSts.setter
	def TxSts(self, value):
		self._TxSts = value if type(value) != base_types.auto else self.make_default("TxSts")

	@TxSts.deleter
	def TxSts(self):
		del self._TxSts
		self._TxSts = None

	@property
	def IncdntDtl(self):
		return self._IncdntDtl

	@IncdntDtl.setter
	def IncdntDtl(self, value):
		self._IncdntDtl = value if type(value) != base_types.auto else self.make_default("IncdntDtl")

	@IncdntDtl.deleter
	def IncdntDtl(self):
		del self._IncdntDtl
		self._IncdntDtl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ReqdRct', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthstnRslt', type=AuthorisationResult20, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrCnsnt', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ICCRltdData', type=Max10000Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RctPrtd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Incdnt', type=FailureReason9Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxId', type=TransactionIdentifier3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxSts', type=ATMTransactionStatus1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IncdntDtl', type=Max70Text, min=0, max=None, mutex_group=None, array=True),
	))

