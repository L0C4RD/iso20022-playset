# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateAction88
from . import CorporateActionAgent2
from . import CorporateActionGeneralInformation196
from . import CorporateActionNarrative2
from . import CorporateActionNotification12
from . import CorporateActionOption250
from . import DocumentIdentification31
from . import Pagination1

class AgentCANotificationAdviceV03(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_AgtInf", "_CorpActnDtls", "_CorpActnGnlInf", "_CorpActnOptnDtls", "_NtfctnGnlInf", "_Pgntn", "_PrvsNtfctnId"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', CorporateActionNarrative2, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', CorporateActionNarrative2, False)

	@property
	def AgtInf(self):
		return self._AgtInf

	@AgtInf.setter
	def AgtInf(self, value):
		self._AgtInf = value if value is not None else base_types.UninitialisedField(self, 'AgtInf', CorporateActionAgent2, True)

	@AgtInf.deleter
	def AgtInf(self):
		del self._AgtInf
		self._AgtInf = base_types.UninitialisedField(self, 'AgtInf', CorporateActionAgent2, True)

	@property
	def CorpActnDtls(self):
		return self._CorpActnDtls

	@CorpActnDtls.setter
	def CorpActnDtls(self, value):
		self._CorpActnDtls = value if value is not None else base_types.UninitialisedField(self, 'CorpActnDtls', CorporateAction88, False)

	@CorpActnDtls.deleter
	def CorpActnDtls(self):
		del self._CorpActnDtls
		self._CorpActnDtls = base_types.UninitialisedField(self, 'CorpActnDtls', CorporateAction88, False)

	@property
	def CorpActnGnlInf(self):
		return self._CorpActnGnlInf

	@CorpActnGnlInf.setter
	def CorpActnGnlInf(self, value):
		self._CorpActnGnlInf = value if value is not None else base_types.UninitialisedField(self, 'CorpActnGnlInf', CorporateActionGeneralInformation196, False)

	@CorpActnGnlInf.deleter
	def CorpActnGnlInf(self):
		del self._CorpActnGnlInf
		self._CorpActnGnlInf = base_types.UninitialisedField(self, 'CorpActnGnlInf', CorporateActionGeneralInformation196, False)

	@property
	def CorpActnOptnDtls(self):
		return self._CorpActnOptnDtls

	@CorpActnOptnDtls.setter
	def CorpActnOptnDtls(self, value):
		self._CorpActnOptnDtls = value if value is not None else base_types.UninitialisedField(self, 'CorpActnOptnDtls', CorporateActionOption250, True)

	@CorpActnOptnDtls.deleter
	def CorpActnOptnDtls(self):
		del self._CorpActnOptnDtls
		self._CorpActnOptnDtls = base_types.UninitialisedField(self, 'CorpActnOptnDtls', CorporateActionOption250, True)

	@property
	def NtfctnGnlInf(self):
		return self._NtfctnGnlInf

	@NtfctnGnlInf.setter
	def NtfctnGnlInf(self, value):
		self._NtfctnGnlInf = value if value is not None else base_types.UninitialisedField(self, 'NtfctnGnlInf', CorporateActionNotification12, False)

	@NtfctnGnlInf.deleter
	def NtfctnGnlInf(self):
		del self._NtfctnGnlInf
		self._NtfctnGnlInf = base_types.UninitialisedField(self, 'NtfctnGnlInf', CorporateActionNotification12, False)

	@property
	def Pgntn(self):
		return self._Pgntn

	@Pgntn.setter
	def Pgntn(self, value):
		self._Pgntn = value if value is not None else base_types.UninitialisedField(self, 'Pgntn', Pagination1, False)

	@Pgntn.deleter
	def Pgntn(self):
		del self._Pgntn
		self._Pgntn = base_types.UninitialisedField(self, 'Pgntn', Pagination1, False)

	@property
	def PrvsNtfctnId(self):
		return self._PrvsNtfctnId

	@PrvsNtfctnId.setter
	def PrvsNtfctnId(self, value):
		self._PrvsNtfctnId = value if value is not None else base_types.UninitialisedField(self, 'PrvsNtfctnId', DocumentIdentification31, False)

	@PrvsNtfctnId.deleter
	def PrvsNtfctnId(self):
		del self._PrvsNtfctnId
		self._PrvsNtfctnId = base_types.UninitialisedField(self, 'PrvsNtfctnId', DocumentIdentification31, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=CorporateActionNarrative2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgtInf', type=CorporateActionAgent2, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CorpActnDtls', type=CorporateAction88, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionGeneralInformation196, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnOptnDtls', type=CorporateActionOption250, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NtfctnGnlInf', type=CorporateActionNotification12, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pgntn', type=Pagination1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsNtfctnId', type=DocumentIdentification31, min=0, max=1, mutex_group=None, array=False),
	))