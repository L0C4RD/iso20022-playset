from . import base_types
from ._ATICALaxProcessing import ATICALaxProcessing
from ._Frequency17Code import Frequency17Code
from ._ISODate import ISODate
from ._ISOTime import ISOTime
from ._Max140Text import Max140Text
from ._Max5NumericText import Max5NumericText
from ._Max70Text import Max70Text
from ._OutputFormat7Code import OutputFormat7Code
from ._TrueFalseIndicator import TrueFalseIndicator

class ReportData8(base_types._BaseFieldType):

	__slots__ = ["_ConttnInd", "_Dt", "_Frmt", "_Frqcy", "_Id", "_Nm", "_NtlData", "_PrvtData", "_Qlfr", "_Seq", "_Tm", "_TtlOcrncs"]
	@property
	def ConttnInd(self):
		return self._ConttnInd

	@ConttnInd.setter
	def ConttnInd(self, value):
		self._ConttnInd = value if type(value) != base_types.auto else self.make_default("ConttnInd")

	@ConttnInd.deleter
	def ConttnInd(self):
		del self._ConttnInd
		self._ConttnInd = None

	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if type(value) != base_types.auto else self.make_default("Dt")

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = None

	@property
	def Frmt(self):
		return self._Frmt

	@Frmt.setter
	def Frmt(self, value):
		self._Frmt = value if type(value) != base_types.auto else self.make_default("Frmt")

	@Frmt.deleter
	def Frmt(self):
		del self._Frmt
		self._Frmt = None

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
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if type(value) != base_types.auto else self.make_default("Nm")

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = None

	@property
	def NtlData(self):
		return self._NtlData

	@NtlData.setter
	def NtlData(self, value):
		self._NtlData = value if type(value) != base_types.auto else self.make_default("NtlData")

	@NtlData.deleter
	def NtlData(self):
		del self._NtlData
		self._NtlData = None

	@property
	def PrvtData(self):
		return self._PrvtData

	@PrvtData.setter
	def PrvtData(self, value):
		self._PrvtData = value if type(value) != base_types.auto else self.make_default("PrvtData")

	@PrvtData.deleter
	def PrvtData(self):
		del self._PrvtData
		self._PrvtData = None

	@property
	def Qlfr(self):
		return self._Qlfr

	@Qlfr.setter
	def Qlfr(self, value):
		self._Qlfr = value if type(value) != base_types.auto else self.make_default("Qlfr")

	@Qlfr.deleter
	def Qlfr(self):
		del self._Qlfr
		self._Qlfr = None

	@property
	def Seq(self):
		return self._Seq

	@Seq.setter
	def Seq(self, value):
		self._Seq = value if type(value) != base_types.auto else self.make_default("Seq")

	@Seq.deleter
	def Seq(self):
		del self._Seq
		self._Seq = None

	@property
	def Tm(self):
		return self._Tm

	@Tm.setter
	def Tm(self, value):
		self._Tm = value if type(value) != base_types.auto else self.make_default("Tm")

	@Tm.deleter
	def Tm(self):
		del self._Tm
		self._Tm = None

	@property
	def TtlOcrncs(self):
		return self._TtlOcrncs

	@TtlOcrncs.setter
	def TtlOcrncs(self, value):
		self._TtlOcrncs = value if type(value) != base_types.auto else self.make_default("TtlOcrncs")

	@TtlOcrncs.deleter
	def TtlOcrncs(self):
		del self._TtlOcrncs
		self._TtlOcrncs = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ConttnInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Frmt', type=OutputFormat7Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Frqcy', type=Frequency17Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtlData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrvtData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Qlfr', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Seq', type=Max5NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tm', type=ISOTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlOcrncs', type=Max5NumericText, min=0, max=1, mutex_group=None, array=False),
	))

