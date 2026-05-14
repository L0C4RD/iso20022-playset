# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AccountIdentification4Choice import AccountIdentification4Choice
from ._ActiveCurrencyCode import ActiveCurrencyCode
from ._LimitType4Code import LimitType4Code
from ._PartyIdentification136 import PartyIdentification136
from ._SystemPartyIdentification8 import SystemPartyIdentification8

class LimitIdentification7(base_types._BaseFieldType):

	__slots__ = ["_AcctId", "_AcctOwnr", "_BilLmtCtrPtyId", "_LmtCcy", "_Tp"]
	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if type(value) != base_types.auto else self.make_default("AcctId")

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = None

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
	def BilLmtCtrPtyId(self):
		return self._BilLmtCtrPtyId

	@BilLmtCtrPtyId.setter
	def BilLmtCtrPtyId(self, value):
		self._BilLmtCtrPtyId = value if type(value) != base_types.auto else self.make_default("BilLmtCtrPtyId")

	@BilLmtCtrPtyId.deleter
	def BilLmtCtrPtyId(self):
		del self._BilLmtCtrPtyId
		self._BilLmtCtrPtyId = None

	@property
	def LmtCcy(self):
		return self._LmtCcy

	@LmtCcy.setter
	def LmtCcy(self, value):
		self._LmtCcy = value if type(value) != base_types.auto else self.make_default("LmtCcy")

	@LmtCcy.deleter
	def LmtCcy(self):
		del self._LmtCcy
		self._LmtCcy = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctId', type=AccountIdentification4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification136, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BilLmtCtrPtyId', type=SystemPartyIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LmtCcy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=LimitType4Code, min=1, max=1, mutex_group=None, array=False),
	))