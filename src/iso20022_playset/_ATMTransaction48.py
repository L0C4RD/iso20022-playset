# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMAccountStatement3
from . import ATMCommand7
from . import ATMCustomerProfile7
from . import Action7
from . import AuthorisationResult20
from . import CardAccount18
from . import CurrencyConversion33
from . import CurrencyConversion5
from . import Max10000Binary
from . import ResponseType12
from . import TransactionIdentifier3

class ATMTransaction48(base_types._BaseFieldType):

	__slots__ = ["_AcctInf", "_AcctStmtData", "_Actn", "_AuthstnRslt", "_CcyConvs", "_CcyXchg", "_Cmd", "_CstmrSvcPrfl", "_ICCRltdData", "_TxId", "_TxRspn"]
	@property
	def AcctInf(self):
		return self._AcctInf

	@AcctInf.setter
	def AcctInf(self, value):
		self._AcctInf = value if value is not None else base_types.UninitialisedField(self, 'AcctInf', CardAccount18, True)

	@AcctInf.deleter
	def AcctInf(self):
		del self._AcctInf
		self._AcctInf = base_types.UninitialisedField(self, 'AcctInf', CardAccount18, True)

	@property
	def AcctStmtData(self):
		return self._AcctStmtData

	@AcctStmtData.setter
	def AcctStmtData(self, value):
		self._AcctStmtData = value if value is not None else base_types.UninitialisedField(self, 'AcctStmtData', ATMAccountStatement3, True)

	@AcctStmtData.deleter
	def AcctStmtData(self):
		del self._AcctStmtData
		self._AcctStmtData = base_types.UninitialisedField(self, 'AcctStmtData', ATMAccountStatement3, True)

	@property
	def Actn(self):
		return self._Actn

	@Actn.setter
	def Actn(self, value):
		self._Actn = value if value is not None else base_types.UninitialisedField(self, 'Actn', Action7, True)

	@Actn.deleter
	def Actn(self):
		del self._Actn
		self._Actn = base_types.UninitialisedField(self, 'Actn', Action7, True)

	@property
	def AuthstnRslt(self):
		return self._AuthstnRslt

	@AuthstnRslt.setter
	def AuthstnRslt(self, value):
		self._AuthstnRslt = value if value is not None else base_types.UninitialisedField(self, 'AuthstnRslt', AuthorisationResult20, False)

	@AuthstnRslt.deleter
	def AuthstnRslt(self):
		del self._AuthstnRslt
		self._AuthstnRslt = base_types.UninitialisedField(self, 'AuthstnRslt', AuthorisationResult20, False)

	@property
	def CcyConvs(self):
		return self._CcyConvs

	@CcyConvs.setter
	def CcyConvs(self, value):
		self._CcyConvs = value if value is not None else base_types.UninitialisedField(self, 'CcyConvs', CurrencyConversion33, False)

	@CcyConvs.deleter
	def CcyConvs(self):
		del self._CcyConvs
		self._CcyConvs = base_types.UninitialisedField(self, 'CcyConvs', CurrencyConversion33, False)

	@property
	def CcyXchg(self):
		return self._CcyXchg

	@CcyXchg.setter
	def CcyXchg(self, value):
		self._CcyXchg = value if value is not None else base_types.UninitialisedField(self, 'CcyXchg', CurrencyConversion5, False)

	@CcyXchg.deleter
	def CcyXchg(self):
		del self._CcyXchg
		self._CcyXchg = base_types.UninitialisedField(self, 'CcyXchg', CurrencyConversion5, False)

	@property
	def Cmd(self):
		return self._Cmd

	@Cmd.setter
	def Cmd(self, value):
		self._Cmd = value if value is not None else base_types.UninitialisedField(self, 'Cmd', ATMCommand7, True)

	@Cmd.deleter
	def Cmd(self):
		del self._Cmd
		self._Cmd = base_types.UninitialisedField(self, 'Cmd', ATMCommand7, True)

	@property
	def CstmrSvcPrfl(self):
		return self._CstmrSvcPrfl

	@CstmrSvcPrfl.setter
	def CstmrSvcPrfl(self, value):
		self._CstmrSvcPrfl = value if value is not None else base_types.UninitialisedField(self, 'CstmrSvcPrfl', ATMCustomerProfile7, False)

	@CstmrSvcPrfl.deleter
	def CstmrSvcPrfl(self):
		del self._CstmrSvcPrfl
		self._CstmrSvcPrfl = base_types.UninitialisedField(self, 'CstmrSvcPrfl', ATMCustomerProfile7, False)

	@property
	def ICCRltdData(self):
		return self._ICCRltdData

	@ICCRltdData.setter
	def ICCRltdData(self, value):
		self._ICCRltdData = value if value is not None else base_types.UninitialisedField(self, 'ICCRltdData', Max10000Binary, False)

	@ICCRltdData.deleter
	def ICCRltdData(self):
		del self._ICCRltdData
		self._ICCRltdData = base_types.UninitialisedField(self, 'ICCRltdData', Max10000Binary, False)

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if value is not None else base_types.UninitialisedField(self, 'TxId', TransactionIdentifier3, False)

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = base_types.UninitialisedField(self, 'TxId', TransactionIdentifier3, False)

	@property
	def TxRspn(self):
		return self._TxRspn

	@TxRspn.setter
	def TxRspn(self, value):
		self._TxRspn = value if value is not None else base_types.UninitialisedField(self, 'TxRspn', ResponseType12, False)

	@TxRspn.deleter
	def TxRspn(self):
		del self._TxRspn
		self._TxRspn = base_types.UninitialisedField(self, 'TxRspn', ResponseType12, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctInf', type=CardAccount18, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctStmtData', type=ATMAccountStatement3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Actn', type=Action7, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AuthstnRslt', type=AuthorisationResult20, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CcyConvs', type=CurrencyConversion33, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CcyXchg', type=CurrencyConversion5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cmd', type=ATMCommand7, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CstmrSvcPrfl', type=ATMCustomerProfile7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ICCRltdData', type=Max10000Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=TransactionIdentifier3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxRspn', type=ResponseType12, min=1, max=1, mutex_group=None, array=False),
	))