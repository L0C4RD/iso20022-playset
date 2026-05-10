from . import base_types
from .Number import Number
from .OptionStyle1Choice import OptionStyle1Choice
from .Standardisation3Choice import Standardisation3Choice
from .Max4AlphaNumericText import Max4AlphaNumericText
from .OptionType8Choice import OptionType8Choice
from .Price8 import Price8
from .AssignmentMethod2Choice import AssignmentMethod2Choice
from .OptionParty3Choice import OptionParty3Choice
from .BaseOneRate import BaseOneRate
from .DateTimePeriod1Choice import DateTimePeriod1Choice
from .UnderlyingAttributes4 import UnderlyingAttributes4
from .FinancialInstrumentQuantity1Choice import FinancialInstrumentQuantity1Choice
from .ISODateTime import ISODateTime
from .SettleStyle2Choice import SettleStyle2Choice

class Option15(base_types._BaseFieldType):

	__slots__ = ["_TradgPtyRole", "_InstrmAssgnmtMtd", "_OptnTp", "_StrkMltplr", "_CtrctSz", "_Stdstn", "_OptnStyle", "_ConvsPrd", "_VrsnNb", "_MinExrcblQty", "_ConvsDt", "_StrkPric", "_OptnSttlmStyle", "_StrkVal", "_AddtlUndrlygAttrbts", "_XpryLctn"]
	@property
	def TradgPtyRole(self):
		return self._TradgPtyRole

	@TradgPtyRole.setter
	def TradgPtyRole(self, value):
		self._TradgPtyRole = value if type(value) != base_types.auto else self.make_default("TradgPtyRole")

	@TradgPtyRole.deleter
	def TradgPtyRole(self):
		del self._TradgPtyRole
		self._TradgPtyRole = None

	@property
	def InstrmAssgnmtMtd(self):
		return self._InstrmAssgnmtMtd

	@InstrmAssgnmtMtd.setter
	def InstrmAssgnmtMtd(self, value):
		self._InstrmAssgnmtMtd = value if type(value) != base_types.auto else self.make_default("InstrmAssgnmtMtd")

	@InstrmAssgnmtMtd.deleter
	def InstrmAssgnmtMtd(self):
		del self._InstrmAssgnmtMtd
		self._InstrmAssgnmtMtd = None

	@property
	def OptnTp(self):
		return self._OptnTp

	@OptnTp.setter
	def OptnTp(self, value):
		self._OptnTp = value if type(value) != base_types.auto else self.make_default("OptnTp")

	@OptnTp.deleter
	def OptnTp(self):
		del self._OptnTp
		self._OptnTp = None

	@property
	def StrkMltplr(self):
		return self._StrkMltplr

	@StrkMltplr.setter
	def StrkMltplr(self, value):
		self._StrkMltplr = value if type(value) != base_types.auto else self.make_default("StrkMltplr")

	@StrkMltplr.deleter
	def StrkMltplr(self):
		del self._StrkMltplr
		self._StrkMltplr = None

	@property
	def CtrctSz(self):
		return self._CtrctSz

	@CtrctSz.setter
	def CtrctSz(self, value):
		self._CtrctSz = value if type(value) != base_types.auto else self.make_default("CtrctSz")

	@CtrctSz.deleter
	def CtrctSz(self):
		del self._CtrctSz
		self._CtrctSz = None

	@property
	def Stdstn(self):
		return self._Stdstn

	@Stdstn.setter
	def Stdstn(self, value):
		self._Stdstn = value if type(value) != base_types.auto else self.make_default("Stdstn")

	@Stdstn.deleter
	def Stdstn(self):
		del self._Stdstn
		self._Stdstn = None

	@property
	def OptnStyle(self):
		return self._OptnStyle

	@OptnStyle.setter
	def OptnStyle(self, value):
		self._OptnStyle = value if type(value) != base_types.auto else self.make_default("OptnStyle")

	@OptnStyle.deleter
	def OptnStyle(self):
		del self._OptnStyle
		self._OptnStyle = None

	@property
	def ConvsPrd(self):
		return self._ConvsPrd

	@ConvsPrd.setter
	def ConvsPrd(self, value):
		self._ConvsPrd = value if type(value) != base_types.auto else self.make_default("ConvsPrd")

	@ConvsPrd.deleter
	def ConvsPrd(self):
		del self._ConvsPrd
		self._ConvsPrd = None

	@property
	def VrsnNb(self):
		return self._VrsnNb

	@VrsnNb.setter
	def VrsnNb(self, value):
		self._VrsnNb = value if type(value) != base_types.auto else self.make_default("VrsnNb")

	@VrsnNb.deleter
	def VrsnNb(self):
		del self._VrsnNb
		self._VrsnNb = None

	@property
	def MinExrcblQty(self):
		return self._MinExrcblQty

	@MinExrcblQty.setter
	def MinExrcblQty(self, value):
		self._MinExrcblQty = value if type(value) != base_types.auto else self.make_default("MinExrcblQty")

	@MinExrcblQty.deleter
	def MinExrcblQty(self):
		del self._MinExrcblQty
		self._MinExrcblQty = None

	@property
	def ConvsDt(self):
		return self._ConvsDt

	@ConvsDt.setter
	def ConvsDt(self, value):
		self._ConvsDt = value if type(value) != base_types.auto else self.make_default("ConvsDt")

	@ConvsDt.deleter
	def ConvsDt(self):
		del self._ConvsDt
		self._ConvsDt = None

	@property
	def StrkPric(self):
		return self._StrkPric

	@StrkPric.setter
	def StrkPric(self, value):
		self._StrkPric = value if type(value) != base_types.auto else self.make_default("StrkPric")

	@StrkPric.deleter
	def StrkPric(self):
		del self._StrkPric
		self._StrkPric = None

	@property
	def OptnSttlmStyle(self):
		return self._OptnSttlmStyle

	@OptnSttlmStyle.setter
	def OptnSttlmStyle(self, value):
		self._OptnSttlmStyle = value if type(value) != base_types.auto else self.make_default("OptnSttlmStyle")

	@OptnSttlmStyle.deleter
	def OptnSttlmStyle(self):
		del self._OptnSttlmStyle
		self._OptnSttlmStyle = None

	@property
	def StrkVal(self):
		return self._StrkVal

	@StrkVal.setter
	def StrkVal(self, value):
		self._StrkVal = value if type(value) != base_types.auto else self.make_default("StrkVal")

	@StrkVal.deleter
	def StrkVal(self):
		del self._StrkVal
		self._StrkVal = None

	@property
	def AddtlUndrlygAttrbts(self):
		return self._AddtlUndrlygAttrbts

	@AddtlUndrlygAttrbts.setter
	def AddtlUndrlygAttrbts(self, value):
		self._AddtlUndrlygAttrbts = value if type(value) != base_types.auto else self.make_default("AddtlUndrlygAttrbts")

	@AddtlUndrlygAttrbts.deleter
	def AddtlUndrlygAttrbts(self):
		del self._AddtlUndrlygAttrbts
		self._AddtlUndrlygAttrbts = None

	@property
	def XpryLctn(self):
		return self._XpryLctn

	@XpryLctn.setter
	def XpryLctn(self, value):
		self._XpryLctn = value if type(value) != base_types.auto else self.make_default("XpryLctn")

	@XpryLctn.deleter
	def XpryLctn(self):
		del self._XpryLctn
		self._XpryLctn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TradgPtyRole', type=OptionParty3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrmAssgnmtMtd', type=AssignmentMethod2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnTp', type=OptionType8Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StrkMltplr', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctSz', type=BaseOneRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Stdstn', type=Standardisation3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnStyle', type=OptionStyle1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConvsPrd', type=DateTimePeriod1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VrsnNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinExrcblQty', type=FinancialInstrumentQuantity1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConvsDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StrkPric', type=Price8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnSttlmStyle', type=SettleStyle2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StrkVal', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlUndrlygAttrbts', type=UnderlyingAttributes4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='XpryLctn', type=Max4AlphaNumericText, min=0, max=1, mutex_group=None, array=False),
	))

