# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateAndDateTime2Choice
from . import EventFrequency6Code
from . import Exact5NumericText
from . import Max35Text
from . import StatementUpdateType1Code
from . import YesNoIndicator

class ReportParameters7(base_types._BaseFieldType):

	__slots__ = ["_ActvtyInd", "_Frqcy", "_NetPosId", "_RptDtAndTm", "_RptNb", "_UpdTp"]
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
		self._Frqcy = value if value is not None else base_types.UninitialisedField(self, 'Frqcy', EventFrequency6Code, False)

	@Frqcy.deleter
	def Frqcy(self):
		del self._Frqcy
		self._Frqcy = base_types.UninitialisedField(self, 'Frqcy', EventFrequency6Code, False)

	@property
	def NetPosId(self):
		return self._NetPosId

	@NetPosId.setter
	def NetPosId(self, value):
		self._NetPosId = value if value is not None else base_types.UninitialisedField(self, 'NetPosId', Max35Text, False)

	@NetPosId.deleter
	def NetPosId(self):
		del self._NetPosId
		self._NetPosId = base_types.UninitialisedField(self, 'NetPosId', Max35Text, False)

	@property
	def RptDtAndTm(self):
		return self._RptDtAndTm

	@RptDtAndTm.setter
	def RptDtAndTm(self, value):
		self._RptDtAndTm = value if value is not None else base_types.UninitialisedField(self, 'RptDtAndTm', DateAndDateTime2Choice, False)

	@RptDtAndTm.deleter
	def RptDtAndTm(self):
		del self._RptDtAndTm
		self._RptDtAndTm = base_types.UninitialisedField(self, 'RptDtAndTm', DateAndDateTime2Choice, False)

	@property
	def RptNb(self):
		return self._RptNb

	@RptNb.setter
	def RptNb(self, value):
		self._RptNb = value if value is not None else base_types.UninitialisedField(self, 'RptNb', Exact5NumericText, False)

	@RptNb.deleter
	def RptNb(self):
		del self._RptNb
		self._RptNb = base_types.UninitialisedField(self, 'RptNb', Exact5NumericText, False)

	@property
	def UpdTp(self):
		return self._UpdTp

	@UpdTp.setter
	def UpdTp(self, value):
		self._UpdTp = value if value is not None else base_types.UninitialisedField(self, 'UpdTp', StatementUpdateType1Code, False)

	@UpdTp.deleter
	def UpdTp(self):
		del self._UpdTp
		self._UpdTp = base_types.UninitialisedField(self, 'UpdTp', StatementUpdateType1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActvtyInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Frqcy', type=EventFrequency6Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetPosId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptDtAndTm', type=DateAndDateTime2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptNb', type=Exact5NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UpdTp', type=StatementUpdateType1Code, min=1, max=1, mutex_group=None, array=False),
	))