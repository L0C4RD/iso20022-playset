# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalData1
from . import Frequency17Code
from . import ISODate
from . import ISOTime
from . import Max140Text
from . import Max35Text
from . import Max5NumericText
from . import Max70Text
from . import OutputFormat5Code
from . import TrueFalseIndicator

class ReportData7(base_types._BaseFieldType):

	__slots__ = ["_AddtlData", "_ConttnInd", "_Dt", "_Frmt", "_Frqcy", "_Id", "_Nm", "_OthrFrmt", "_Qlfr", "_Seq", "_Tm", "_TtlOcrncs"]
	@property
	def AddtlData(self):
		return self._AddtlData

	@AddtlData.setter
	def AddtlData(self, value):
		self._AddtlData = value if value is not None else base_types.UninitialisedField(self, 'AddtlData', AdditionalData1, True)

	@AddtlData.deleter
	def AddtlData(self):
		del self._AddtlData
		self._AddtlData = base_types.UninitialisedField(self, 'AddtlData', AdditionalData1, True)

	@property
	def ConttnInd(self):
		return self._ConttnInd

	@ConttnInd.setter
	def ConttnInd(self, value):
		self._ConttnInd = value if value is not None else base_types.UninitialisedField(self, 'ConttnInd', TrueFalseIndicator, False)

	@ConttnInd.deleter
	def ConttnInd(self):
		del self._ConttnInd
		self._ConttnInd = base_types.UninitialisedField(self, 'ConttnInd', TrueFalseIndicator, False)

	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if value is not None else base_types.UninitialisedField(self, 'Dt', ISODate, False)

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = base_types.UninitialisedField(self, 'Dt', ISODate, False)

	@property
	def Frmt(self):
		return self._Frmt

	@Frmt.setter
	def Frmt(self, value):
		self._Frmt = value if value is not None else base_types.UninitialisedField(self, 'Frmt', OutputFormat5Code, False)

	@Frmt.deleter
	def Frmt(self):
		del self._Frmt
		self._Frmt = base_types.UninitialisedField(self, 'Frmt', OutputFormat5Code, False)

	@property
	def Frqcy(self):
		return self._Frqcy

	@Frqcy.setter
	def Frqcy(self, value):
		self._Frqcy = value if value is not None else base_types.UninitialisedField(self, 'Frqcy', Frequency17Code, False)

	@Frqcy.deleter
	def Frqcy(self):
		del self._Frqcy
		self._Frqcy = base_types.UninitialisedField(self, 'Frqcy', Frequency17Code, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Max140Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Max140Text, False)

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if value is not None else base_types.UninitialisedField(self, 'Nm', Max140Text, False)

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = base_types.UninitialisedField(self, 'Nm', Max140Text, False)

	@property
	def OthrFrmt(self):
		return self._OthrFrmt

	@OthrFrmt.setter
	def OthrFrmt(self, value):
		self._OthrFrmt = value if value is not None else base_types.UninitialisedField(self, 'OthrFrmt', Max35Text, False)

	@OthrFrmt.deleter
	def OthrFrmt(self):
		del self._OthrFrmt
		self._OthrFrmt = base_types.UninitialisedField(self, 'OthrFrmt', Max35Text, False)

	@property
	def Qlfr(self):
		return self._Qlfr

	@Qlfr.setter
	def Qlfr(self, value):
		self._Qlfr = value if value is not None else base_types.UninitialisedField(self, 'Qlfr', Max70Text, False)

	@Qlfr.deleter
	def Qlfr(self):
		del self._Qlfr
		self._Qlfr = base_types.UninitialisedField(self, 'Qlfr', Max70Text, False)

	@property
	def Seq(self):
		return self._Seq

	@Seq.setter
	def Seq(self, value):
		self._Seq = value if value is not None else base_types.UninitialisedField(self, 'Seq', Max5NumericText, False)

	@Seq.deleter
	def Seq(self):
		del self._Seq
		self._Seq = base_types.UninitialisedField(self, 'Seq', Max5NumericText, False)

	@property
	def Tm(self):
		return self._Tm

	@Tm.setter
	def Tm(self, value):
		self._Tm = value if value is not None else base_types.UninitialisedField(self, 'Tm', ISOTime, False)

	@Tm.deleter
	def Tm(self):
		del self._Tm
		self._Tm = base_types.UninitialisedField(self, 'Tm', ISOTime, False)

	@property
	def TtlOcrncs(self):
		return self._TtlOcrncs

	@TtlOcrncs.setter
	def TtlOcrncs(self, value):
		self._TtlOcrncs = value if value is not None else base_types.UninitialisedField(self, 'TtlOcrncs', Max5NumericText, False)

	@TtlOcrncs.deleter
	def TtlOcrncs(self):
		del self._TtlOcrncs
		self._TtlOcrncs = base_types.UninitialisedField(self, 'TtlOcrncs', Max5NumericText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlData', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ConttnInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Frmt', type=OutputFormat5Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Frqcy', type=Frequency17Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrFrmt', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qlfr', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Seq', type=Max5NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tm', type=ISOTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlOcrncs', type=Max5NumericText, min=0, max=1, mutex_group=None, array=False),
	))