from . import base_types
from ._BusinessDayConvention1Code import BusinessDayConvention1Code
from ._EndPoint1Choice import EndPoint1Choice
from ._Frequency37Choice import Frequency37Choice
from ._ISODate import ISODate
from ._Max3NumericText import Max3NumericText

class Frequency1(base_types._BaseFieldType):

	__slots__ = ["_EndPtChc", "_NonWorkgDayAdjstmnt", "_ReqdFrqcyPttrn", "_Seq", "_StartDt"]
	@property
	def EndPtChc(self):
		return self._EndPtChc

	@EndPtChc.setter
	def EndPtChc(self, value):
		self._EndPtChc = value if type(value) != base_types.auto else self.make_default("EndPtChc")

	@EndPtChc.deleter
	def EndPtChc(self):
		del self._EndPtChc
		self._EndPtChc = None

	@property
	def NonWorkgDayAdjstmnt(self):
		return self._NonWorkgDayAdjstmnt

	@NonWorkgDayAdjstmnt.setter
	def NonWorkgDayAdjstmnt(self, value):
		self._NonWorkgDayAdjstmnt = value if type(value) != base_types.auto else self.make_default("NonWorkgDayAdjstmnt")

	@NonWorkgDayAdjstmnt.deleter
	def NonWorkgDayAdjstmnt(self):
		del self._NonWorkgDayAdjstmnt
		self._NonWorkgDayAdjstmnt = None

	@property
	def ReqdFrqcyPttrn(self):
		return self._ReqdFrqcyPttrn

	@ReqdFrqcyPttrn.setter
	def ReqdFrqcyPttrn(self, value):
		self._ReqdFrqcyPttrn = value if type(value) != base_types.auto else self.make_default("ReqdFrqcyPttrn")

	@ReqdFrqcyPttrn.deleter
	def ReqdFrqcyPttrn(self):
		del self._ReqdFrqcyPttrn
		self._ReqdFrqcyPttrn = None

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
	def StartDt(self):
		return self._StartDt

	@StartDt.setter
	def StartDt(self, value):
		self._StartDt = value if type(value) != base_types.auto else self.make_default("StartDt")

	@StartDt.deleter
	def StartDt(self):
		del self._StartDt
		self._StartDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='EndPtChc', type=EndPoint1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonWorkgDayAdjstmnt', type=BusinessDayConvention1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdFrqcyPttrn', type=Frequency37Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Seq', type=Max3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StartDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
	))

