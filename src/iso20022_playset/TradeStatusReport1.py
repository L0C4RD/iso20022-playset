from . import base_types
import OriginalMessage1
import Max35Text
import UndertakingStatus1Code
import StatusReasonInformation8

class TradeStatusReport1(base_types._BaseFieldType):

	__slots__ = ["_Sts", "_AddtlInf", "_OrgnlMsgDtls", "_StsRsn"]
	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if type(value) != auto else self.make_default("Sts")

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def OrgnlMsgDtls(self):
		return self._OrgnlMsgDtls

	@OrgnlMsgDtls.setter
	def OrgnlMsgDtls(self, value):
		self._OrgnlMsgDtls = value if type(value) != auto else self.make_default("OrgnlMsgDtls")

	@OrgnlMsgDtls.deleter
	def OrgnlMsgDtls(self):
		del self._OrgnlMsgDtls
		self._OrgnlMsgDtls = None

	@property
	def StsRsn(self):
		return self._StsRsn

	@StsRsn.setter
	def StsRsn(self, value):
		self._StsRsn = value if type(value) != auto else self.make_default("StsRsn")

	@StsRsn.deleter
	def StsRsn(self):
		del self._StsRsn
		self._StsRsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Sts', type=UndertakingStatus1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlMsgDtls', type=OriginalMessage1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsRsn', type=StatusReasonInformation8, min=0, max=None, mutex_group=None, array=True),
	))

