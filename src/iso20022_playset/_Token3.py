# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalData1
from . import ISOYearMonth
from . import Max11NumericText
from . import Max140Text
from . import Max19NumericText
from . import Max2NumericText
from . import Max35Text
from . import ProtectionMethod1Code
from . import StorageLocation1Code
from . import Token4
from . import TrueFalseIndicator

class Token3(base_types._BaseFieldType):

	__slots__ = ["_AddtlData", "_OrgnlTkn", "_OthrPrtcnMtd", "_OthrStorgLctn", "_PmtTkn", "_PrtcnMtd", "_StorgLctn", "_TknAssrncData", "_TknAssrncMtd", "_TknInittdInd", "_TknRefId", "_TknRqstrId", "_TknXpryDt"]
	@property
	def AddtlData(self):
		return self._AddtlData

	@AddtlData.setter
	def AddtlData(self, value):
		self._AddtlData = value if value is not None else base_types.UninitialisedField(self, 'AddtlData', AdditionalData1, True)

	@AddtlData.deleter
	def AddtlData(self):
		del self._AddtlData
		self._AddtlData = base_types.UninitialisedField(self, 'AddtlData', AdditionalData1, True)

	@property
	def OrgnlTkn(self):
		return self._OrgnlTkn

	@OrgnlTkn.setter
	def OrgnlTkn(self, value):
		self._OrgnlTkn = value if value is not None else base_types.UninitialisedField(self, 'OrgnlTkn', Token4, False)

	@OrgnlTkn.deleter
	def OrgnlTkn(self):
		del self._OrgnlTkn
		self._OrgnlTkn = base_types.UninitialisedField(self, 'OrgnlTkn', Token4, False)

	@property
	def OthrPrtcnMtd(self):
		return self._OthrPrtcnMtd

	@OthrPrtcnMtd.setter
	def OthrPrtcnMtd(self, value):
		self._OthrPrtcnMtd = value if value is not None else base_types.UninitialisedField(self, 'OthrPrtcnMtd', Max35Text, False)

	@OthrPrtcnMtd.deleter
	def OthrPrtcnMtd(self):
		del self._OthrPrtcnMtd
		self._OthrPrtcnMtd = base_types.UninitialisedField(self, 'OthrPrtcnMtd', Max35Text, False)

	@property
	def OthrStorgLctn(self):
		return self._OthrStorgLctn

	@OthrStorgLctn.setter
	def OthrStorgLctn(self, value):
		self._OthrStorgLctn = value if value is not None else base_types.UninitialisedField(self, 'OthrStorgLctn', Max35Text, False)

	@OthrStorgLctn.deleter
	def OthrStorgLctn(self):
		del self._OthrStorgLctn
		self._OthrStorgLctn = base_types.UninitialisedField(self, 'OthrStorgLctn', Max35Text, False)

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
	def PrtcnMtd(self):
		return self._PrtcnMtd

	@PrtcnMtd.setter
	def PrtcnMtd(self, value):
		self._PrtcnMtd = value if value is not None else base_types.UninitialisedField(self, 'PrtcnMtd', ProtectionMethod1Code, False)

	@PrtcnMtd.deleter
	def PrtcnMtd(self):
		del self._PrtcnMtd
		self._PrtcnMtd = base_types.UninitialisedField(self, 'PrtcnMtd', ProtectionMethod1Code, False)

	@property
	def StorgLctn(self):
		return self._StorgLctn

	@StorgLctn.setter
	def StorgLctn(self, value):
		self._StorgLctn = value if value is not None else base_types.UninitialisedField(self, 'StorgLctn', StorageLocation1Code, False)

	@StorgLctn.deleter
	def StorgLctn(self):
		del self._StorgLctn
		self._StorgLctn = base_types.UninitialisedField(self, 'StorgLctn', StorageLocation1Code, False)

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
		base_types.FieldEntry(name='AddtlData', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrgnlTkn', type=Token4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrPrtcnMtd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrStorgLctn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtTkn', type=Max19NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtcnMtd', type=ProtectionMethod1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StorgLctn', type=StorageLocation1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TknAssrncData', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TknAssrncMtd', type=Max2NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TknInittdInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TknRefId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TknRqstrId', type=Max11NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TknXpryDt', type=ISOYearMonth, min=0, max=1, mutex_group=None, array=False),
	))