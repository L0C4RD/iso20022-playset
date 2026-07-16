# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import OriginalMessage1
from . import StatusReasonInformation8
from . import UndertakingStatus1Code

class TradeStatusReport1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_OrgnlMsgDtls", "_Sts", "_StsRsn"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', Max35Text, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', Max35Text, False)

	@property
	def OrgnlMsgDtls(self):
		return self._OrgnlMsgDtls

	@OrgnlMsgDtls.setter
	def OrgnlMsgDtls(self, value):
		self._OrgnlMsgDtls = value if value is not None else base_types.UninitialisedField(self, 'OrgnlMsgDtls', OriginalMessage1, False)

	@OrgnlMsgDtls.deleter
	def OrgnlMsgDtls(self):
		del self._OrgnlMsgDtls
		self._OrgnlMsgDtls = base_types.UninitialisedField(self, 'OrgnlMsgDtls', OriginalMessage1, False)

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if value is not None else base_types.UninitialisedField(self, 'Sts', UndertakingStatus1Code, False)

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = base_types.UninitialisedField(self, 'Sts', UndertakingStatus1Code, False)

	@property
	def StsRsn(self):
		return self._StsRsn

	@StsRsn.setter
	def StsRsn(self, value):
		self._StsRsn = value if value is not None else base_types.UninitialisedField(self, 'StsRsn', StatusReasonInformation8, True)

	@StsRsn.deleter
	def StsRsn(self):
		del self._StsRsn
		self._StsRsn = base_types.UninitialisedField(self, 'StsRsn', StatusReasonInformation8, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlMsgDtls', type=OriginalMessage1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sts', type=UndertakingStatus1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsRsn', type=StatusReasonInformation8, min=0, max=None, mutex_group=None, array=True),
	))