import base_types
import Max35Text
import TrueFalseIndicator
import Max10Text
import Number
import Max2NumericText
import PaymentTokenIdentifiers1
import Max500Binary

class MerchantToken2(base_types._BaseFieldType):

	__slots__ = ["_TknAssrncMtd", "_TknChrtc", "_TknAssrncLvl", "_TknInittdInd", "_TknAssrncData", "_TknXpryDt", "_Tkn", "_TknRqstr"]
	@property
	def TknAssrncMtd(self):
		return self._TknAssrncMtd

	@TknAssrncMtd.setter
	def TknAssrncMtd(self, value):
		self._TknAssrncMtd = value if type(value) != auto else self.make_default("TknAssrncMtd")

	@TknAssrncMtd.deleter
	def TknAssrncMtd(self):
		del self._TknAssrncMtd
		self._TknAssrncMtd = None

	@property
	def TknChrtc(self):
		return self._TknChrtc

	@TknChrtc.setter
	def TknChrtc(self, value):
		self._TknChrtc = value if type(value) != auto else self.make_default("TknChrtc")

	@TknChrtc.deleter
	def TknChrtc(self):
		del self._TknChrtc
		self._TknChrtc = None

	@property
	def TknAssrncLvl(self):
		return self._TknAssrncLvl

	@TknAssrncLvl.setter
	def TknAssrncLvl(self, value):
		self._TknAssrncLvl = value if type(value) != auto else self.make_default("TknAssrncLvl")

	@TknAssrncLvl.deleter
	def TknAssrncLvl(self):
		del self._TknAssrncLvl
		self._TknAssrncLvl = None

	@property
	def TknInittdInd(self):
		return self._TknInittdInd

	@TknInittdInd.setter
	def TknInittdInd(self, value):
		self._TknInittdInd = value if type(value) != auto else self.make_default("TknInittdInd")

	@TknInittdInd.deleter
	def TknInittdInd(self):
		del self._TknInittdInd
		self._TknInittdInd = None

	@property
	def TknAssrncData(self):
		return self._TknAssrncData

	@TknAssrncData.setter
	def TknAssrncData(self, value):
		self._TknAssrncData = value if type(value) != auto else self.make_default("TknAssrncData")

	@TknAssrncData.deleter
	def TknAssrncData(self):
		del self._TknAssrncData
		self._TknAssrncData = None

	@property
	def TknXpryDt(self):
		return self._TknXpryDt

	@TknXpryDt.setter
	def TknXpryDt(self, value):
		self._TknXpryDt = value if type(value) != auto else self.make_default("TknXpryDt")

	@TknXpryDt.deleter
	def TknXpryDt(self):
		del self._TknXpryDt
		self._TknXpryDt = None

	@property
	def Tkn(self):
		return self._Tkn

	@Tkn.setter
	def Tkn(self, value):
		self._Tkn = value if type(value) != auto else self.make_default("Tkn")

	@Tkn.deleter
	def Tkn(self):
		del self._Tkn
		self._Tkn = None

	@property
	def TknRqstr(self):
		return self._TknRqstr

	@TknRqstr.setter
	def TknRqstr(self, value):
		self._TknRqstr = value if type(value) != auto else self.make_default("TknRqstr")

	@TknRqstr.deleter
	def TknRqstr(self):
		del self._TknRqstr
		self._TknRqstr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TknAssrncMtd', type=Max2NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TknChrtc', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TknAssrncLvl', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TknInittdInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TknAssrncData', type=Max500Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TknXpryDt', type=Max10Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tkn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TknRqstr', type=PaymentTokenIdentifiers1, min=0, max=1, mutex_group=None, array=False),
	))

