# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Exact4AlphaNumericText
from . import ISODateTime
from . import Max20Text
from . import Max35Text
from . import Status28Choice
from . import StatusAndSubStatus2
from . import StatusSubType2Code
from . import YesNoIndicator

class TradeData15(base_types._BaseFieldType):

	__slots__ = ["_CurSts", "_CurStsDtTm", "_CurStsSubTp", "_MsgId", "_MtchgSysMtchdSdRef", "_MtchgSysMtchgRef", "_MtchgSysUnqRef", "_OrgtrRef", "_PdctTp", "_PrvsSts", "_PrvsStsDtTm", "_PrvsStsSubTp", "_SpltTradInd", "_StsOrgtr", "_SttlmSsnIdr"]
	@property
	def CurSts(self):
		return self._CurSts

	@CurSts.setter
	def CurSts(self, value):
		self._CurSts = value if value is not None else base_types.UninitialisedField(self, 'CurSts', StatusAndSubStatus2, False)

	@CurSts.deleter
	def CurSts(self):
		del self._CurSts
		self._CurSts = base_types.UninitialisedField(self, 'CurSts', StatusAndSubStatus2, False)

	@property
	def CurStsDtTm(self):
		return self._CurStsDtTm

	@CurStsDtTm.setter
	def CurStsDtTm(self, value):
		self._CurStsDtTm = value if value is not None else base_types.UninitialisedField(self, 'CurStsDtTm', ISODateTime, False)

	@CurStsDtTm.deleter
	def CurStsDtTm(self):
		del self._CurStsDtTm
		self._CurStsDtTm = base_types.UninitialisedField(self, 'CurStsDtTm', ISODateTime, False)

	@property
	def CurStsSubTp(self):
		return self._CurStsSubTp

	@CurStsSubTp.setter
	def CurStsSubTp(self, value):
		self._CurStsSubTp = value if value is not None else base_types.UninitialisedField(self, 'CurStsSubTp', StatusSubType2Code, False)

	@CurStsSubTp.deleter
	def CurStsSubTp(self):
		del self._CurStsSubTp
		self._CurStsSubTp = base_types.UninitialisedField(self, 'CurStsSubTp', StatusSubType2Code, False)

	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if value is not None else base_types.UninitialisedField(self, 'MsgId', Max35Text, False)

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = base_types.UninitialisedField(self, 'MsgId', Max35Text, False)

	@property
	def MtchgSysMtchdSdRef(self):
		return self._MtchgSysMtchdSdRef

	@MtchgSysMtchdSdRef.setter
	def MtchgSysMtchdSdRef(self, value):
		self._MtchgSysMtchdSdRef = value if value is not None else base_types.UninitialisedField(self, 'MtchgSysMtchdSdRef', Max35Text, False)

	@MtchgSysMtchdSdRef.deleter
	def MtchgSysMtchdSdRef(self):
		del self._MtchgSysMtchdSdRef
		self._MtchgSysMtchdSdRef = base_types.UninitialisedField(self, 'MtchgSysMtchdSdRef', Max35Text, False)

	@property
	def MtchgSysMtchgRef(self):
		return self._MtchgSysMtchgRef

	@MtchgSysMtchgRef.setter
	def MtchgSysMtchgRef(self, value):
		self._MtchgSysMtchgRef = value if value is not None else base_types.UninitialisedField(self, 'MtchgSysMtchgRef', Max35Text, False)

	@MtchgSysMtchgRef.deleter
	def MtchgSysMtchgRef(self):
		del self._MtchgSysMtchgRef
		self._MtchgSysMtchgRef = base_types.UninitialisedField(self, 'MtchgSysMtchgRef', Max35Text, False)

	@property
	def MtchgSysUnqRef(self):
		return self._MtchgSysUnqRef

	@MtchgSysUnqRef.setter
	def MtchgSysUnqRef(self, value):
		self._MtchgSysUnqRef = value if value is not None else base_types.UninitialisedField(self, 'MtchgSysUnqRef', Max35Text, False)

	@MtchgSysUnqRef.deleter
	def MtchgSysUnqRef(self):
		del self._MtchgSysUnqRef
		self._MtchgSysUnqRef = base_types.UninitialisedField(self, 'MtchgSysUnqRef', Max35Text, False)

	@property
	def OrgtrRef(self):
		return self._OrgtrRef

	@OrgtrRef.setter
	def OrgtrRef(self, value):
		self._OrgtrRef = value if value is not None else base_types.UninitialisedField(self, 'OrgtrRef', Max35Text, False)

	@OrgtrRef.deleter
	def OrgtrRef(self):
		del self._OrgtrRef
		self._OrgtrRef = base_types.UninitialisedField(self, 'OrgtrRef', Max35Text, False)

	@property
	def PdctTp(self):
		return self._PdctTp

	@PdctTp.setter
	def PdctTp(self, value):
		self._PdctTp = value if value is not None else base_types.UninitialisedField(self, 'PdctTp', Max35Text, False)

	@PdctTp.deleter
	def PdctTp(self):
		del self._PdctTp
		self._PdctTp = base_types.UninitialisedField(self, 'PdctTp', Max35Text, False)

	@property
	def PrvsSts(self):
		return self._PrvsSts

	@PrvsSts.setter
	def PrvsSts(self, value):
		self._PrvsSts = value if value is not None else base_types.UninitialisedField(self, 'PrvsSts', Status28Choice, False)

	@PrvsSts.deleter
	def PrvsSts(self):
		del self._PrvsSts
		self._PrvsSts = base_types.UninitialisedField(self, 'PrvsSts', Status28Choice, False)

	@property
	def PrvsStsDtTm(self):
		return self._PrvsStsDtTm

	@PrvsStsDtTm.setter
	def PrvsStsDtTm(self, value):
		self._PrvsStsDtTm = value if value is not None else base_types.UninitialisedField(self, 'PrvsStsDtTm', ISODateTime, False)

	@PrvsStsDtTm.deleter
	def PrvsStsDtTm(self):
		del self._PrvsStsDtTm
		self._PrvsStsDtTm = base_types.UninitialisedField(self, 'PrvsStsDtTm', ISODateTime, False)

	@property
	def PrvsStsSubTp(self):
		return self._PrvsStsSubTp

	@PrvsStsSubTp.setter
	def PrvsStsSubTp(self, value):
		self._PrvsStsSubTp = value if value is not None else base_types.UninitialisedField(self, 'PrvsStsSubTp', StatusSubType2Code, False)

	@PrvsStsSubTp.deleter
	def PrvsStsSubTp(self):
		del self._PrvsStsSubTp
		self._PrvsStsSubTp = base_types.UninitialisedField(self, 'PrvsStsSubTp', StatusSubType2Code, False)

	@property
	def SpltTradInd(self):
		return self._SpltTradInd

	@SpltTradInd.setter
	def SpltTradInd(self, value):
		self._SpltTradInd = value if value is not None else base_types.UninitialisedField(self, 'SpltTradInd', YesNoIndicator, False)

	@SpltTradInd.deleter
	def SpltTradInd(self):
		del self._SpltTradInd
		self._SpltTradInd = base_types.UninitialisedField(self, 'SpltTradInd', YesNoIndicator, False)

	@property
	def StsOrgtr(self):
		return self._StsOrgtr

	@StsOrgtr.setter
	def StsOrgtr(self, value):
		self._StsOrgtr = value if value is not None else base_types.UninitialisedField(self, 'StsOrgtr', Max20Text, False)

	@StsOrgtr.deleter
	def StsOrgtr(self):
		del self._StsOrgtr
		self._StsOrgtr = base_types.UninitialisedField(self, 'StsOrgtr', Max20Text, False)

	@property
	def SttlmSsnIdr(self):
		return self._SttlmSsnIdr

	@SttlmSsnIdr.setter
	def SttlmSsnIdr(self, value):
		self._SttlmSsnIdr = value if value is not None else base_types.UninitialisedField(self, 'SttlmSsnIdr', Exact4AlphaNumericText, False)

	@SttlmSsnIdr.deleter
	def SttlmSsnIdr(self):
		del self._SttlmSsnIdr
		self._SttlmSsnIdr = base_types.UninitialisedField(self, 'SttlmSsnIdr', Exact4AlphaNumericText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CurSts', type=StatusAndSubStatus2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CurStsDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CurStsSubTp', type=StatusSubType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtchgSysMtchdSdRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtchgSysMtchgRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtchgSysUnqRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgtrRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsSts', type=Status28Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsStsDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsStsSubTp', type=StatusSubType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SpltTradInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsOrgtr', type=Max20Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmSsnIdr', type=Exact4AlphaNumericText, min=0, max=1, mutex_group=None, array=False),
	))