# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CountryCode import CountryCode
from ._DateAndDateTimeSearch5Choice import DateAndDateTimeSearch5Choice
from ._GenericIdentification37 import GenericIdentification37
from ._IntraPositionQueryStatus3 import IntraPositionQueryStatus3
from ._IntraPositionType2 import IntraPositionType2
from ._PriorityNumeric4Choice import PriorityNumeric4Choice
from ._QuantitySearch2Choice import QuantitySearch2Choice
from ._References82Choice import References82Choice
from ._SecuritiesAccount19 import SecuritiesAccount19
from ._SecurityIdentification19 import SecurityIdentification19
from ._SystemPartyIdentification8 import SystemPartyIdentification8

class IntraPositionQueryCriteria8(base_types._BaseFieldType):

	__slots__ = ["_BalTp", "_CreDtTm", "_CtryOfIsse", "_FctvSttlmDt", "_FinInstrmId", "_IntnddSttlmDt", "_MsgOrgtr", "_Prty", "_Refs", "_SctiesSubBalId", "_SfkpgAcct", "_SfkpgAcctOwnr", "_Sts", "_SttldQty", "_SttlmQty"]
	@property
	def BalTp(self):
		return self._BalTp

	@BalTp.setter
	def BalTp(self, value):
		self._BalTp = value if type(value) != base_types.auto else self.make_default("BalTp")

	@BalTp.deleter
	def BalTp(self):
		del self._BalTp
		self._BalTp = None

	@property
	def CreDtTm(self):
		return self._CreDtTm

	@CreDtTm.setter
	def CreDtTm(self, value):
		self._CreDtTm = value if type(value) != base_types.auto else self.make_default("CreDtTm")

	@CreDtTm.deleter
	def CreDtTm(self):
		del self._CreDtTm
		self._CreDtTm = None

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
	def FctvSttlmDt(self):
		return self._FctvSttlmDt

	@FctvSttlmDt.setter
	def FctvSttlmDt(self, value):
		self._FctvSttlmDt = value if type(value) != base_types.auto else self.make_default("FctvSttlmDt")

	@FctvSttlmDt.deleter
	def FctvSttlmDt(self):
		del self._FctvSttlmDt
		self._FctvSttlmDt = None

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if type(value) != base_types.auto else self.make_default("FinInstrmId")

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = None

	@property
	def IntnddSttlmDt(self):
		return self._IntnddSttlmDt

	@IntnddSttlmDt.setter
	def IntnddSttlmDt(self, value):
		self._IntnddSttlmDt = value if type(value) != base_types.auto else self.make_default("IntnddSttlmDt")

	@IntnddSttlmDt.deleter
	def IntnddSttlmDt(self):
		del self._IntnddSttlmDt
		self._IntnddSttlmDt = None

	@property
	def MsgOrgtr(self):
		return self._MsgOrgtr

	@MsgOrgtr.setter
	def MsgOrgtr(self, value):
		self._MsgOrgtr = value if type(value) != base_types.auto else self.make_default("MsgOrgtr")

	@MsgOrgtr.deleter
	def MsgOrgtr(self):
		del self._MsgOrgtr
		self._MsgOrgtr = None

	@property
	def Prty(self):
		return self._Prty

	@Prty.setter
	def Prty(self, value):
		self._Prty = value if type(value) != base_types.auto else self.make_default("Prty")

	@Prty.deleter
	def Prty(self):
		del self._Prty
		self._Prty = None

	@property
	def Refs(self):
		return self._Refs

	@Refs.setter
	def Refs(self, value):
		self._Refs = value if type(value) != base_types.auto else self.make_default("Refs")

	@Refs.deleter
	def Refs(self):
		del self._Refs
		self._Refs = None

	@property
	def SctiesSubBalId(self):
		return self._SctiesSubBalId

	@SctiesSubBalId.setter
	def SctiesSubBalId(self, value):
		self._SctiesSubBalId = value if type(value) != base_types.auto else self.make_default("SctiesSubBalId")

	@SctiesSubBalId.deleter
	def SctiesSubBalId(self):
		del self._SctiesSubBalId
		self._SctiesSubBalId = None

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
	def SfkpgAcctOwnr(self):
		return self._SfkpgAcctOwnr

	@SfkpgAcctOwnr.setter
	def SfkpgAcctOwnr(self, value):
		self._SfkpgAcctOwnr = value if type(value) != base_types.auto else self.make_default("SfkpgAcctOwnr")

	@SfkpgAcctOwnr.deleter
	def SfkpgAcctOwnr(self):
		del self._SfkpgAcctOwnr
		self._SfkpgAcctOwnr = None

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if type(value) != base_types.auto else self.make_default("Sts")

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = None

	@property
	def SttldQty(self):
		return self._SttldQty

	@SttldQty.setter
	def SttldQty(self, value):
		self._SttldQty = value if type(value) != base_types.auto else self.make_default("SttldQty")

	@SttldQty.deleter
	def SttldQty(self):
		del self._SttldQty
		self._SttldQty = None

	@property
	def SttlmQty(self):
		return self._SttlmQty

	@SttlmQty.setter
	def SttlmQty(self, value):
		self._SttlmQty = value if type(value) != base_types.auto else self.make_default("SttlmQty")

	@SttlmQty.deleter
	def SttlmQty(self):
		del self._SttlmQty
		self._SttlmQty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BalTp', type=IntraPositionType2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CreDtTm', type=DateAndDateTimeSearch5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryOfIsse', type=CountryCode, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FctvSttlmDt', type=DateAndDateTimeSearch5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IntnddSttlmDt', type=DateAndDateTimeSearch5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgOrgtr', type=SystemPartyIdentification8, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Prty', type=PriorityNumeric4Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Refs', type=References82Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SctiesSubBalId', type=GenericIdentification37, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SfkpgAcct', type=SecuritiesAccount19, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SfkpgAcctOwnr', type=SystemPartyIdentification8, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sts', type=IntraPositionQueryStatus3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttldQty', type=QuantitySearch2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmQty', type=QuantitySearch2Choice, min=0, max=1, mutex_group=None, array=False),
	))