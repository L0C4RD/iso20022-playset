import base_types
import StatusAndSubStatus2
import YesNoIndicator
import ISODateTime
import Max35Text
import StatusSubType2Code
import Exact4AlphaNumericText
import Status28Choice
import Max20Text

class TradeData15(base_types._BaseFieldType):

	__slots__ = ["_CurSts", "_PrvsStsDtTm", "_StsOrgtr", "_CurStsSubTp", "_MtchgSysMtchdSdRef", "_MsgId", "_SttlmSsnIdr", "_PrvsSts", "_CurStsDtTm", "_PrvsStsSubTp", "_OrgtrRef", "_MtchgSysUnqRef", "_SpltTradInd", "_PdctTp", "_MtchgSysMtchgRef"]
	@property
	def CurSts(self):
		return self._CurSts

	@CurSts.setter
	def CurSts(self, value):
		self._CurSts = value if type(value) != auto else self.make_default("CurSts")

	@CurSts.deleter
	def CurSts(self):
		del self._CurSts
		self._CurSts = None

	@property
	def PrvsStsDtTm(self):
		return self._PrvsStsDtTm

	@PrvsStsDtTm.setter
	def PrvsStsDtTm(self, value):
		self._PrvsStsDtTm = value if type(value) != auto else self.make_default("PrvsStsDtTm")

	@PrvsStsDtTm.deleter
	def PrvsStsDtTm(self):
		del self._PrvsStsDtTm
		self._PrvsStsDtTm = None

	@property
	def StsOrgtr(self):
		return self._StsOrgtr

	@StsOrgtr.setter
	def StsOrgtr(self, value):
		self._StsOrgtr = value if type(value) != auto else self.make_default("StsOrgtr")

	@StsOrgtr.deleter
	def StsOrgtr(self):
		del self._StsOrgtr
		self._StsOrgtr = None

	@property
	def CurStsSubTp(self):
		return self._CurStsSubTp

	@CurStsSubTp.setter
	def CurStsSubTp(self, value):
		self._CurStsSubTp = value if type(value) != auto else self.make_default("CurStsSubTp")

	@CurStsSubTp.deleter
	def CurStsSubTp(self):
		del self._CurStsSubTp
		self._CurStsSubTp = None

	@property
	def MtchgSysMtchdSdRef(self):
		return self._MtchgSysMtchdSdRef

	@MtchgSysMtchdSdRef.setter
	def MtchgSysMtchdSdRef(self, value):
		self._MtchgSysMtchdSdRef = value if type(value) != auto else self.make_default("MtchgSysMtchdSdRef")

	@MtchgSysMtchdSdRef.deleter
	def MtchgSysMtchdSdRef(self):
		del self._MtchgSysMtchdSdRef
		self._MtchgSysMtchdSdRef = None

	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if type(value) != auto else self.make_default("MsgId")

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = None

	@property
	def SttlmSsnIdr(self):
		return self._SttlmSsnIdr

	@SttlmSsnIdr.setter
	def SttlmSsnIdr(self, value):
		self._SttlmSsnIdr = value if type(value) != auto else self.make_default("SttlmSsnIdr")

	@SttlmSsnIdr.deleter
	def SttlmSsnIdr(self):
		del self._SttlmSsnIdr
		self._SttlmSsnIdr = None

	@property
	def PrvsSts(self):
		return self._PrvsSts

	@PrvsSts.setter
	def PrvsSts(self, value):
		self._PrvsSts = value if type(value) != auto else self.make_default("PrvsSts")

	@PrvsSts.deleter
	def PrvsSts(self):
		del self._PrvsSts
		self._PrvsSts = None

	@property
	def CurStsDtTm(self):
		return self._CurStsDtTm

	@CurStsDtTm.setter
	def CurStsDtTm(self, value):
		self._CurStsDtTm = value if type(value) != auto else self.make_default("CurStsDtTm")

	@CurStsDtTm.deleter
	def CurStsDtTm(self):
		del self._CurStsDtTm
		self._CurStsDtTm = None

	@property
	def PrvsStsSubTp(self):
		return self._PrvsStsSubTp

	@PrvsStsSubTp.setter
	def PrvsStsSubTp(self, value):
		self._PrvsStsSubTp = value if type(value) != auto else self.make_default("PrvsStsSubTp")

	@PrvsStsSubTp.deleter
	def PrvsStsSubTp(self):
		del self._PrvsStsSubTp
		self._PrvsStsSubTp = None

	@property
	def OrgtrRef(self):
		return self._OrgtrRef

	@OrgtrRef.setter
	def OrgtrRef(self, value):
		self._OrgtrRef = value if type(value) != auto else self.make_default("OrgtrRef")

	@OrgtrRef.deleter
	def OrgtrRef(self):
		del self._OrgtrRef
		self._OrgtrRef = None

	@property
	def MtchgSysUnqRef(self):
		return self._MtchgSysUnqRef

	@MtchgSysUnqRef.setter
	def MtchgSysUnqRef(self, value):
		self._MtchgSysUnqRef = value if type(value) != auto else self.make_default("MtchgSysUnqRef")

	@MtchgSysUnqRef.deleter
	def MtchgSysUnqRef(self):
		del self._MtchgSysUnqRef
		self._MtchgSysUnqRef = None

	@property
	def SpltTradInd(self):
		return self._SpltTradInd

	@SpltTradInd.setter
	def SpltTradInd(self, value):
		self._SpltTradInd = value if type(value) != auto else self.make_default("SpltTradInd")

	@SpltTradInd.deleter
	def SpltTradInd(self):
		del self._SpltTradInd
		self._SpltTradInd = None

	@property
	def PdctTp(self):
		return self._PdctTp

	@PdctTp.setter
	def PdctTp(self, value):
		self._PdctTp = value if type(value) != auto else self.make_default("PdctTp")

	@PdctTp.deleter
	def PdctTp(self):
		del self._PdctTp
		self._PdctTp = None

	@property
	def MtchgSysMtchgRef(self):
		return self._MtchgSysMtchgRef

	@MtchgSysMtchgRef.setter
	def MtchgSysMtchgRef(self, value):
		self._MtchgSysMtchgRef = value if type(value) != auto else self.make_default("MtchgSysMtchgRef")

	@MtchgSysMtchgRef.deleter
	def MtchgSysMtchgRef(self):
		del self._MtchgSysMtchgRef
		self._MtchgSysMtchgRef = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CurSts', type=StatusAndSubStatus2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsStsDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsOrgtr', type=Max20Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CurStsSubTp', type=StatusSubType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtchgSysMtchdSdRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmSsnIdr', type=Exact4AlphaNumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsSts', type=Status28Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CurStsDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsStsSubTp', type=StatusSubType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgtrRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtchgSysUnqRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SpltTradInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtchgSysMtchgRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

