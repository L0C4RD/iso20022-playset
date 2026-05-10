import base_types
import InstructionStatusReturnCriteria1
import RequestedIndicator

class PaymentReturnCriteria4(base_types._BaseFieldType):

	__slots__ = ["_CdtDbtInd", "_TxIdInd", "_CdtrAgtInd", "_PurpInd", "_DbtrInd", "_ReqdExctnDtInd", "_EndToEndIdInd", "_CdtrInd", "_InstrInd", "_InstdAmtInd", "_InstrCpyInd", "_DbtrAgtInd", "_PmtMtdInd", "_IntrBkSttlmAmtInd", "_PmtTpInd", "_MsgIdInd", "_InstdRmbrsmntAgtInd", "_IntrBkSttlmDtInd", "_PrcgVldtyTmInd", "_PrtyInd", "_InstrStsRtrCrit", "_PmtMTInd", "_InstgRmbrsmntAgtInd", "_IntrmyInd"]
	@property
	def CdtDbtInd(self):
		return self._CdtDbtInd

	@CdtDbtInd.setter
	def CdtDbtInd(self, value):
		self._CdtDbtInd = value if type(value) != auto else self.make_default("CdtDbtInd")

	@CdtDbtInd.deleter
	def CdtDbtInd(self):
		del self._CdtDbtInd
		self._CdtDbtInd = None

	@property
	def TxIdInd(self):
		return self._TxIdInd

	@TxIdInd.setter
	def TxIdInd(self, value):
		self._TxIdInd = value if type(value) != auto else self.make_default("TxIdInd")

	@TxIdInd.deleter
	def TxIdInd(self):
		del self._TxIdInd
		self._TxIdInd = None

	@property
	def CdtrAgtInd(self):
		return self._CdtrAgtInd

	@CdtrAgtInd.setter
	def CdtrAgtInd(self, value):
		self._CdtrAgtInd = value if type(value) != auto else self.make_default("CdtrAgtInd")

	@CdtrAgtInd.deleter
	def CdtrAgtInd(self):
		del self._CdtrAgtInd
		self._CdtrAgtInd = None

	@property
	def PurpInd(self):
		return self._PurpInd

	@PurpInd.setter
	def PurpInd(self, value):
		self._PurpInd = value if type(value) != auto else self.make_default("PurpInd")

	@PurpInd.deleter
	def PurpInd(self):
		del self._PurpInd
		self._PurpInd = None

	@property
	def DbtrInd(self):
		return self._DbtrInd

	@DbtrInd.setter
	def DbtrInd(self, value):
		self._DbtrInd = value if type(value) != auto else self.make_default("DbtrInd")

	@DbtrInd.deleter
	def DbtrInd(self):
		del self._DbtrInd
		self._DbtrInd = None

	@property
	def ReqdExctnDtInd(self):
		return self._ReqdExctnDtInd

	@ReqdExctnDtInd.setter
	def ReqdExctnDtInd(self, value):
		self._ReqdExctnDtInd = value if type(value) != auto else self.make_default("ReqdExctnDtInd")

	@ReqdExctnDtInd.deleter
	def ReqdExctnDtInd(self):
		del self._ReqdExctnDtInd
		self._ReqdExctnDtInd = None

	@property
	def EndToEndIdInd(self):
		return self._EndToEndIdInd

	@EndToEndIdInd.setter
	def EndToEndIdInd(self, value):
		self._EndToEndIdInd = value if type(value) != auto else self.make_default("EndToEndIdInd")

	@EndToEndIdInd.deleter
	def EndToEndIdInd(self):
		del self._EndToEndIdInd
		self._EndToEndIdInd = None

	@property
	def CdtrInd(self):
		return self._CdtrInd

	@CdtrInd.setter
	def CdtrInd(self, value):
		self._CdtrInd = value if type(value) != auto else self.make_default("CdtrInd")

	@CdtrInd.deleter
	def CdtrInd(self):
		del self._CdtrInd
		self._CdtrInd = None

	@property
	def InstrInd(self):
		return self._InstrInd

	@InstrInd.setter
	def InstrInd(self, value):
		self._InstrInd = value if type(value) != auto else self.make_default("InstrInd")

	@InstrInd.deleter
	def InstrInd(self):
		del self._InstrInd
		self._InstrInd = None

	@property
	def InstdAmtInd(self):
		return self._InstdAmtInd

	@InstdAmtInd.setter
	def InstdAmtInd(self, value):
		self._InstdAmtInd = value if type(value) != auto else self.make_default("InstdAmtInd")

	@InstdAmtInd.deleter
	def InstdAmtInd(self):
		del self._InstdAmtInd
		self._InstdAmtInd = None

	@property
	def InstrCpyInd(self):
		return self._InstrCpyInd

	@InstrCpyInd.setter
	def InstrCpyInd(self, value):
		self._InstrCpyInd = value if type(value) != auto else self.make_default("InstrCpyInd")

	@InstrCpyInd.deleter
	def InstrCpyInd(self):
		del self._InstrCpyInd
		self._InstrCpyInd = None

	@property
	def DbtrAgtInd(self):
		return self._DbtrAgtInd

	@DbtrAgtInd.setter
	def DbtrAgtInd(self, value):
		self._DbtrAgtInd = value if type(value) != auto else self.make_default("DbtrAgtInd")

	@DbtrAgtInd.deleter
	def DbtrAgtInd(self):
		del self._DbtrAgtInd
		self._DbtrAgtInd = None

	@property
	def PmtMtdInd(self):
		return self._PmtMtdInd

	@PmtMtdInd.setter
	def PmtMtdInd(self, value):
		self._PmtMtdInd = value if type(value) != auto else self.make_default("PmtMtdInd")

	@PmtMtdInd.deleter
	def PmtMtdInd(self):
		del self._PmtMtdInd
		self._PmtMtdInd = None

	@property
	def IntrBkSttlmAmtInd(self):
		return self._IntrBkSttlmAmtInd

	@IntrBkSttlmAmtInd.setter
	def IntrBkSttlmAmtInd(self, value):
		self._IntrBkSttlmAmtInd = value if type(value) != auto else self.make_default("IntrBkSttlmAmtInd")

	@IntrBkSttlmAmtInd.deleter
	def IntrBkSttlmAmtInd(self):
		del self._IntrBkSttlmAmtInd
		self._IntrBkSttlmAmtInd = None

	@property
	def PmtTpInd(self):
		return self._PmtTpInd

	@PmtTpInd.setter
	def PmtTpInd(self, value):
		self._PmtTpInd = value if type(value) != auto else self.make_default("PmtTpInd")

	@PmtTpInd.deleter
	def PmtTpInd(self):
		del self._PmtTpInd
		self._PmtTpInd = None

	@property
	def MsgIdInd(self):
		return self._MsgIdInd

	@MsgIdInd.setter
	def MsgIdInd(self, value):
		self._MsgIdInd = value if type(value) != auto else self.make_default("MsgIdInd")

	@MsgIdInd.deleter
	def MsgIdInd(self):
		del self._MsgIdInd
		self._MsgIdInd = None

	@property
	def InstdRmbrsmntAgtInd(self):
		return self._InstdRmbrsmntAgtInd

	@InstdRmbrsmntAgtInd.setter
	def InstdRmbrsmntAgtInd(self, value):
		self._InstdRmbrsmntAgtInd = value if type(value) != auto else self.make_default("InstdRmbrsmntAgtInd")

	@InstdRmbrsmntAgtInd.deleter
	def InstdRmbrsmntAgtInd(self):
		del self._InstdRmbrsmntAgtInd
		self._InstdRmbrsmntAgtInd = None

	@property
	def IntrBkSttlmDtInd(self):
		return self._IntrBkSttlmDtInd

	@IntrBkSttlmDtInd.setter
	def IntrBkSttlmDtInd(self, value):
		self._IntrBkSttlmDtInd = value if type(value) != auto else self.make_default("IntrBkSttlmDtInd")

	@IntrBkSttlmDtInd.deleter
	def IntrBkSttlmDtInd(self):
		del self._IntrBkSttlmDtInd
		self._IntrBkSttlmDtInd = None

	@property
	def PrcgVldtyTmInd(self):
		return self._PrcgVldtyTmInd

	@PrcgVldtyTmInd.setter
	def PrcgVldtyTmInd(self, value):
		self._PrcgVldtyTmInd = value if type(value) != auto else self.make_default("PrcgVldtyTmInd")

	@PrcgVldtyTmInd.deleter
	def PrcgVldtyTmInd(self):
		del self._PrcgVldtyTmInd
		self._PrcgVldtyTmInd = None

	@property
	def PrtyInd(self):
		return self._PrtyInd

	@PrtyInd.setter
	def PrtyInd(self, value):
		self._PrtyInd = value if type(value) != auto else self.make_default("PrtyInd")

	@PrtyInd.deleter
	def PrtyInd(self):
		del self._PrtyInd
		self._PrtyInd = None

	@property
	def InstrStsRtrCrit(self):
		return self._InstrStsRtrCrit

	@InstrStsRtrCrit.setter
	def InstrStsRtrCrit(self, value):
		self._InstrStsRtrCrit = value if type(value) != auto else self.make_default("InstrStsRtrCrit")

	@InstrStsRtrCrit.deleter
	def InstrStsRtrCrit(self):
		del self._InstrStsRtrCrit
		self._InstrStsRtrCrit = None

	@property
	def PmtMTInd(self):
		return self._PmtMTInd

	@PmtMTInd.setter
	def PmtMTInd(self, value):
		self._PmtMTInd = value if type(value) != auto else self.make_default("PmtMTInd")

	@PmtMTInd.deleter
	def PmtMTInd(self):
		del self._PmtMTInd
		self._PmtMTInd = None

	@property
	def InstgRmbrsmntAgtInd(self):
		return self._InstgRmbrsmntAgtInd

	@InstgRmbrsmntAgtInd.setter
	def InstgRmbrsmntAgtInd(self, value):
		self._InstgRmbrsmntAgtInd = value if type(value) != auto else self.make_default("InstgRmbrsmntAgtInd")

	@InstgRmbrsmntAgtInd.deleter
	def InstgRmbrsmntAgtInd(self):
		del self._InstgRmbrsmntAgtInd
		self._InstgRmbrsmntAgtInd = None

	@property
	def IntrmyInd(self):
		return self._IntrmyInd

	@IntrmyInd.setter
	def IntrmyInd(self, value):
		self._IntrmyInd = value if type(value) != auto else self.make_default("IntrmyInd")

	@IntrmyInd.deleter
	def IntrmyInd(self):
		del self._IntrmyInd
		self._IntrmyInd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CdtDbtInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxIdInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrAgtInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PurpInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdExctnDtInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EndToEndIdInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstdAmtInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrCpyInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrAgtInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtMtdInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrBkSttlmAmtInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtTpInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgIdInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstdRmbrsmntAgtInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrBkSttlmDtInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgVldtyTmInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtyInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrStsRtrCrit', type=InstructionStatusReturnCriteria1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtMTInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstgRmbrsmntAgtInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
	))

