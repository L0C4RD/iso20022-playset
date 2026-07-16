# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateAndDateTimeChoice
from . import DatePeriod1Choice
from . import Frequency22Choice
from . import FrequencyGranularityType1Code
from . import Max35Text
from . import Number3Choice
from . import SenderBusinessRole1Code
from . import UpdateType4Choice
from . import YesNoIndicator

class Statement59(base_types._BaseFieldType):

	__slots__ = ["_ActvtyInd", "_Frqcy", "_FrqcyGrnlrty", "_QryRef", "_SndrBizRole", "_StmtDtTm", "_StmtId", "_StmtNb", "_StmtPrd", "_UpdTp"]
	@property
	def ActvtyInd(self):
		return self._ActvtyInd

	@ActvtyInd.setter
	def ActvtyInd(self, value):
		self._ActvtyInd = value if value is not None else base_types.UninitialisedField(self, 'ActvtyInd', YesNoIndicator, False)

	@ActvtyInd.deleter
	def ActvtyInd(self):
		del self._ActvtyInd
		self._ActvtyInd = base_types.UninitialisedField(self, 'ActvtyInd', YesNoIndicator, False)

	@property
	def Frqcy(self):
		return self._Frqcy

	@Frqcy.setter
	def Frqcy(self, value):
		self._Frqcy = value if value is not None else base_types.UninitialisedField(self, 'Frqcy', Frequency22Choice, False)

	@Frqcy.deleter
	def Frqcy(self):
		del self._Frqcy
		self._Frqcy = base_types.UninitialisedField(self, 'Frqcy', Frequency22Choice, False)

	@property
	def FrqcyGrnlrty(self):
		return self._FrqcyGrnlrty

	@FrqcyGrnlrty.setter
	def FrqcyGrnlrty(self, value):
		self._FrqcyGrnlrty = value if value is not None else base_types.UninitialisedField(self, 'FrqcyGrnlrty', FrequencyGranularityType1Code, False)

	@FrqcyGrnlrty.deleter
	def FrqcyGrnlrty(self):
		del self._FrqcyGrnlrty
		self._FrqcyGrnlrty = base_types.UninitialisedField(self, 'FrqcyGrnlrty', FrequencyGranularityType1Code, False)

	@property
	def QryRef(self):
		return self._QryRef

	@QryRef.setter
	def QryRef(self, value):
		self._QryRef = value if value is not None else base_types.UninitialisedField(self, 'QryRef', Max35Text, False)

	@QryRef.deleter
	def QryRef(self):
		del self._QryRef
		self._QryRef = base_types.UninitialisedField(self, 'QryRef', Max35Text, False)

	@property
	def SndrBizRole(self):
		return self._SndrBizRole

	@SndrBizRole.setter
	def SndrBizRole(self, value):
		self._SndrBizRole = value if value is not None else base_types.UninitialisedField(self, 'SndrBizRole', SenderBusinessRole1Code, False)

	@SndrBizRole.deleter
	def SndrBizRole(self):
		del self._SndrBizRole
		self._SndrBizRole = base_types.UninitialisedField(self, 'SndrBizRole', SenderBusinessRole1Code, False)

	@property
	def StmtDtTm(self):
		return self._StmtDtTm

	@StmtDtTm.setter
	def StmtDtTm(self, value):
		self._StmtDtTm = value if value is not None else base_types.UninitialisedField(self, 'StmtDtTm', DateAndDateTimeChoice, False)

	@StmtDtTm.deleter
	def StmtDtTm(self):
		del self._StmtDtTm
		self._StmtDtTm = base_types.UninitialisedField(self, 'StmtDtTm', DateAndDateTimeChoice, False)

	@property
	def StmtId(self):
		return self._StmtId

	@StmtId.setter
	def StmtId(self, value):
		self._StmtId = value if value is not None else base_types.UninitialisedField(self, 'StmtId', Max35Text, False)

	@StmtId.deleter
	def StmtId(self):
		del self._StmtId
		self._StmtId = base_types.UninitialisedField(self, 'StmtId', Max35Text, False)

	@property
	def StmtNb(self):
		return self._StmtNb

	@StmtNb.setter
	def StmtNb(self, value):
		self._StmtNb = value if value is not None else base_types.UninitialisedField(self, 'StmtNb', Number3Choice, False)

	@StmtNb.deleter
	def StmtNb(self):
		del self._StmtNb
		self._StmtNb = base_types.UninitialisedField(self, 'StmtNb', Number3Choice, False)

	@property
	def StmtPrd(self):
		return self._StmtPrd

	@StmtPrd.setter
	def StmtPrd(self, value):
		self._StmtPrd = value if value is not None else base_types.UninitialisedField(self, 'StmtPrd', DatePeriod1Choice, False)

	@StmtPrd.deleter
	def StmtPrd(self):
		del self._StmtPrd
		self._StmtPrd = base_types.UninitialisedField(self, 'StmtPrd', DatePeriod1Choice, False)

	@property
	def UpdTp(self):
		return self._UpdTp

	@UpdTp.setter
	def UpdTp(self, value):
		self._UpdTp = value if value is not None else base_types.UninitialisedField(self, 'UpdTp', UpdateType4Choice, False)

	@UpdTp.deleter
	def UpdTp(self):
		del self._UpdTp
		self._UpdTp = base_types.UninitialisedField(self, 'UpdTp', UpdateType4Choice, False)

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