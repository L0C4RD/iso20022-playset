# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import InstructionStatusReturnCriteria1
from . import RequestedIndicator

class PaymentReturnCriteria4(base_types._BaseFieldType):

	__slots__ = ["_CdtDbtInd", "_CdtrAgtInd", "_CdtrInd", "_DbtrAgtInd", "_DbtrInd", "_EndToEndIdInd", "_InstdAmtInd", "_InstdRmbrsmntAgtInd", "_InstgRmbrsmntAgtInd", "_InstrCpyInd", "_InstrInd", "_InstrStsRtrCrit", "_IntrBkSttlmAmtInd", "_IntrBkSttlmDtInd", "_IntrmyInd", "_MsgIdInd", "_PmtMTInd", "_PmtMtdInd", "_PmtTpInd", "_PrcgVldtyTmInd", "_PrtyInd", "_PurpInd", "_ReqdExctnDtInd", "_TxIdInd"]
	@property
	def CdtDbtInd(self):
		return self._CdtDbtInd

	@CdtDbtInd.setter
	def CdtDbtInd(self, value):
		self._CdtDbtInd = value if value is not None else base_types.UninitialisedField(self, 'CdtDbtInd', RequestedIndicator, False)

	@CdtDbtInd.deleter
	def CdtDbtInd(self):
		del self._CdtDbtInd
		self._CdtDbtInd = base_types.UninitialisedField(self, 'CdtDbtInd', RequestedIndicator, False)

	@property
	def CdtrAgtInd(self):
		return self._CdtrAgtInd

	@CdtrAgtInd.setter
	def CdtrAgtInd(self, value):
		self._CdtrAgtInd = value if value is not None else base_types.UninitialisedField(self, 'CdtrAgtInd', RequestedIndicator, False)

	@CdtrAgtInd.deleter
	def CdtrAgtInd(self):
		del self._CdtrAgtInd
		self._CdtrAgtInd = base_types.UninitialisedField(self, 'CdtrAgtInd', RequestedIndicator, False)

	@property
	def CdtrInd(self):
		return self._CdtrInd

	@CdtrInd.setter
	def CdtrInd(self, value):
		self._CdtrInd = value if value is not None else base_types.UninitialisedField(self, 'CdtrInd', RequestedIndicator, False)

	@CdtrInd.deleter
	def CdtrInd(self):
		del self._CdtrInd
		self._CdtrInd = base_types.UninitialisedField(self, 'CdtrInd', RequestedIndicator, False)

	@property
	def DbtrAgtInd(self):
		return self._DbtrAgtInd

	@DbtrAgtInd.setter
	def DbtrAgtInd(self, value):
		self._DbtrAgtInd = value if value is not None else base_types.UninitialisedField(self, 'DbtrAgtInd', RequestedIndicator, False)

	@DbtrAgtInd.deleter
	def DbtrAgtInd(self):
		del self._DbtrAgtInd
		self._DbtrAgtInd = base_types.UninitialisedField(self, 'DbtrAgtInd', RequestedIndicator, False)

	@property
	def DbtrInd(self):
		return self._DbtrInd

	@DbtrInd.setter
	def DbtrInd(self, value):
		self._DbtrInd = value if value is not None else base_types.UninitialisedField(self, 'DbtrInd', RequestedIndicator, False)

	@DbtrInd.deleter
	def DbtrInd(self):
		del self._DbtrInd
		self._DbtrInd = base_types.UninitialisedField(self, 'DbtrInd', RequestedIndicator, False)

	@property
	def EndToEndIdInd(self):
		return self._EndToEndIdInd

	@EndToEndIdInd.setter
	def EndToEndIdInd(self, value):
		self._EndToEndIdInd = value if value is not None else base_types.UninitialisedField(self, 'EndToEndIdInd', RequestedIndicator, False)

	@EndToEndIdInd.deleter
	def EndToEndIdInd(self):
		del self._EndToEndIdInd
		self._EndToEndIdInd = base_types.UninitialisedField(self, 'EndToEndIdInd', RequestedIndicator, False)

	@property
	def InstdAmtInd(self):
		return self._InstdAmtInd

	@InstdAmtInd.setter
	def InstdAmtInd(self, value):
		self._InstdAmtInd = value if value is not None else base_types.UninitialisedField(self, 'InstdAmtInd', RequestedIndicator, False)

	@InstdAmtInd.deleter
	def InstdAmtInd(self):
		del self._InstdAmtInd
		self._InstdAmtInd = base_types.UninitialisedField(self, 'InstdAmtInd', RequestedIndicator, False)

	@property
	def InstdRmbrsmntAgtInd(self):
		return self._InstdRmbrsmntAgtInd

	@InstdRmbrsmntAgtInd.setter
	def InstdRmbrsmntAgtInd(self, value):
		self._InstdRmbrsmntAgtInd = value if value is not None else base_types.UninitialisedField(self, 'InstdRmbrsmntAgtInd', RequestedIndicator, False)

	@InstdRmbrsmntAgtInd.deleter
	def InstdRmbrsmntAgtInd(self):
		del self._InstdRmbrsmntAgtInd
		self._InstdRmbrsmntAgtInd = base_types.UninitialisedField(self, 'InstdRmbrsmntAgtInd', RequestedIndicator, False)

	@property
	def InstgRmbrsmntAgtInd(self):
		return self._InstgRmbrsmntAgtInd

	@InstgRmbrsmntAgtInd.setter
	def InstgRmbrsmntAgtInd(self, value):
		self._InstgRmbrsmntAgtInd = value if value is not None else base_types.UninitialisedField(self, 'InstgRmbrsmntAgtInd', RequestedIndicator, False)

	@InstgRmbrsmntAgtInd.deleter
	def InstgRmbrsmntAgtInd(self):
		del self._InstgRmbrsmntAgtInd
		self._InstgRmbrsmntAgtInd = base_types.UninitialisedField(self, 'InstgRmbrsmntAgtInd', RequestedIndicator, False)

	@property
	def InstrCpyInd(self):
		return self._InstrCpyInd

	@InstrCpyInd.setter
	def InstrCpyInd(self, value):
		self._InstrCpyInd = value if value is not None else base_types.UninitialisedField(self, 'InstrCpyInd', RequestedIndicator, False)

	@InstrCpyInd.deleter
	def InstrCpyInd(self):
		del self._InstrCpyInd
		self._InstrCpyInd = base_types.UninitialisedField(self, 'InstrCpyInd', RequestedIndicator, False)

	@property
	def InstrInd(self):
		return self._InstrInd

	@InstrInd.setter
	def InstrInd(self, value):
		self._InstrInd = value if value is not None else base_types.UninitialisedField(self, 'InstrInd', RequestedIndicator, False)

	@InstrInd.deleter
	def InstrInd(self):
		del self._InstrInd
		self._InstrInd = base_types.UninitialisedField(self, 'InstrInd', RequestedIndicator, False)

	@property
	def InstrStsRtrCrit(self):
		return self._InstrStsRtrCrit

	@InstrStsRtrCrit.setter
	def InstrStsRtrCrit(self, value):
		self._InstrStsRtrCrit = value if value is not None else base_types.UninitialisedField(self, 'InstrStsRtrCrit', InstructionStatusReturnCriteria1, False)

	@InstrStsRtrCrit.deleter
	def InstrStsRtrCrit(self):
		del self._InstrStsRtrCrit
		self._InstrStsRtrCrit = base_types.UninitialisedField(self, 'InstrStsRtrCrit', InstructionStatusReturnCriteria1, False)

	@property
	def IntrBkSttlmAmtInd(self):
		return self._IntrBkSttlmAmtInd

	@IntrBkSttlmAmtInd.setter
	def IntrBkSttlmAmtInd(self, value):
		self._IntrBkSttlmAmtInd = value if value is not None else base_types.UninitialisedField(self, 'IntrBkSttlmAmtInd', RequestedIndicator, False)

	@IntrBkSttlmAmtInd.deleter
	def IntrBkSttlmAmtInd(self):
		del self._IntrBkSttlmAmtInd
		self._IntrBkSttlmAmtInd = base_types.UninitialisedField(self, 'IntrBkSttlmAmtInd', RequestedIndicator, False)

	@property
	def IntrBkSttlmDtInd(self):
		return self._IntrBkSttlmDtInd

	@IntrBkSttlmDtInd.setter
	def IntrBkSttlmDtInd(self, value):
		self._IntrBkSttlmDtInd = value if value is not None else base_types.UninitialisedField(self, 'IntrBkSttlmDtInd', RequestedIndicator, False)

	@IntrBkSttlmDtInd.deleter
	def IntrBkSttlmDtInd(self):
		del self._IntrBkSttlmDtInd
		self._IntrBkSttlmDtInd = base_types.UninitialisedField(self, 'IntrBkSttlmDtInd', RequestedIndicator, False)

	@property
	def IntrmyInd(self):
		return self._IntrmyInd

	@IntrmyInd.setter
	def IntrmyInd(self, value):
		self._IntrmyInd = value if value is not None else base_types.UninitialisedField(self, 'IntrmyInd', RequestedIndicator, False)

	@IntrmyInd.deleter
	def IntrmyInd(self):
		del self._IntrmyInd
		self._IntrmyInd = base_types.UninitialisedField(self, 'IntrmyInd', RequestedIndicator, False)

	@property
	def MsgIdInd(self):
		return self._MsgIdInd

	@MsgIdInd.setter
	def MsgIdInd(self, value):
		self._MsgIdInd = value if value is not None else base_types.UninitialisedField(self, 'MsgIdInd', RequestedIndicator, False)

	@MsgIdInd.deleter
	def MsgIdInd(self):
		del self._MsgIdInd
		self._MsgIdInd = base_types.UninitialisedField(self, 'MsgIdInd', RequestedIndicator, False)

	@property
	def PmtMTInd(self):
		return self._PmtMTInd

	@PmtMTInd.setter
	def PmtMTInd(self, value):
		self._PmtMTInd = value if value is not None else base_types.UninitialisedField(self, 'PmtMTInd', RequestedIndicator, False)

	@PmtMTInd.deleter
	def PmtMTInd(self):
		del self._PmtMTInd
		self._PmtMTInd = base_types.UninitialisedField(self, 'PmtMTInd', RequestedIndicator, False)

	@property
	def PmtMtdInd(self):
		return self._PmtMtdInd

	@PmtMtdInd.setter
	def PmtMtdInd(self, value):
		self._PmtMtdInd = value if value is not None else base_types.UninitialisedField(self, 'PmtMtdInd', RequestedIndicator, False)

	@PmtMtdInd.deleter
	def PmtMtdInd(self):
		del self._PmtMtdInd
		self._PmtMtdInd = base_types.UninitialisedField(self, 'PmtMtdInd', RequestedIndicator, False)

	@property
	def PmtTpInd(self):
		return self._PmtTpInd

	@PmtTpInd.setter
	def PmtTpInd(self, value):
		self._PmtTpInd = value if value is not None else base_types.UninitialisedField(self, 'PmtTpInd', RequestedIndicator, False)

	@PmtTpInd.deleter
	def PmtTpInd(self):
		del self._PmtTpInd
		self._PmtTpInd = base_types.UninitialisedField(self, 'PmtTpInd', RequestedIndicator, False)

	@property
	def PrcgVldtyTmInd(self):
		return self._PrcgVldtyTmInd

	@PrcgVldtyTmInd.setter
	def PrcgVldtyTmInd(self, value):
		self._PrcgVldtyTmInd = value if value is not None else base_types.UninitialisedField(self, 'PrcgVldtyTmInd', RequestedIndicator, False)

	@PrcgVldtyTmInd.deleter
	def PrcgVldtyTmInd(self):
		del self._PrcgVldtyTmInd
		self._PrcgVldtyTmInd = base_types.UninitialisedField(self, 'PrcgVldtyTmInd', RequestedIndicator, False)

	@property
	def PrtyInd(self):
		return self._PrtyInd

	@PrtyInd.setter
	def PrtyInd(self, value):
		self._PrtyInd = value if value is not None else base_types.UninitialisedField(self, 'PrtyInd', RequestedIndicator, False)

	@PrtyInd.deleter
	def PrtyInd(self):
		del self._PrtyInd
		self._PrtyInd = base_types.UninitialisedField(self, 'PrtyInd', RequestedIndicator, False)

	@property
	def PurpInd(self):
		return self._PurpInd

	@PurpInd.setter
	def PurpInd(self, value):
		self._PurpInd = value if value is not None else base_types.UninitialisedField(self, 'PurpInd', RequestedIndicator, False)

	@PurpInd.deleter
	def PurpInd(self):
		del self._PurpInd
		self._PurpInd = base_types.UninitialisedField(self, 'PurpInd', RequestedIndicator, False)

	@property
	def ReqdExctnDtInd(self):
		return self._ReqdExctnDtInd

	@ReqdExctnDtInd.setter
	def ReqdExctnDtInd(self, value):
		self._ReqdExctnDtInd = value if value is not None else base_types.UninitialisedField(self, 'ReqdExctnDtInd', RequestedIndicator, False)

	@ReqdExctnDtInd.deleter
	def ReqdExctnDtInd(self):
		del self._ReqdExctnDtInd
		self._ReqdExctnDtInd = base_types.UninitialisedField(self, 'ReqdExctnDtInd', RequestedIndicator, False)

	@property
	def TxIdInd(self):
		return self._TxIdInd

	@TxIdInd.setter
	def TxIdInd(self, value):
		self._TxIdInd = value if value is not None else base_types.UninitialisedField(self, 'TxIdInd', RequestedIndicator, False)

	@TxIdInd.deleter
	def TxIdInd(self):
		del self._TxIdInd
		self._TxIdInd = base_types.UninitialisedField(self, 'TxIdInd', RequestedIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CdtDbtInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrAgtInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrAgtInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EndToEndIdInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstdAmtInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstdRmbrsmntAgtInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstgRmbrsmntAgtInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrCpyInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrStsRtrCrit', type=InstructionStatusReturnCriteria1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrBkSttlmAmtInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrBkSttlmDtInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgIdInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtMTInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtMtdInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtTpInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgVldtyTmInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtyInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PurpInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdExctnDtInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxIdInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
	))