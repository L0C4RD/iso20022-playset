# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Exact4AlphaNumericText
from . import ISODate
from . import ISODateTime
from . import Max35Text
from . import RegulatoryReporting8

class TradeData44(base_types._BaseFieldType):

	__slots__ = ["_CurStsDtTm", "_CurSttlmDt", "_MtchgSysMtchdSdRef", "_MtchgSysMtchgRef", "_MtchgSysUnqRef", "_NewSttlmDt", "_OrgtrRef", "_PdctTp", "_RgltryRptg", "_SttlmSsnIdr"]
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
	def CurSttlmDt(self):
		return self._CurSttlmDt

	@CurSttlmDt.setter
	def CurSttlmDt(self, value):
		self._CurSttlmDt = value if value is not None else base_types.UninitialisedField(self, 'CurSttlmDt', ISODate, False)

	@CurSttlmDt.deleter
	def CurSttlmDt(self):
		del self._CurSttlmDt
		self._CurSttlmDt = base_types.UninitialisedField(self, 'CurSttlmDt', ISODate, False)

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
	def NewSttlmDt(self):
		return self._NewSttlmDt

	@NewSttlmDt.setter
	def NewSttlmDt(self, value):
		self._NewSttlmDt = value if value is not None else base_types.UninitialisedField(self, 'NewSttlmDt', ISODate, False)

	@NewSttlmDt.deleter
	def NewSttlmDt(self):
		del self._NewSttlmDt
		self._NewSttlmDt = base_types.UninitialisedField(self, 'NewSttlmDt', ISODate, False)

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
	def RgltryRptg(self):
		return self._RgltryRptg

	@RgltryRptg.setter
	def RgltryRptg(self, value):
		self._RgltryRptg = value if value is not None else base_types.UninitialisedField(self, 'RgltryRptg', RegulatoryReporting8, False)

	@RgltryRptg.deleter
	def RgltryRptg(self):
		del self._RgltryRptg
		self._RgltryRptg = base_types.UninitialisedField(self, 'RgltryRptg', RegulatoryReporting8, False)

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
		base_types.FieldEntry(name='CurStsDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CurSttlmDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtchgSysMtchdSdRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtchgSysMtchgRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtchgSysUnqRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewSttlmDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgtrRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RgltryRptg', type=RegulatoryReporting8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmSsnIdr', type=Exact4AlphaNumericText, min=0, max=1, mutex_group=None, array=False),
	))