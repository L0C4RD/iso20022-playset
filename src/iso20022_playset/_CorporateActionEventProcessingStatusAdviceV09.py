# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CorporateActionGeneralInformation182 import CorporateActionGeneralInformation182
from ._CorporateActionNarrative10 import CorporateActionNarrative10
from ._DocumentIdentification33 import DocumentIdentification33
from ._DocumentIdentification9 import DocumentIdentification9
from ._EventProcessingStatus7Choice import EventProcessingStatus7Choice
from ._SupplementaryData1 import SupplementaryData1

class CorporateActionEventProcessingStatusAdviceV09(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_CorpActnGnlInf", "_EvtPrcgSts", "_NtfctnId", "_OthrDocId", "_SplmtryData"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != base_types.auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def CorpActnGnlInf(self):
		return self._CorpActnGnlInf

	@CorpActnGnlInf.setter
	def CorpActnGnlInf(self, value):
		self._CorpActnGnlInf = value if type(value) != base_types.auto else self.make_default("CorpActnGnlInf")

	@CorpActnGnlInf.deleter
	def CorpActnGnlInf(self):
		del self._CorpActnGnlInf
		self._CorpActnGnlInf = None

	@property
	def EvtPrcgSts(self):
		return self._EvtPrcgSts

	@EvtPrcgSts.setter
	def EvtPrcgSts(self, value):
		self._EvtPrcgSts = value if type(value) != base_types.auto else self.make_default("EvtPrcgSts")

	@EvtPrcgSts.deleter
	def EvtPrcgSts(self):
		del self._EvtPrcgSts
		self._EvtPrcgSts = None

	@property
	def NtfctnId(self):
		return self._NtfctnId

	@NtfctnId.setter
	def NtfctnId(self, value):
		self._NtfctnId = value if type(value) != base_types.auto else self.make_default("NtfctnId")

	@NtfctnId.deleter
	def NtfctnId(self):
		del self._NtfctnId
		self._NtfctnId = None

	@property
	def OthrDocId(self):
		return self._OthrDocId

	@OthrDocId.setter
	def OthrDocId(self, value):
		self._OthrDocId = value if type(value) != base_types.auto else self.make_default("OthrDocId")

	@OthrDocId.deleter
	def OthrDocId(self):
		del self._OthrDocId
		self._OthrDocId = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=CorporateActionNarrative10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionGeneralInformation182, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtPrcgSts', type=EventProcessingStatus7Choice, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NtfctnId', type=DocumentIdentification9, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrDocId', type=DocumentIdentification33, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))