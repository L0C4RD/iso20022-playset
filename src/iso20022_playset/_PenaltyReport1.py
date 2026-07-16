# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateAndDateTime2Choice
from . import DatePeriod1Choice
from . import Frequency22Choice
from . import Max35Text
from . import PenaltyListType1Choice
from . import UpdateType15Choice
from . import YesNoIndicator

class PenaltyReport1(base_types._BaseFieldType):

	__slots__ = ["_ActvtyInd", "_Frqcy", "_PnltyListTp", "_RptDt", "_RptId", "_RptPrd", "_UpdTp"]
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
	def PnltyListTp(self):
		return self._PnltyListTp

	@PnltyListTp.setter
	def PnltyListTp(self, value):
		self._PnltyListTp = value if value is not None else base_types.UninitialisedField(self, 'PnltyListTp', PenaltyListType1Choice, False)

	@PnltyListTp.deleter
	def PnltyListTp(self):
		del self._PnltyListTp
		self._PnltyListTp = base_types.UninitialisedField(self, 'PnltyListTp', PenaltyListType1Choice, False)

	@property
	def RptDt(self):
		return self._RptDt

	@RptDt.setter
	def RptDt(self, value):
		self._RptDt = value if value is not None else base_types.UninitialisedField(self, 'RptDt', DateAndDateTime2Choice, False)

	@RptDt.deleter
	def RptDt(self):
		del self._RptDt
		self._RptDt = base_types.UninitialisedField(self, 'RptDt', DateAndDateTime2Choice, False)

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
	def RptPrd(self):
		return self._RptPrd

	@RptPrd.setter
	def RptPrd(self, value):
		self._RptPrd = value if value is not None else base_types.UninitialisedField(self, 'RptPrd', DatePeriod1Choice, False)

	@RptPrd.deleter
	def RptPrd(self):
		del self._RptPrd
		self._RptPrd = base_types.UninitialisedField(self, 'RptPrd', DatePeriod1Choice, False)

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
		base_types.FieldEntry(name='PnltyListTp', type=PenaltyListType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptPrd', type=DatePeriod1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UpdTp', type=UpdateType15Choice, min=0, max=1, mutex_group=None, array=False),
	))