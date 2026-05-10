from . import base_types
import LimitType4Code
import AccountIdentification4Choice
import PartyIdentification136
import SystemPartyIdentification8
import ActiveCurrencyCode

class LimitIdentification7(base_types._BaseFieldType):

	__slots__ = ["_Tp", "_BilLmtCtrPtyId", "_LmtCcy", "_AcctOwnr", "_AcctId"]
	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def BilLmtCtrPtyId(self):
		return self._BilLmtCtrPtyId

	@BilLmtCtrPtyId.setter
	def BilLmtCtrPtyId(self, value):
		self._BilLmtCtrPtyId = value if type(value) != auto else self.make_default("BilLmtCtrPtyId")

	@BilLmtCtrPtyId.deleter
	def BilLmtCtrPtyId(self):
		del self._BilLmtCtrPtyId
		self._BilLmtCtrPtyId = None

	@property
	def LmtCcy(self):
		return self._LmtCcy

	@LmtCcy.setter
	def LmtCcy(self, value):
		self._LmtCcy = value if type(value) != auto else self.make_default("LmtCcy")

	@LmtCcy.deleter
	def LmtCcy(self):
		del self._LmtCcy
		self._LmtCcy = None

	@property
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if type(value) != auto else self.make_default("AcctOwnr")

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = None

	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if type(value) != auto else self.make_default("AcctId")

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tp', type=LimitType4Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BilLmtCtrPtyId', type=SystemPartyIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LmtCcy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification136, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctId', type=AccountIdentification4Choice, min=1, max=1, mutex_group=None, array=False),
	))

