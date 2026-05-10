import base_types
import Max19NumericText
import Max11NumericText
import Max140Text
import Max2NumericText
import TrueFalseIndicator
import Exact4NumericText

class Token1(base_types._BaseFieldType):

	__slots__ = ["_TknAssrncData", "_TknAssrncMtd", "_TknRqstrId", "_TknInittdInd", "_TknXpryDt", "_PmtTkn"]
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
	def TknRqstrId(self):
		return self._TknRqstrId

	@TknRqstrId.setter
	def TknRqstrId(self, value):
		self._TknRqstrId = value if type(value) != auto else self.make_default("TknRqstrId")

	@TknRqstrId.deleter
	def TknRqstrId(self):
		del self._TknRqstrId
		self._TknRqstrId = None

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
	def PmtTkn(self):
		return self._PmtTkn

	@PmtTkn.setter
	def PmtTkn(self, value):
		self._PmtTkn = value if type(value) != auto else self.make_default("PmtTkn")

	@PmtTkn.deleter
	def PmtTkn(self):
		del self._PmtTkn
		self._PmtTkn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TknAssrncData', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TknAssrncMtd', type=Max2NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TknRqstrId', type=Max11NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TknInittdInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TknXpryDt', type=Exact4NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtTkn', type=Max19NumericText, min=0, max=1, mutex_group=None, array=False),
	))

