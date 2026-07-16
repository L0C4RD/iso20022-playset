# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISOYearMonth
from . import Max11NumericText
from . import Max140Text
from . import Max19NumericText
from . import Max2NumericText
from . import Max35Text

class Token4(base_types._BaseFieldType):

	__slots__ = ["_PmtTkn", "_TknAssrncData", "_TknAssrncMtd", "_TknRefId", "_TknRqstrId", "_TknXpryDt"]
	@property
	def PmtTkn(self):
		return self._PmtTkn

	@PmtTkn.setter
	def PmtTkn(self, value):
		self._PmtTkn = value if value is not None else base_types.UninitialisedField(self, 'PmtTkn', Max19NumericText, False)

	@PmtTkn.deleter
	def PmtTkn(self):
		del self._PmtTkn
		self._PmtTkn = base_types.UninitialisedField(self, 'PmtTkn', Max19NumericText, False)

	@property
	def TknAssrncData(self):
		return self._TknAssrncData

	@TknAssrncData.setter
	def TknAssrncData(self, value):
		self._TknAssrncData = value if value is not None else base_types.UninitialisedField(self, 'TknAssrncData', Max140Text, False)

	@TknAssrncData.deleter
	def TknAssrncData(self):
		del self._TknAssrncData
		self._TknAssrncData = base_types.UninitialisedField(self, 'TknAssrncData', Max140Text, False)

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
	def TknRefId(self):
		return self._TknRefId

	@TknRefId.setter
	def TknRefId(self, value):
		self._TknRefId = value if value is not None else base_types.UninitialisedField(self, 'TknRefId', Max35Text, False)

	@TknRefId.deleter
	def TknRefId(self):
		del self._TknRefId
		self._TknRefId = base_types.UninitialisedField(self, 'TknRefId', Max35Text, False)

	@property
	def TknRqstrId(self):
		return self._TknRqstrId

	@TknRqstrId.setter
	def TknRqstrId(self, value):
		self._TknRqstrId = value if value is not None else base_types.UninitialisedField(self, 'TknRqstrId', Max11NumericText, False)

	@TknRqstrId.deleter
	def TknRqstrId(self):
		del self._TknRqstrId
		self._TknRqstrId = base_types.UninitialisedField(self, 'TknRqstrId', Max11NumericText, False)

	@property
	def TknXpryDt(self):
		return self._TknXpryDt

	@TknXpryDt.setter
	def TknXpryDt(self, value):
		self._TknXpryDt = value if value is not None else base_types.UninitialisedField(self, 'TknXpryDt', ISOYearMonth, False)

	@TknXpryDt.deleter
	def TknXpryDt(self):
		del self._TknXpryDt
		self._TknXpryDt = base_types.UninitialisedField(self, 'TknXpryDt', ISOYearMonth, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PmtTkn', type=Max19NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TknAssrncData', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TknAssrncMtd', type=Max2NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TknRefId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TknRqstrId', type=Max11NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TknXpryDt', type=ISOYearMonth, min=0, max=1, mutex_group=None, array=False),
	))