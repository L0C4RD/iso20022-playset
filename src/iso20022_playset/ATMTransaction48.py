import base_types
import TransactionIdentifier3
import AuthorisationResult20
import Max10000Binary
import CurrencyConversion33
import CurrencyConversion5
import ResponseType12
import Action7
import ATMCommand7
import CardAccount18
import ATMCustomerProfile7
import ATMAccountStatement3

class ATMTransaction48(base_types._BaseFieldType):

	__slots__ = ["_Actn", "_CcyConvs", "_Cmd", "_TxRspn", "_ICCRltdData", "_AcctInf", "_TxId", "_AuthstnRslt", "_CstmrSvcPrfl", "_CcyXchg", "_AcctStmtData"]
	@property
	def Actn(self):
		return self._Actn

	@Actn.setter
	def Actn(self, value):
		self._Actn = value if type(value) != auto else self.make_default("Actn")

	@Actn.deleter
	def Actn(self):
		del self._Actn
		self._Actn = None

	@property
	def CcyConvs(self):
		return self._CcyConvs

	@CcyConvs.setter
	def CcyConvs(self, value):
		self._CcyConvs = value if type(value) != auto else self.make_default("CcyConvs")

	@CcyConvs.deleter
	def CcyConvs(self):
		del self._CcyConvs
		self._CcyConvs = None

	@property
	def Cmd(self):
		return self._Cmd

	@Cmd.setter
	def Cmd(self, value):
		self._Cmd = value if type(value) != auto else self.make_default("Cmd")

	@Cmd.deleter
	def Cmd(self):
		del self._Cmd
		self._Cmd = None

	@property
	def TxRspn(self):
		return self._TxRspn

	@TxRspn.setter
	def TxRspn(self, value):
		self._TxRspn = value if type(value) != auto else self.make_default("TxRspn")

	@TxRspn.deleter
	def TxRspn(self):
		del self._TxRspn
		self._TxRspn = None

	@property
	def ICCRltdData(self):
		return self._ICCRltdData

	@ICCRltdData.setter
	def ICCRltdData(self, value):
		self._ICCRltdData = value if type(value) != auto else self.make_default("ICCRltdData")

	@ICCRltdData.deleter
	def ICCRltdData(self):
		del self._ICCRltdData
		self._ICCRltdData = None

	@property
	def AcctInf(self):
		return self._AcctInf

	@AcctInf.setter
	def AcctInf(self, value):
		self._AcctInf = value if type(value) != auto else self.make_default("AcctInf")

	@AcctInf.deleter
	def AcctInf(self):
		del self._AcctInf
		self._AcctInf = None

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
	def AuthstnRslt(self):
		return self._AuthstnRslt

	@AuthstnRslt.setter
	def AuthstnRslt(self, value):
		self._AuthstnRslt = value if type(value) != auto else self.make_default("AuthstnRslt")

	@AuthstnRslt.deleter
	def AuthstnRslt(self):
		del self._AuthstnRslt
		self._AuthstnRslt = None

	@property
	def CstmrSvcPrfl(self):
		return self._CstmrSvcPrfl

	@CstmrSvcPrfl.setter
	def CstmrSvcPrfl(self, value):
		self._CstmrSvcPrfl = value if type(value) != auto else self.make_default("CstmrSvcPrfl")

	@CstmrSvcPrfl.deleter
	def CstmrSvcPrfl(self):
		del self._CstmrSvcPrfl
		self._CstmrSvcPrfl = None

	@property
	def CcyXchg(self):
		return self._CcyXchg

	@CcyXchg.setter
	def CcyXchg(self, value):
		self._CcyXchg = value if type(value) != auto else self.make_default("CcyXchg")

	@CcyXchg.deleter
	def CcyXchg(self):
		del self._CcyXchg
		self._CcyXchg = None

	@property
	def AcctStmtData(self):
		return self._AcctStmtData

	@AcctStmtData.setter
	def AcctStmtData(self, value):
		self._AcctStmtData = value if type(value) != auto else self.make_default("AcctStmtData")

	@AcctStmtData.deleter
	def AcctStmtData(self):
		del self._AcctStmtData
		self._AcctStmtData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Actn', type=Action7, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CcyConvs', type=CurrencyConversion33, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cmd', type=ATMCommand7, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxRspn', type=ResponseType12, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ICCRltdData', type=Max10000Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctInf', type=CardAccount18, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxId', type=TransactionIdentifier3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthstnRslt', type=AuthorisationResult20, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrSvcPrfl', type=ATMCustomerProfile7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CcyXchg', type=CurrencyConversion5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctStmtData', type=ATMAccountStatement3, min=0, max=None, mutex_group=None, array=True),
	))

