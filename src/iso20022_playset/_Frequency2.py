# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BusinessDayConvention2Code
from . import EndPoint2Choice
from . import Frequency37Choice
from . import ISODate
from . import Max3NumericText

class Frequency2(base_types._BaseFieldType):

	__slots__ = ["_EndPtChc", "_NonWorkgDayAdjstmnt", "_ReqdFrqcyPttrn", "_Seq", "_StartDt"]
	@property
	def EndPtChc(self):
		return self._EndPtChc

	@EndPtChc.setter
	def EndPtChc(self, value):
		self._EndPtChc = value if value is not None else base_types.UninitialisedField(self, 'EndPtChc', EndPoint2Choice, False)

	@EndPtChc.deleter
	def EndPtChc(self):
		del self._EndPtChc
		self._EndPtChc = base_types.UninitialisedField(self, 'EndPtChc', EndPoint2Choice, False)

	@property
	def NonWorkgDayAdjstmnt(self):
		return self._NonWorkgDayAdjstmnt

	@NonWorkgDayAdjstmnt.setter
	def NonWorkgDayAdjstmnt(self, value):
		self._NonWorkgDayAdjstmnt = value if value is not None else base_types.UninitialisedField(self, 'NonWorkgDayAdjstmnt', BusinessDayConvention2Code, False)

	@NonWorkgDayAdjstmnt.deleter
	def NonWorkgDayAdjstmnt(self):
		del self._NonWorkgDayAdjstmnt
		self._NonWorkgDayAdjstmnt = base_types.UninitialisedField(self, 'NonWorkgDayAdjstmnt', BusinessDayConvention2Code, False)

	@property
	def ReqdFrqcyPttrn(self):
		return self._ReqdFrqcyPttrn

	@ReqdFrqcyPttrn.setter
	def ReqdFrqcyPttrn(self, value):
		self._ReqdFrqcyPttrn = value if value is not None else base_types.UninitialisedField(self, 'ReqdFrqcyPttrn', Frequency37Choice, False)

	@ReqdFrqcyPttrn.deleter
	def ReqdFrqcyPttrn(self):
		del self._ReqdFrqcyPttrn
		self._ReqdFrqcyPttrn = base_types.UninitialisedField(self, 'ReqdFrqcyPttrn', Frequency37Choice, False)

	@property
	def Seq(self):
		return self._Seq

	@Seq.setter
	def Seq(self, value):
		self._Seq = value if value is not None else base_types.UninitialisedField(self, 'Seq', Max3NumericText, False)

	@Seq.deleter
	def Seq(self):
		del self._Seq
		self._Seq = base_types.UninitialisedField(self, 'Seq', Max3NumericText, False)

	@property
	def StartDt(self):
		return self._StartDt

	@StartDt.setter
	def StartDt(self, value):
		self._StartDt = value if value is not None else base_types.UninitialisedField(self, 'StartDt', ISODate, False)

	@StartDt.deleter
	def StartDt(self):
		del self._StartDt
		self._StartDt = base_types.UninitialisedField(self, 'StartDt', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='EndPtChc', type=EndPoint2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonWorkgDayAdjstmnt', type=BusinessDayConvention2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdFrqcyPttrn', type=Frequency37Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Seq', type=Max3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StartDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
	))