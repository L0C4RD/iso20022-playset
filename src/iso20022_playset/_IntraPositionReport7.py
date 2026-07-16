# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateAndDateTime2Choice
from . import Frequency22Choice
from . import Max35Text
from . import Number3Choice
from . import Period7Choice
from . import UpdateType15Choice
from . import YesNoIndicator

class IntraPositionReport7(base_types._BaseFieldType):

	__slots__ = ["_ActvtyInd", "_Frqcy", "_QryRef", "_RptDtTm", "_RptId", "_RptNb", "_RptPrd", "_UpdTp"]
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
	def RptDtTm(self):
		return self._RptDtTm

	@RptDtTm.setter
	def RptDtTm(self, value):
		self._RptDtTm = value if value is not None else base_types.UninitialisedField(self, 'RptDtTm', DateAndDateTime2Choice, False)

	@RptDtTm.deleter
	def RptDtTm(self):
		del self._RptDtTm
		self._RptDtTm = base_types.UninitialisedField(self, 'RptDtTm', DateAndDateTime2Choice, False)

	@property
	def RptId(self):
		return self._RptId

	@RptId.setter
	def RptId(self, value):
		self._RptId = value if value is not None else base_types.UninitialisedField(self, 'RptId', Max35Text, False)

	@RptId.deleter
	def RptId(self):
		del self._RptId
		self._RptId = base_types.UninitialisedField(self, 'RptId', Max35Text, False)

	@property
	def RptNb(self):
		return self._RptNb

	@RptNb.setter
	def RptNb(self, value):
		self._RptNb = value if value is not None else base_types.UninitialisedField(self, 'RptNb', Number3Choice, False)

	@RptNb.deleter
	def RptNb(self):
		del self._RptNb
		self._RptNb = base_types.UninitialisedField(self, 'RptNb', Number3Choice, False)

	@property
	def RptPrd(self):
		return self._RptPrd

	@RptPrd.setter
	def RptPrd(self, value):
		self._RptPrd = value if value is not None else base_types.UninitialisedField(self, 'RptPrd', Period7Choice, False)

	@RptPrd.deleter
	def RptPrd(self):
		del self._RptPrd
		self._RptPrd = base_types.UninitialisedField(self, 'RptPrd', Period7Choice, False)

	@property
	def UpdTp(self):
		return self._UpdTp

	@UpdTp.setter
	def UpdTp(self, value):
		self._UpdTp = value if value is not None else base_types.UninitialisedField(self, 'UpdTp', UpdateType15Choice, False)

	@UpdTp.deleter
	def UpdTp(self):
		del self._UpdTp
		self._UpdTp = base_types.UninitialisedField(self, 'UpdTp', UpdateType15Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActvtyInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Frqcy', type=Frequency22Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptDtTm', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptNb', type=Number3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptPrd', type=Period7Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UpdTp', type=UpdateType15Choice, min=1, max=1, mutex_group=None, array=False),
	))