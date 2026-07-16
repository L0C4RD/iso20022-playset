# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMTransactionStatus1Code
from . import AuthorisationResult20
from . import FailureReason9Code
from . import Max10000Binary
from . import Max35Text
from . import Max70Text
from . import TransactionIdentifier3
from . import TrueFalseIndicator

class ATMTransaction47(base_types._BaseFieldType):

	__slots__ = ["_AuthstnRslt", "_CstmrCnsnt", "_ICCRltdData", "_Incdnt", "_IncdntDtl", "_RcncltnId", "_RctPrtd", "_ReqdRct", "_TxId", "_TxSts"]
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
	def CstmrCnsnt(self):
		return self._CstmrCnsnt

	@CstmrCnsnt.setter
	def CstmrCnsnt(self, value):
		self._CstmrCnsnt = value if value is not None else base_types.UninitialisedField(self, 'CstmrCnsnt', TrueFalseIndicator, False)

	@CstmrCnsnt.deleter
	def CstmrCnsnt(self):
		del self._CstmrCnsnt
		self._CstmrCnsnt = base_types.UninitialisedField(self, 'CstmrCnsnt', TrueFalseIndicator, False)

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
	def Incdnt(self):
		return self._Incdnt

	@Incdnt.setter
	def Incdnt(self, value):
		self._Incdnt = value if value is not None else base_types.UninitialisedField(self, 'Incdnt', FailureReason9Code, True)

	@Incdnt.deleter
	def Incdnt(self):
		del self._Incdnt
		self._Incdnt = base_types.UninitialisedField(self, 'Incdnt', FailureReason9Code, True)

	@property
	def IncdntDtl(self):
		return self._IncdntDtl

	@IncdntDtl.setter
	def IncdntDtl(self, value):
		self._IncdntDtl = value if value is not None else base_types.UninitialisedField(self, 'IncdntDtl', Max70Text, True)

	@IncdntDtl.deleter
	def IncdntDtl(self):
		del self._IncdntDtl
		self._IncdntDtl = base_types.UninitialisedField(self, 'IncdntDtl', Max70Text, True)

	@property
	def RcncltnId(self):
		return self._RcncltnId

	@RcncltnId.setter
	def RcncltnId(self, value):
		self._RcncltnId = value if value is not None else base_types.UninitialisedField(self, 'RcncltnId', Max35Text, False)

	@RcncltnId.deleter
	def RcncltnId(self):
		del self._RcncltnId
		self._RcncltnId = base_types.UninitialisedField(self, 'RcncltnId', Max35Text, False)

	@property
	def RctPrtd(self):
		return self._RctPrtd

	@RctPrtd.setter
	def RctPrtd(self, value):
		self._RctPrtd = value if value is not None else base_types.UninitialisedField(self, 'RctPrtd', TrueFalseIndicator, False)

	@RctPrtd.deleter
	def RctPrtd(self):
		del self._RctPrtd
		self._RctPrtd = base_types.UninitialisedField(self, 'RctPrtd', TrueFalseIndicator, False)

	@property
	def ReqdRct(self):
		return self._ReqdRct

	@ReqdRct.setter
	def ReqdRct(self, value):
		self._ReqdRct = value if value is not None else base_types.UninitialisedField(self, 'ReqdRct', TrueFalseIndicator, False)

	@ReqdRct.deleter
	def ReqdRct(self):
		del self._ReqdRct
		self._ReqdRct = base_types.UninitialisedField(self, 'ReqdRct', TrueFalseIndicator, False)

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
	def TxSts(self):
		return self._TxSts

	@TxSts.setter
	def TxSts(self, value):
		self._TxSts = value if value is not None else base_types.UninitialisedField(self, 'TxSts', ATMTransactionStatus1Code, False)

	@TxSts.deleter
	def TxSts(self):
		del self._TxSts
		self._TxSts = base_types.UninitialisedField(self, 'TxSts', ATMTransactionStatus1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AuthstnRslt', type=AuthorisationResult20, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrCnsnt', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ICCRltdData', type=Max10000Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Incdnt', type=FailureReason9Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IncdntDtl', type=Max70Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RcncltnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RctPrtd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdRct', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=TransactionIdentifier3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxSts', type=ATMTransactionStatus1Code, min=1, max=1, mutex_group=None, array=False),
	))