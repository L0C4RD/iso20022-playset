from . import base_types
from ._SecuritiesAccount19 import SecuritiesAccount19
from ._StatusAndReason52 import StatusAndReason52
from ._SystemPartyIdentification8 import SystemPartyIdentification8
from ._Transaction169 import Transaction169

class SecuritiesSettlementTransactions6(base_types._BaseFieldType):

	__slots__ = ["_AcctOwnr", "_SfkpgAcct", "_StsAndRsn", "_Tx"]
	@property
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if type(value) != base_types.auto else self.make_default("AcctOwnr")

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = None

	@property
	def SfkpgAcct(self):
		return self._SfkpgAcct

	@SfkpgAcct.setter
	def SfkpgAcct(self, value):
		self._SfkpgAcct = value if type(value) != base_types.auto else self.make_default("SfkpgAcct")

	@SfkpgAcct.deleter
	def SfkpgAcct(self):
		del self._SfkpgAcct
		self._SfkpgAcct = None

	@property
	def StsAndRsn(self):
		return self._StsAndRsn

	@StsAndRsn.setter
	def StsAndRsn(self, value):
		self._StsAndRsn = value if type(value) != base_types.auto else self.make_default("StsAndRsn")

	@StsAndRsn.deleter
	def StsAndRsn(self):
		del self._StsAndRsn
		self._StsAndRsn = None

	@property
	def Tx(self):
		return self._Tx

	@Tx.setter
	def Tx(self, value):
		self._Tx = value if type(value) != base_types.auto else self.make_default("Tx")

	@Tx.deleter
	def Tx(self):
		del self._Tx
		self._Tx = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctOwnr', type=SystemPartyIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgAcct', type=SecuritiesAccount19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsAndRsn', type=StatusAndReason52, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tx', type=Transaction169, min=1, max=None, mutex_group=None, array=True),
	))

