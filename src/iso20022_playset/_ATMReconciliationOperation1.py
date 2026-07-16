# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMCassette3
from . import ATMOperation2Code
from . import ATMTotals3
from . import ATMTotals4
from . import FailureReason9Code
from . import Max140Text
from . import Max35Text
from . import Number
from . import TransactionIdentifier3

class ATMReconciliationOperation1(base_types._BaseFieldType):

	__slots__ = ["_ATMTtls", "_AddtlTxInf", "_Csstt", "_Incdnt", "_RcncltnId", "_RtndCard", "_TpOfOpr", "_TxId", "_TxTtls"]
	@property
	def ATMTtls(self):
		return self._ATMTtls

	@ATMTtls.setter
	def ATMTtls(self, value):
		self._ATMTtls = value if value is not None else base_types.UninitialisedField(self, 'ATMTtls', ATMTotals4, True)

	@ATMTtls.deleter
	def ATMTtls(self):
		del self._ATMTtls
		self._ATMTtls = base_types.UninitialisedField(self, 'ATMTtls', ATMTotals4, True)

	@property
	def AddtlTxInf(self):
		return self._AddtlTxInf

	@AddtlTxInf.setter
	def AddtlTxInf(self, value):
		self._AddtlTxInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlTxInf', Max140Text, False)

	@AddtlTxInf.deleter
	def AddtlTxInf(self):
		del self._AddtlTxInf
		self._AddtlTxInf = base_types.UninitialisedField(self, 'AddtlTxInf', Max140Text, False)

	@property
	def Csstt(self):
		return self._Csstt

	@Csstt.setter
	def Csstt(self, value):
		self._Csstt = value if value is not None else base_types.UninitialisedField(self, 'Csstt', ATMCassette3, True)

	@Csstt.deleter
	def Csstt(self):
		del self._Csstt
		self._Csstt = base_types.UninitialisedField(self, 'Csstt', ATMCassette3, True)

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
	def RtndCard(self):
		return self._RtndCard

	@RtndCard.setter
	def RtndCard(self, value):
		self._RtndCard = value if value is not None else base_types.UninitialisedField(self, 'RtndCard', Number, False)

	@RtndCard.deleter
	def RtndCard(self):
		del self._RtndCard
		self._RtndCard = base_types.UninitialisedField(self, 'RtndCard', Number, False)

	@property
	def TpOfOpr(self):
		return self._TpOfOpr

	@TpOfOpr.setter
	def TpOfOpr(self, value):
		self._TpOfOpr = value if value is not None else base_types.UninitialisedField(self, 'TpOfOpr', ATMOperation2Code, False)

	@TpOfOpr.deleter
	def TpOfOpr(self):
		del self._TpOfOpr
		self._TpOfOpr = base_types.UninitialisedField(self, 'TpOfOpr', ATMOperation2Code, False)

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
	def TxTtls(self):
		return self._TxTtls

	@TxTtls.setter
	def TxTtls(self, value):
		self._TxTtls = value if value is not None else base_types.UninitialisedField(self, 'TxTtls', ATMTotals3, True)

	@TxTtls.deleter
	def TxTtls(self):
		del self._TxTtls
		self._TxTtls = base_types.UninitialisedField(self, 'TxTtls', ATMTotals3, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ATMTtls', type=ATMTotals4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlTxInf', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Csstt', type=ATMCassette3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Incdnt', type=FailureReason9Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RcncltnId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtndCard', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TpOfOpr', type=ATMOperation2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=TransactionIdentifier3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTtls', type=ATMTotals3, min=0, max=None, mutex_group=None, array=True),
	))