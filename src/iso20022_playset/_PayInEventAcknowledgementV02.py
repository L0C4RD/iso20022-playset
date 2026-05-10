from . import base_types
from ._Max35Text import Max35Text
from ._SupplementaryData1 import SupplementaryData1
from ._AcknowledgementDetails1Choice import AcknowledgementDetails1Choice
from ._Exact4AlphaNumericText import Exact4AlphaNumericText

class PayInEventAcknowledgementV02(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_AckDtls", "_SttlmSsnIdr", "_MsgId"]
	@property
	def AckDtls(self):
		return self._AckDtls

	@AckDtls.setter
	def AckDtls(self, value):
		self._AckDtls = value if type(value) != base_types.auto else self.make_default("AckDtls")

	@AckDtls.deleter
	def AckDtls(self):
		del self._AckDtls
		self._AckDtls = None

	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if type(value) != base_types.auto else self.make_default("MsgId")

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def SttlmSsnIdr(self):
		return self._SttlmSsnIdr

	@SttlmSsnIdr.setter
	def SttlmSsnIdr(self, value):
		self._SttlmSsnIdr = value if type(value) != base_types.auto else self.make_default("SttlmSsnIdr")

	@SttlmSsnIdr.deleter
	def SttlmSsnIdr(self):
		del self._SttlmSsnIdr
		self._SttlmSsnIdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AckDtls', type=AcknowledgementDetails1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttlmSsnIdr', type=Exact4AlphaNumericText, min=0, max=1, mutex_group=None, array=False),
	))

