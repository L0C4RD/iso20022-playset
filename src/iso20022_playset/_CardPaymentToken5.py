from . import base_types
from ._Number import Number
from ._PaymentTokenIdentifiers1 import PaymentTokenIdentifiers1
from ._Min2Max3NumericText import Min2Max3NumericText
from ._Max2NumericText import Max2NumericText
from ._TrueFalseIndicator import TrueFalseIndicator
from ._Max500Binary import Max500Binary
from ._Max35Text import Max35Text
from ._Max10Text import Max10Text
from ._Min8Max28NumericText import Min8Max28NumericText

class CardPaymentToken5(base_types._BaseFieldType):

	__slots__ = ["_CardSeqNb", "_TknChrtc", "_TknInittdInd", "_TknXpryDt", "_TknAssrncData", "_Tkn", "_TknAssrncLvl", "_TknRqstr", "_TknAssrncMtd"]
	@property
	def CardSeqNb(self):
		return self._CardSeqNb

	@CardSeqNb.setter
	def CardSeqNb(self, value):
		self._CardSeqNb = value if type(value) != base_types.auto else self.make_default("CardSeqNb")

	@CardSeqNb.deleter
	def CardSeqNb(self):
		del self._CardSeqNb
		self._CardSeqNb = None

	@property
	def TknChrtc(self):
		return self._TknChrtc

	@TknChrtc.setter
	def TknChrtc(self, value):
		self._TknChrtc = value if type(value) != base_types.auto else self.make_default("TknChrtc")

	@TknChrtc.deleter
	def TknChrtc(self):
		del self._TknChrtc
		self._TknChrtc = None

	@property
	def TknInittdInd(self):
		return self._TknInittdInd

	@TknInittdInd.setter
	def TknInittdInd(self, value):
		self._TknInittdInd = value if type(value) != base_types.auto else self.make_default("TknInittdInd")

	@TknInittdInd.deleter
	def TknInittdInd(self):
		del self._TknInittdInd
		self._TknInittdInd = None

	@property
	def TknXpryDt(self):
		return self._TknXpryDt

	@TknXpryDt.setter
	def TknXpryDt(self, value):
		self._TknXpryDt = value if type(value) != base_types.auto else self.make_default("TknXpryDt")

	@TknXpryDt.deleter
	def TknXpryDt(self):
		del self._TknXpryDt
		self._TknXpryDt = None

	@property
	def TknAssrncData(self):
		return self._TknAssrncData

	@TknAssrncData.setter
	def TknAssrncData(self, value):
		self._TknAssrncData = value if type(value) != base_types.auto else self.make_default("TknAssrncData")

	@TknAssrncData.deleter
	def TknAssrncData(self):
		del self._TknAssrncData
		self._TknAssrncData = None

	@property
	def Tkn(self):
		return self._Tkn

	@Tkn.setter
	def Tkn(self, value):
		self._Tkn = value if type(value) != base_types.auto else self.make_default("Tkn")

	@Tkn.deleter
	def Tkn(self):
		del self._Tkn
		self._Tkn = None

	@property
	def TknAssrncLvl(self):
		return self._TknAssrncLvl

	@TknAssrncLvl.setter
	def TknAssrncLvl(self, value):
		self._TknAssrncLvl = value if type(value) != base_types.auto else self.make_default("TknAssrncLvl")

	@TknAssrncLvl.deleter
	def TknAssrncLvl(self):
		del self._TknAssrncLvl
		self._TknAssrncLvl = None

	@property
	def TknRqstr(self):
		return self._TknRqstr

	@TknRqstr.setter
	def TknRqstr(self, value):
		self._TknRqstr = value if type(value) != base_types.auto else self.make_default("TknRqstr")

	@TknRqstr.deleter
	def TknRqstr(self):
		del self._TknRqstr
		self._TknRqstr = None

	@property
	def TknAssrncMtd(self):
		return self._TknAssrncMtd

	@TknAssrncMtd.setter
	def TknAssrncMtd(self, value):
		self._TknAssrncMtd = value if type(value) != base_types.auto else self.make_default("TknAssrncMtd")

	@TknAssrncMtd.deleter
	def TknAssrncMtd(self):
		del self._TknAssrncMtd
		self._TknAssrncMtd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CardSeqNb', type=Min2Max3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TknChrtc', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TknInittdInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TknXpryDt', type=Max10Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TknAssrncData', type=Max500Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tkn', type=Min8Max28NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TknAssrncLvl', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TknRqstr', type=PaymentTokenIdentifiers1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TknAssrncMtd', type=Max2NumericText, min=0, max=1, mutex_group=None, array=False),
	))

