# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AssignmentMethod2Choice
from . import BaseOneRate
from . import DateTimePeriod1Choice
from . import FinancialInstrumentQuantity1Choice
from . import ISODateTime
from . import Max4AlphaNumericText
from . import Number
from . import OptionParty3Choice
from . import OptionStyle1Choice
from . import OptionType8Choice
from . import Price8
from . import SettleStyle2Choice
from . import Standardisation3Choice
from . import UnderlyingAttributes4

class Option15(base_types._BaseFieldType):

	__slots__ = ["_AddtlUndrlygAttrbts", "_ConvsDt", "_ConvsPrd", "_CtrctSz", "_InstrmAssgnmtMtd", "_MinExrcblQty", "_OptnSttlmStyle", "_OptnStyle", "_OptnTp", "_Stdstn", "_StrkMltplr", "_StrkPric", "_StrkVal", "_TradgPtyRole", "_VrsnNb", "_XpryLctn"]
	@property
	def AddtlUndrlygAttrbts(self):
		return self._AddtlUndrlygAttrbts

	@AddtlUndrlygAttrbts.setter
	def AddtlUndrlygAttrbts(self, value):
		self._AddtlUndrlygAttrbts = value if value is not None else base_types.UninitialisedField(self, 'AddtlUndrlygAttrbts', UnderlyingAttributes4, True)

	@AddtlUndrlygAttrbts.deleter
	def AddtlUndrlygAttrbts(self):
		del self._AddtlUndrlygAttrbts
		self._AddtlUndrlygAttrbts = base_types.UninitialisedField(self, 'AddtlUndrlygAttrbts', UnderlyingAttributes4, True)

	@property
	def ConvsDt(self):
		return self._ConvsDt

	@ConvsDt.setter
	def ConvsDt(self, value):
		self._ConvsDt = value if value is not None else base_types.UninitialisedField(self, 'ConvsDt', ISODateTime, False)

	@ConvsDt.deleter
	def ConvsDt(self):
		del self._ConvsDt
		self._ConvsDt = base_types.UninitialisedField(self, 'ConvsDt', ISODateTime, False)

	@property
	def ConvsPrd(self):
		return self._ConvsPrd

	@ConvsPrd.setter
	def ConvsPrd(self, value):
		self._ConvsPrd = value if value is not None else base_types.UninitialisedField(self, 'ConvsPrd', DateTimePeriod1Choice, False)

	@ConvsPrd.deleter
	def ConvsPrd(self):
		del self._ConvsPrd
		self._ConvsPrd = base_types.UninitialisedField(self, 'ConvsPrd', DateTimePeriod1Choice, False)

	@property
	def CtrctSz(self):
		return self._CtrctSz

	@CtrctSz.setter
	def CtrctSz(self, value):
		self._CtrctSz = value if value is not None else base_types.UninitialisedField(self, 'CtrctSz', BaseOneRate, False)

	@CtrctSz.deleter
	def CtrctSz(self):
		del self._CtrctSz
		self._CtrctSz = base_types.UninitialisedField(self, 'CtrctSz', BaseOneRate, False)

	@property
	def InstrmAssgnmtMtd(self):
		return self._InstrmAssgnmtMtd

	@InstrmAssgnmtMtd.setter
	def InstrmAssgnmtMtd(self, value):
		self._InstrmAssgnmtMtd = value if value is not None else base_types.UninitialisedField(self, 'InstrmAssgnmtMtd', AssignmentMethod2Choice, False)

	@InstrmAssgnmtMtd.deleter
	def InstrmAssgnmtMtd(self):
		del self._InstrmAssgnmtMtd
		self._InstrmAssgnmtMtd = base_types.UninitialisedField(self, 'InstrmAssgnmtMtd', AssignmentMethod2Choice, False)

	@property
	def MinExrcblQty(self):
		return self._MinExrcblQty

	@MinExrcblQty.setter
	def MinExrcblQty(self, value):
		self._MinExrcblQty = value if value is not None else base_types.UninitialisedField(self, 'MinExrcblQty', FinancialInstrumentQuantity1Choice, False)

	@MinExrcblQty.deleter
	def MinExrcblQty(self):
		del self._MinExrcblQty
		self._MinExrcblQty = base_types.UninitialisedField(self, 'MinExrcblQty', FinancialInstrumentQuantity1Choice, False)

	@property
	def OptnSttlmStyle(self):
		return self._OptnSttlmStyle

	@OptnSttlmStyle.setter
	def OptnSttlmStyle(self, value):
		self._OptnSttlmStyle = value if value is not None else base_types.UninitialisedField(self, 'OptnSttlmStyle', SettleStyle2Choice, False)

	@OptnSttlmStyle.deleter
	def OptnSttlmStyle(self):
		del self._OptnSttlmStyle
		self._OptnSttlmStyle = base_types.UninitialisedField(self, 'OptnSttlmStyle', SettleStyle2Choice, False)

	@property
	def OptnStyle(self):
		return self._OptnStyle

	@OptnStyle.setter
	def OptnStyle(self, value):
		self._OptnStyle = value if value is not None else base_types.UninitialisedField(self, 'OptnStyle', OptionStyle1Choice, False)

	@OptnStyle.deleter
	def OptnStyle(self):
		del self._OptnStyle
		self._OptnStyle = base_types.UninitialisedField(self, 'OptnStyle', OptionStyle1Choice, False)

	@property
	def OptnTp(self):
		return self._OptnTp

	@OptnTp.setter
	def OptnTp(self, value):
		self._OptnTp = value if value is not None else base_types.UninitialisedField(self, 'OptnTp', OptionType8Choice, False)

	@OptnTp.deleter
	def OptnTp(self):
		del self._OptnTp
		self._OptnTp = base_types.UninitialisedField(self, 'OptnTp', OptionType8Choice, False)

	@property
	def Stdstn(self):
		return self._Stdstn

	@Stdstn.setter
	def Stdstn(self, value):
		self._Stdstn = value if value is not None else base_types.UninitialisedField(self, 'Stdstn', Standardisation3Choice, False)

	@Stdstn.deleter
	def Stdstn(self):
		del self._Stdstn
		self._Stdstn = base_types.UninitialisedField(self, 'Stdstn', Standardisation3Choice, False)

	@property
	def StrkMltplr(self):
		return self._StrkMltplr

	@StrkMltplr.setter
	def StrkMltplr(self, value):
		self._StrkMltplr = value if value is not None else base_types.UninitialisedField(self, 'StrkMltplr', Number, False)

	@StrkMltplr.deleter
	def StrkMltplr(self):
		del self._StrkMltplr
		self._StrkMltplr = base_types.UninitialisedField(self, 'StrkMltplr', Number, False)

	@property
	def StrkPric(self):
		return self._StrkPric

	@StrkPric.setter
	def StrkPric(self, value):
		self._StrkPric = value if value is not None else base_types.UninitialisedField(self, 'StrkPric', Price8, False)

	@StrkPric.deleter
	def StrkPric(self):
		del self._StrkPric
		self._StrkPric = base_types.UninitialisedField(self, 'StrkPric', Price8, False)

	@property
	def StrkVal(self):
		return self._StrkVal

	@StrkVal.setter
	def StrkVal(self, value):
		self._StrkVal = value if value is not None else base_types.UninitialisedField(self, 'StrkVal', Number, False)

	@StrkVal.deleter
	def StrkVal(self):
		del self._StrkVal
		self._StrkVal = base_types.UninitialisedField(self, 'StrkVal', Number, False)

	@property
	def TradgPtyRole(self):
		return self._TradgPtyRole

	@TradgPtyRole.setter
	def TradgPtyRole(self, value):
		self._TradgPtyRole = value if value is not None else base_types.UninitialisedField(self, 'TradgPtyRole', OptionParty3Choice, False)

	@TradgPtyRole.deleter
	def TradgPtyRole(self):
		del self._TradgPtyRole
		self._TradgPtyRole = base_types.UninitialisedField(self, 'TradgPtyRole', OptionParty3Choice, False)

	@property
	def VrsnNb(self):
		return self._VrsnNb

	@VrsnNb.setter
	def VrsnNb(self, value):
		self._VrsnNb = value if value is not None else base_types.UninitialisedField(self, 'VrsnNb', Number, False)

	@VrsnNb.deleter
	def VrsnNb(self):
		del self._VrsnNb
		self._VrsnNb = base_types.UninitialisedField(self, 'VrsnNb', Number, False)

	@property
	def XpryLctn(self):
		return self._XpryLctn

	@XpryLctn.setter
	def XpryLctn(self, value):
		self._XpryLctn = value if value is not None else base_types.UninitialisedField(self, 'XpryLctn', Max4AlphaNumericText, False)

	@XpryLctn.deleter
	def XpryLctn(self):
		del self._XpryLctn
		self._XpryLctn = base_types.UninitialisedField(self, 'XpryLctn', Max4AlphaNumericText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlUndrlygAttrbts', type=UnderlyingAttributes4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ConvsDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConvsPrd', type=DateTimePeriod1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctSz', type=BaseOneRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrmAssgnmtMtd', type=AssignmentMethod2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinExrcblQty', type=FinancialInstrumentQuantity1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnSttlmStyle', type=SettleStyle2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnStyle', type=OptionStyle1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnTp', type=OptionType8Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Stdstn', type=Standardisation3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StrkMltplr', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StrkPric', type=Price8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StrkVal', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgPtyRole', type=OptionParty3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VrsnNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpryLctn', type=Max4AlphaNumericText, min=0, max=1, mutex_group=None, array=False),
	))