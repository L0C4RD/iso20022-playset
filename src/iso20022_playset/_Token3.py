from . import base_types
from ._Max140Text import Max140Text
from ._Max19NumericText import Max19NumericText
from ._Max2NumericText import Max2NumericText
from ._ProtectionMethod1Code import ProtectionMethod1Code
from ._TrueFalseIndicator import TrueFalseIndicator
from ._AdditionalData1 import AdditionalData1
from ._Max35Text import Max35Text
from ._ISOYearMonth import ISOYearMonth
from ._StorageLocation1Code import StorageLocation1Code
from ._Max11NumericText import Max11NumericText
from ._Token4 import Token4

class Token3(base_types._BaseFieldType):

	__slots__ = ["_TknRqstrId", "_TknRefId", "_TknInittdInd", "_PrtcnMtd", "_OthrStorgLctn", "_OrgnlTkn", "_OthrPrtcnMtd", "_AddtlData", "_TknAssrncData", "_PmtTkn", "_StorgLctn", "_TknXpryDt", "_TknAssrncMtd"]
	@property
	def TknRqstrId(self):
		return self._TknRqstrId

	@TknRqstrId.setter
	def TknRqstrId(self, value):
		self._TknRqstrId = value if type(value) != base_types.auto else self.make_default("TknRqstrId")

	@TknRqstrId.deleter
	def TknRqstrId(self):
		del self._TknRqstrId
		self._TknRqstrId = None

	@property
	def TknRefId(self):
		return self._TknRefId

	@TknRefId.setter
	def TknRefId(self, value):
		self._TknRefId = value if type(value) != base_types.auto else self.make_default("TknRefId")

	@TknRefId.deleter
	def TknRefId(self):
		del self._TknRefId
		self._TknRefId = None

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
	def PrtcnMtd(self):
		return self._PrtcnMtd

	@PrtcnMtd.setter
	def PrtcnMtd(self, value):
		self._PrtcnMtd = value if type(value) != base_types.auto else self.make_default("PrtcnMtd")

	@PrtcnMtd.deleter
	def PrtcnMtd(self):
		del self._PrtcnMtd
		self._PrtcnMtd = None

	@property
	def OthrStorgLctn(self):
		return self._OthrStorgLctn

	@OthrStorgLctn.setter
	def OthrStorgLctn(self, value):
		self._OthrStorgLctn = value if type(value) != base_types.auto else self.make_default("OthrStorgLctn")

	@OthrStorgLctn.deleter
	def OthrStorgLctn(self):
		del self._OthrStorgLctn
		self._OthrStorgLctn = None

	@property
	def OrgnlTkn(self):
		return self._OrgnlTkn

	@OrgnlTkn.setter
	def OrgnlTkn(self, value):
		self._OrgnlTkn = value if type(value) != base_types.auto else self.make_default("OrgnlTkn")

	@OrgnlTkn.deleter
	def OrgnlTkn(self):
		del self._OrgnlTkn
		self._OrgnlTkn = None

	@property
	def OthrPrtcnMtd(self):
		return self._OthrPrtcnMtd

	@OthrPrtcnMtd.setter
	def OthrPrtcnMtd(self, value):
		self._OthrPrtcnMtd = value if type(value) != base_types.auto else self.make_default("OthrPrtcnMtd")

	@OthrPrtcnMtd.deleter
	def OthrPrtcnMtd(self):
		del self._OthrPrtcnMtd
		self._OthrPrtcnMtd = None

	@property
	def AddtlData(self):
		return self._AddtlData

	@AddtlData.setter
	def AddtlData(self, value):
		self._AddtlData = value if type(value) != base_types.auto else self.make_default("AddtlData")

	@AddtlData.deleter
	def AddtlData(self):
		del self._AddtlData
		self._AddtlData = None

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
	def PmtTkn(self):
		return self._PmtTkn

	@PmtTkn.setter
	def PmtTkn(self, value):
		self._PmtTkn = value if type(value) != base_types.auto else self.make_default("PmtTkn")

	@PmtTkn.deleter
	def PmtTkn(self):
		del self._PmtTkn
		self._PmtTkn = None

	@property
	def StorgLctn(self):
		return self._StorgLctn

	@StorgLctn.setter
	def StorgLctn(self, value):
		self._StorgLctn = value if type(value) != base_types.auto else self.make_default("StorgLctn")

	@StorgLctn.deleter
	def StorgLctn(self):
		del self._StorgLctn
		self._StorgLctn = None

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
		base_types.FieldEntry(name='TknRqstrId', type=Max11NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TknRefId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TknInittdInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtcnMtd', type=ProtectionMethod1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrStorgLctn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlTkn', type=Token4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrPrtcnMtd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlData', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TknAssrncData', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtTkn', type=Max19NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StorgLctn', type=StorageLocation1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TknXpryDt', type=ISOYearMonth, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TknAssrncMtd', type=Max2NumericText, min=0, max=1, mutex_group=None, array=False),
	))

