# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max10Text
from . import Max2NumericText
from . import Max35Text
from . import Max500Binary
from . import Min2Max3NumericText
from . import Min8Max28NumericText
from . import Number
from . import PaymentTokenIdentifiers1
from . import TrueFalseIndicator

class CardPaymentToken5(base_types._BaseFieldType):

	__slots__ = ["_CardSeqNb", "_Tkn", "_TknAssrncData", "_TknAssrncLvl", "_TknAssrncMtd", "_TknChrtc", "_TknInittdInd", "_TknRqstr", "_TknXpryDt"]
	@property
	def CardSeqNb(self):
		return self._CardSeqNb

	@CardSeqNb.setter
	def CardSeqNb(self, value):
		self._CardSeqNb = value if value is not None else base_types.UninitialisedField(self, 'CardSeqNb', Min2Max3NumericText, False)

	@CardSeqNb.deleter
	def CardSeqNb(self):
		del self._CardSeqNb
		self._CardSeqNb = base_types.UninitialisedField(self, 'CardSeqNb', Min2Max3NumericText, False)

	@property
	def Tkn(self):
		return self._Tkn

	@Tkn.setter
	def Tkn(self, value):
		self._Tkn = value if value is not None else base_types.UninitialisedField(self, 'Tkn', Min8Max28NumericText, False)

	@Tkn.deleter
	def Tkn(self):
		del self._Tkn
		self._Tkn = base_types.UninitialisedField(self, 'Tkn', Min8Max28NumericText, False)

	@property
	def TknAssrncData(self):
		return self._TknAssrncData

	@TknAssrncData.setter
	def TknAssrncData(self, value):
		self._TknAssrncData = value if value is not None else base_types.UninitialisedField(self, 'TknAssrncData', Max500Binary, False)

	@TknAssrncData.deleter
	def TknAssrncData(self):
		del self._TknAssrncData
		self._TknAssrncData = base_types.UninitialisedField(self, 'TknAssrncData', Max500Binary, False)

	@property
	def TknAssrncLvl(self):
		return self._TknAssrncLvl

	@TknAssrncLvl.setter
	def TknAssrncLvl(self, value):
		self._TknAssrncLvl = value if value is not None else base_types.UninitialisedField(self, 'TknAssrncLvl', Number, False)

	@TknAssrncLvl.deleter
	def TknAssrncLvl(self):
		del self._TknAssrncLvl
		self._TknAssrncLvl = base_types.UninitialisedField(self, 'TknAssrncLvl', Number, False)

	@property
	def TknAssrncMtd(self):
		return self._TknAssrncMtd

	@TknAssrncMtd.setter
	def TknAssrncMtd(self, value):
		self._TknAssrncMtd = value if value is not None else base_types.UninitialisedField(self, 'TknAssrncMtd', Max2NumericText, False)

	@TknAssrncMtd.deleter
	def TknAssrncMtd(self):
		del self._TknAssrncMtd
		self._TknAssrncMtd = base_types.UninitialisedField(self, 'TknAssrncMtd', Max2NumericText, False)

	@property
	def TknChrtc(self):
		return self._TknChrtc

	@TknChrtc.setter
	def TknChrtc(self, value):
		self._TknChrtc = value if value is not None else base_types.UninitialisedField(self, 'TknChrtc', Max35Text, True)

	@TknChrtc.deleter
	def TknChrtc(self):
		del self._TknChrtc
		self._TknChrtc = base_types.UninitialisedField(self, 'TknChrtc', Max35Text, True)

	@property
	def TknInittdInd(self):
		return self._TknInittdInd

	@TknInittdInd.setter
	def TknInittdInd(self, value):
		self._TknInittdInd = value if value is not None else base_types.UninitialisedField(self, 'TknInittdInd', TrueFalseIndicator, False)

	@TknInittdInd.deleter
	def TknInittdInd(self):
		del self._TknInittdInd
		self._TknInittdInd = base_types.UninitialisedField(self, 'TknInittdInd', TrueFalseIndicator, False)

	@property
	def TknRqstr(self):
		return self._TknRqstr

	@TknRqstr.setter
	def TknRqstr(self, value):
		self._TknRqstr = value if value is not None else base_types.UninitialisedField(self, 'TknRqstr', PaymentTokenIdentifiers1, False)

	@TknRqstr.deleter
	def TknRqstr(self):
		del self._TknRqstr
		self._TknRqstr = base_types.UninitialisedField(self, 'TknRqstr', PaymentTokenIdentifiers1, False)

	@property
	def TknXpryDt(self):
		return self._TknXpryDt

	@TknXpryDt.setter
	def TknXpryDt(self, value):
		self._TknXpryDt = value if value is not None else base_types.UninitialisedField(self, 'TknXpryDt', Max10Text, False)

	@TknXpryDt.deleter
	def TknXpryDt(self):
		del self._TknXpryDt
		self._TknXpryDt = base_types.UninitialisedField(self, 'TknXpryDt', Max10Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CardSeqNb', type=Min2Max3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tkn', type=Min8Max28NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TknAssrncData', type=Max500Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TknAssrncLvl', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TknAssrncMtd', type=Max2NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TknChrtc', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TknInittdInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TknRqstr', type=PaymentTokenIdentifiers1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TknXpryDt', type=Max10Text, min=0, max=1, mutex_group=None, array=False),
	))