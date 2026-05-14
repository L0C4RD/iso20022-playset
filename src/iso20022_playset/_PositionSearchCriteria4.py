# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CountryCode import CountryCode
from ._OtherParties46 import OtherParties46
from ._PartyIdentification136 import PartyIdentification136
from ._SecuritiesAccount2Choice import SecuritiesAccount2Choice
from ._SecuritiesBalanceType7Choice import SecuritiesBalanceType7Choice
from ._SecurityIdentification19 import SecurityIdentification19
from ._TrueFalseIndicator import TrueFalseIndicator

class PositionSearchCriteria4(base_types._BaseFieldType):

	__slots__ = ["_AcctOwnr", "_AcctSvcr", "_CtryOfIsse", "_FinInstrm", "_OthrBizPties", "_RtrZeroPos", "_SfkpgAcct", "_SubBalTp"]
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
	def AcctSvcr(self):
		return self._AcctSvcr

	@AcctSvcr.setter
	def AcctSvcr(self, value):
		self._AcctSvcr = value if type(value) != base_types.auto else self.make_default("AcctSvcr")

	@AcctSvcr.deleter
	def AcctSvcr(self):
		del self._AcctSvcr
		self._AcctSvcr = None

	@property
	def CtryOfIsse(self):
		return self._CtryOfIsse

	@CtryOfIsse.setter
	def CtryOfIsse(self, value):
		self._CtryOfIsse = value if type(value) != base_types.auto else self.make_default("CtryOfIsse")

	@CtryOfIsse.deleter
	def CtryOfIsse(self):
		del self._CtryOfIsse
		self._CtryOfIsse = None

	@property
	def FinInstrm(self):
		return self._FinInstrm

	@FinInstrm.setter
	def FinInstrm(self, value):
		self._FinInstrm = value if type(value) != base_types.auto else self.make_default("FinInstrm")

	@FinInstrm.deleter
	def FinInstrm(self):
		del self._FinInstrm
		self._FinInstrm = None

	@property
	def OthrBizPties(self):
		return self._OthrBizPties

	@OthrBizPties.setter
	def OthrBizPties(self, value):
		self._OthrBizPties = value if type(value) != base_types.auto else self.make_default("OthrBizPties")

	@OthrBizPties.deleter
	def OthrBizPties(self):
		del self._OthrBizPties
		self._OthrBizPties = None

	@property
	def RtrZeroPos(self):
		return self._RtrZeroPos

	@RtrZeroPos.setter
	def RtrZeroPos(self, value):
		self._RtrZeroPos = value if type(value) != base_types.auto else self.make_default("RtrZeroPos")

	@RtrZeroPos.deleter
	def RtrZeroPos(self):
		del self._RtrZeroPos
		self._RtrZeroPos = None

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
	def SubBalTp(self):
		return self._SubBalTp

	@SubBalTp.setter
	def SubBalTp(self, value):
		self._SubBalTp = value if type(value) != base_types.auto else self.make_default("SubBalTp")

	@SubBalTp.deleter
	def SubBalTp(self):
		del self._SubBalTp
		self._SubBalTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification136, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSvcr', type=PartyIdentification136, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryOfIsse', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrm', type=SecurityIdentification19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrBizPties', type=OtherParties46, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrZeroPos', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgAcct', type=SecuritiesAccount2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubBalTp', type=SecuritiesBalanceType7Choice, min=0, max=1, mutex_group=None, array=False),
	))