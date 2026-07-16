# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATICALaxProcessing
from . import ISODateTime
from . import ISOYearMonth
from . import Max11NumericText
from . import Max140Text
from . import Max19NumericText
from . import Max2NumericText
from . import Max35Text
from . import Max3Text
from . import Max70Text
from . import ProtectionMethod2Code
from . import StorageLocation2Code
from . import Token4
from . import TrueFalseIndicator

class Token5(base_types._BaseFieldType):

	__slots__ = ["_NonPmt", "_NtlData", "_OrgnlTkn", "_PmtTkn", "_PrtcnMtd", "_PrvtData", "_StorgLctn", "_Sts", "_TknActvtnDtTm", "_TknAssrncData", "_TknAssrncMtd", "_TknInittdInd", "_TknRefId", "_TknRqstrId", "_TknRqstrNm", "_TknTp", "_TknXpryDt", "_UpdtdChanl"]
	@property
	def NonPmt(self):
		return self._NonPmt

	@NonPmt.setter
	def NonPmt(self, value):
		self._NonPmt = value if value is not None else base_types.UninitialisedField(self, 'NonPmt', TrueFalseIndicator, False)

	@NonPmt.deleter
	def NonPmt(self):
		del self._NonPmt
		self._NonPmt = base_types.UninitialisedField(self, 'NonPmt', TrueFalseIndicator, False)

	@property
	def NtlData(self):
		return self._NtlData

	@NtlData.setter
	def NtlData(self, value):
		self._NtlData = value if value is not None else base_types.UninitialisedField(self, 'NtlData', ATICALaxProcessing, True)

	@NtlData.deleter
	def NtlData(self):
		del self._NtlData
		self._NtlData = base_types.UninitialisedField(self, 'NtlData', ATICALaxProcessing, True)

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
		self._PrtcnMtd = value if value is not None else base_types.UninitialisedField(self, 'PrtcnMtd', ProtectionMethod2Code, False)

	@PrtcnMtd.deleter
	def PrtcnMtd(self):
		del self._PrtcnMtd
		self._PrtcnMtd = base_types.UninitialisedField(self, 'PrtcnMtd', ProtectionMethod2Code, False)

	@property
	def PrvtData(self):
		return self._PrvtData

	@PrvtData.setter
	def PrvtData(self, value):
		self._PrvtData = value if value is not None else base_types.UninitialisedField(self, 'PrvtData', ATICALaxProcessing, True)

	@PrvtData.deleter
	def PrvtData(self):
		del self._PrvtData
		self._PrvtData = base_types.UninitialisedField(self, 'PrvtData', ATICALaxProcessing, True)

	@property
	def StorgLctn(self):
		return self._StorgLctn

	@StorgLctn.setter
	def StorgLctn(self, value):
		self._StorgLctn = value if value is not None else base_types.UninitialisedField(self, 'StorgLctn', StorageLocation2Code, False)

	@StorgLctn.deleter
	def StorgLctn(self):
		del self._StorgLctn
		self._StorgLctn = base_types.UninitialisedField(self, 'StorgLctn', StorageLocation2Code, False)

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if value is not None else base_types.UninitialisedField(self, 'Sts', Max35Text, False)

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = base_types.UninitialisedField(self, 'Sts', Max35Text, False)

	@property
	def TknActvtnDtTm(self):
		return self._TknActvtnDtTm

	@TknActvtnDtTm.setter
	def TknActvtnDtTm(self, value):
		self._TknActvtnDtTm = value if value is not None else base_types.UninitialisedField(self, 'TknActvtnDtTm', ISODateTime, False)

	@TknActvtnDtTm.deleter
	def TknActvtnDtTm(self):
		del self._TknActvtnDtTm
		self._TknActvtnDtTm = base_types.UninitialisedField(self, 'TknActvtnDtTm', ISODateTime, False)

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
	def TknRqstrNm(self):
		return self._TknRqstrNm

	@TknRqstrNm.setter
	def TknRqstrNm(self, value):
		self._TknRqstrNm = value if value is not None else base_types.UninitialisedField(self, 'TknRqstrNm', Max70Text, False)

	@TknRqstrNm.deleter
	def TknRqstrNm(self):
		del self._TknRqstrNm
		self._TknRqstrNm = base_types.UninitialisedField(self, 'TknRqstrNm', Max70Text, False)

	@property
	def TknTp(self):
		return self._TknTp

	@TknTp.setter
	def TknTp(self, value):
		self._TknTp = value if value is not None else base_types.UninitialisedField(self, 'TknTp', Max3Text, False)

	@TknTp.deleter
	def TknTp(self):
		del self._TknTp
		self._TknTp = base_types.UninitialisedField(self, 'TknTp', Max3Text, False)

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

	@property
	def UpdtdChanl(self):
		return self._UpdtdChanl

	@UpdtdChanl.setter
	def UpdtdChanl(self, value):
		self._UpdtdChanl = value if value is not None else base_types.UninitialisedField(self, 'UpdtdChanl', Max35Text, False)

	@UpdtdChanl.deleter
	def UpdtdChanl(self):
		del self._UpdtdChanl
		self._UpdtdChanl = base_types.UninitialisedField(self, 'UpdtdChanl', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NonPmt', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtlData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrgnlTkn', type=Token4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtTkn', type=Max19NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtcnMtd', type=ProtectionMethod2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvtData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StorgLctn', type=StorageLocation2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sts', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TknActvtnDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TknAssrncData', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TknAssrncMtd', type=Max2NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TknInittdInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TknRefId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TknRqstrId', type=Max11NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TknRqstrNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TknTp', type=Max3Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TknXpryDt', type=ISOYearMonth, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UpdtdChanl', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))