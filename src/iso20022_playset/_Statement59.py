# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._DateAndDateTimeChoice import DateAndDateTimeChoice
from ._DatePeriod1Choice import DatePeriod1Choice
from ._Frequency22Choice import Frequency22Choice
from ._FrequencyGranularityType1Code import FrequencyGranularityType1Code
from ._Max35Text import Max35Text
from ._Number3Choice import Number3Choice
from ._SenderBusinessRole1Code import SenderBusinessRole1Code
from ._UpdateType4Choice import UpdateType4Choice
from ._YesNoIndicator import YesNoIndicator

class Statement59(base_types._BaseFieldType):

	__slots__ = ["_ActvtyInd", "_Frqcy", "_FrqcyGrnlrty", "_QryRef", "_SndrBizRole", "_StmtDtTm", "_StmtId", "_StmtNb", "_StmtPrd", "_UpdTp"]
	@property
	def ActvtyInd(self):
		return self._ActvtyInd

	@ActvtyInd.setter
	def ActvtyInd(self, value):
		self._ActvtyInd = value if type(value) != base_types.auto else self.make_default("ActvtyInd")

	@ActvtyInd.deleter
	def ActvtyInd(self):
		del self._ActvtyInd
		self._ActvtyInd = None

	@property
	def Frqcy(self):
		return self._Frqcy

	@Frqcy.setter
	def Frqcy(self, value):
		self._Frqcy = value if type(value) != base_types.auto else self.make_default("Frqcy")

	@Frqcy.deleter
	def Frqcy(self):
		del self._Frqcy
		self._Frqcy = None

	@property
	def FrqcyGrnlrty(self):
		return self._FrqcyGrnlrty

	@FrqcyGrnlrty.setter
	def FrqcyGrnlrty(self, value):
		self._FrqcyGrnlrty = value if type(value) != base_types.auto else self.make_default("FrqcyGrnlrty")

	@FrqcyGrnlrty.deleter
	def FrqcyGrnlrty(self):
		del self._FrqcyGrnlrty
		self._FrqcyGrnlrty = None

	@property
	def QryRef(self):
		return self._QryRef

	@QryRef.setter
	def QryRef(self, value):
		self._QryRef = value if type(value) != base_types.auto else self.make_default("QryRef")

	@QryRef.deleter
	def QryRef(self):
		del self._QryRef
		self._QryRef = None

	@property
	def SndrBizRole(self):
		return self._SndrBizRole

	@SndrBizRole.setter
	def SndrBizRole(self, value):
		self._SndrBizRole = value if type(value) != base_types.auto else self.make_default("SndrBizRole")

	@SndrBizRole.deleter
	def SndrBizRole(self):
		del self._SndrBizRole
		self._SndrBizRole = None

	@property
	def StmtDtTm(self):
		return self._StmtDtTm

	@StmtDtTm.setter
	def StmtDtTm(self, value):
		self._StmtDtTm = value if type(value) != base_types.auto else self.make_default("StmtDtTm")

	@StmtDtTm.deleter
	def StmtDtTm(self):
		del self._StmtDtTm
		self._StmtDtTm = None

	@property
	def StmtId(self):
		return self._StmtId

	@StmtId.setter
	def StmtId(self, value):
		self._StmtId = value if type(value) != base_types.auto else self.make_default("StmtId")

	@StmtId.deleter
	def StmtId(self):
		del self._StmtId
		self._StmtId = None

	@property
	def StmtNb(self):
		return self._StmtNb

	@StmtNb.setter
	def StmtNb(self, value):
		self._StmtNb = value if type(value) != base_types.auto else self.make_default("StmtNb")

	@StmtNb.deleter
	def StmtNb(self):
		del self._StmtNb
		self._StmtNb = None

	@property
	def StmtPrd(self):
		return self._StmtPrd

	@StmtPrd.setter
	def StmtPrd(self, value):
		self._StmtPrd = value if type(value) != base_types.auto else self.make_default("StmtPrd")

	@StmtPrd.deleter
	def StmtPrd(self):
		del self._StmtPrd
		self._StmtPrd = None

	@property
	def UpdTp(self):
		return self._UpdTp

	@UpdTp.setter
	def UpdTp(self, value):
		self._UpdTp = value if type(value) != base_types.auto else self.make_default("UpdTp")

	@UpdTp.deleter
	def UpdTp(self):
		del self._UpdTp
		self._UpdTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActvtyInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Frqcy', type=Frequency22Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrqcyGrnlrty', type=FrequencyGranularityType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SndrBizRole', type=SenderBusinessRole1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmtDtTm', type=DateAndDateTimeChoice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmtId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmtNb', type=Number3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmtPrd', type=DatePeriod1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UpdTp', type=UpdateType4Choice, min=0, max=1, mutex_group=None, array=False),
	))