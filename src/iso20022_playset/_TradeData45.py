# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Exact4AlphaNumericText
from . import ISODateTime
from . import Max35Text
from . import Status28Choice
from . import StatusAndSubStatus2
from . import StatusSubType2Code

class TradeData45(base_types._BaseFieldType):

	__slots__ = ["_CurSts", "_CurStsDtTm", "_CurStsSubTp", "_MsgId", "_PdctTp", "_PrvsSts", "_PrvsStsSubTp", "_StsOrgtr", "_SttlmSsnIdr"]
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
	def StsOrgtr(self):
		return self._StsOrgtr

	@StsOrgtr.setter
	def StsOrgtr(self, value):
		self._StsOrgtr = value if value is not None else base_types.UninitialisedField(self, 'StsOrgtr', Max35Text, False)

	@StsOrgtr.deleter
	def StsOrgtr(self):
		del self._StsOrgtr
		self._StsOrgtr = base_types.UninitialisedField(self, 'StsOrgtr', Max35Text, False)

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
		base_types.FieldEntry(name='CurStsDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CurStsSubTp', type=StatusSubType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsSts', type=Status28Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsStsSubTp', type=StatusSubType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsOrgtr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmSsnIdr', type=Exact4AlphaNumericText, min=0, max=1, mutex_group=None, array=False),
	))