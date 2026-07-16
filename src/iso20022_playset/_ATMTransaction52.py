# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMCassette3
from . import ATMCommand7
from . import ATMOperation2Code
from . import ATMTotals4
from . import Max35Text
from . import ResponseType12
from . import TransactionIdentifier3

class ATMTransaction52(base_types._BaseFieldType):

	__slots__ = ["_ATMTtls", "_Cmd", "_Csstt", "_RcncltnId", "_TpOfOpr", "_TxId", "_TxRspn"]
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
		base_types.FieldEntry(name='ATMTtls', type=ATMTotals4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Cmd', type=ATMCommand7, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Csstt', type=ATMCassette3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RcncltnId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TpOfOpr', type=ATMOperation2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=TransactionIdentifier3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxRspn', type=ResponseType12, min=1, max=1, mutex_group=None, array=False),
	))