from . import base_types
import Max2NumericText
import Max11NumericText
import Max140Text
import ISOYearMonth
import Max19NumericText
import Max35Text

class Token4(base_types._BaseFieldType):

	__slots__ = ["_TknRqstrId", "_TknRefId", "_TknAssrncData", "_TknXpryDt", "_PmtTkn", "_TknAssrncMtd"]
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
	def TknRefId(self):
		return self._TknRefId

	@TknRefId.setter
	def TknRefId(self, value):
		self._TknRefId = value if type(value) != auto else self.make_default("TknRefId")

	@TknRefId.deleter
	def TknRefId(self):
		del self._TknRefId
		self._TknRefId = None

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
	def PmtTkn(self):
		return self._PmtTkn

	@PmtTkn.setter
	def PmtTkn(self, value):
		self._PmtTkn = value if type(value) != auto else self.make_default("PmtTkn")

	@PmtTkn.deleter
	def PmtTkn(self):
		del self._PmtTkn
		self._PmtTkn = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='TknRqstrId', type=Max11NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TknRefId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TknAssrncData', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TknXpryDt', type=ISOYearMonth, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtTkn', type=Max19NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TknAssrncMtd', type=Max2NumericText, min=0, max=1, mutex_group=None, array=False),
	))

