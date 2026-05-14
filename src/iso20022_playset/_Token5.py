# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ATICALaxProcessing import ATICALaxProcessing
from ._ISODateTime import ISODateTime
from ._ISOYearMonth import ISOYearMonth
from ._Max11NumericText import Max11NumericText
from ._Max140Text import Max140Text
from ._Max19NumericText import Max19NumericText
from ._Max2NumericText import Max2NumericText
from ._Max35Text import Max35Text
from ._Max3Text import Max3Text
from ._Max70Text import Max70Text
from ._ProtectionMethod2Code import ProtectionMethod2Code
from ._StorageLocation2Code import StorageLocation2Code
from ._Token4 import Token4
from ._TrueFalseIndicator import TrueFalseIndicator

class Token5(base_types._BaseFieldType):

	__slots__ = ["_NonPmt", "_NtlData", "_OrgnlTkn", "_PmtTkn", "_PrtcnMtd", "_PrvtData", "_StorgLctn", "_Sts", "_TknActvtnDtTm", "_TknAssrncData", "_TknAssrncMtd", "_TknInittdInd", "_TknRefId", "_TknRqstrId", "_TknRqstrNm", "_TknTp", "_TknXpryDt", "_UpdtdChanl"]
	@property
	def NonPmt(self):
		return self._NonPmt

	@NonPmt.setter
	def NonPmt(self, value):
		self._NonPmt = value if type(value) != base_types.auto else self.make_default("NonPmt")

	@NonPmt.deleter
	def NonPmt(self):
		del self._NonPmt
		self._NonPmt = None

	@property
	def NtlData(self):
		return self._NtlData

	@NtlData.setter
	def NtlData(self, value):
		self._NtlData = value if type(value) != base_types.auto else self.make_default("NtlData")

	@NtlData.deleter
	def NtlData(self):
		del self._NtlData
		self._NtlData = None

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
	def PrvtData(self):
		return self._PrvtData

	@PrvtData.setter
	def PrvtData(self, value):
		self._PrvtData = value if type(value) != base_types.auto else self.make_default("PrvtData")

	@PrvtData.deleter
	def PrvtData(self):
		del self._PrvtData
		self._PrvtData = None

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
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if type(value) != base_types.auto else self.make_default("Sts")

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = None

	@property
	def TknActvtnDtTm(self):
		return self._TknActvtnDtTm

	@TknActvtnDtTm.setter
	def TknActvtnDtTm(self, value):
		self._TknActvtnDtTm = value if type(value) != base_types.auto else self.make_default("TknActvtnDtTm")

	@TknActvtnDtTm.deleter
	def TknActvtnDtTm(self):
		del self._TknActvtnDtTm
		self._TknActvtnDtTm = None

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
	def TknAssrncMtd(self):
		return self._TknAssrncMtd

	@TknAssrncMtd.setter
	def TknAssrncMtd(self, value):
		self._TknAssrncMtd = value if type(value) != base_types.auto else self.make_default("TknAssrncMtd")

	@TknAssrncMtd.deleter
	def TknAssrncMtd(self):
		del self._TknAssrncMtd
		self._TknAssrncMtd = None

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
	def TknRqstrNm(self):
		return self._TknRqstrNm

	@TknRqstrNm.setter
	def TknRqstrNm(self, value):
		self._TknRqstrNm = value if type(value) != base_types.auto else self.make_default("TknRqstrNm")

	@TknRqstrNm.deleter
	def TknRqstrNm(self):
		del self._TknRqstrNm
		self._TknRqstrNm = None

	@property
	def TknTp(self):
		return self._TknTp

	@TknTp.setter
	def TknTp(self, value):
		self._TknTp = value if type(value) != base_types.auto else self.make_default("TknTp")

	@TknTp.deleter
	def TknTp(self):
		del self._TknTp
		self._TknTp = None

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
	def UpdtdChanl(self):
		return self._UpdtdChanl

	@UpdtdChanl.setter
	def UpdtdChanl(self, value):
		self._UpdtdChanl = value if type(value) != base_types.auto else self.make_default("UpdtdChanl")

	@UpdtdChanl.deleter
	def UpdtdChanl(self):
		del self._UpdtdChanl
		self._UpdtdChanl = None

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