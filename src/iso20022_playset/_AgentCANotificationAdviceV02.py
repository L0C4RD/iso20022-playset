from . import base_types
from .CorporateActionNotification12 import CorporateActionNotification12
from .DocumentIdentification31 import DocumentIdentification31
from .CorporateActionAgent2 import CorporateActionAgent2
from .CorporateActionOption235 import CorporateActionOption235
from .Pagination1 import Pagination1
from .CorporateActionGeneralInformation172 import CorporateActionGeneralInformation172
from .CorporateActionNarrative2 import CorporateActionNarrative2
from .CorporateAction83 import CorporateAction83

class AgentCANotificationAdviceV02(base_types._BaseFieldType):

	__slots__ = ["_CorpActnOptnDtls", "_CorpActnDtls", "_AgtInf", "_NtfctnGnlInf", "_AddtlInf", "_CorpActnGnlInf", "_PrvsNtfctnId", "_Pgntn"]
	@property
	def CorpActnOptnDtls(self):
		return self._CorpActnOptnDtls

	@CorpActnOptnDtls.setter
	def CorpActnOptnDtls(self, value):
		self._CorpActnOptnDtls = value if type(value) != base_types.auto else self.make_default("CorpActnOptnDtls")

	@CorpActnOptnDtls.deleter
	def CorpActnOptnDtls(self):
		del self._CorpActnOptnDtls
		self._CorpActnOptnDtls = None

	@property
	def CorpActnDtls(self):
		return self._CorpActnDtls

	@CorpActnDtls.setter
	def CorpActnDtls(self, value):
		self._CorpActnDtls = value if type(value) != base_types.auto else self.make_default("CorpActnDtls")

	@CorpActnDtls.deleter
	def CorpActnDtls(self):
		del self._CorpActnDtls
		self._CorpActnDtls = None

	@property
	def AgtInf(self):
		return self._AgtInf

	@AgtInf.setter
	def AgtInf(self, value):
		self._AgtInf = value if type(value) != base_types.auto else self.make_default("AgtInf")

	@AgtInf.deleter
	def AgtInf(self):
		del self._AgtInf
		self._AgtInf = None

	@property
	def NtfctnGnlInf(self):
		return self._NtfctnGnlInf

	@NtfctnGnlInf.setter
	def NtfctnGnlInf(self, value):
		self._NtfctnGnlInf = value if type(value) != base_types.auto else self.make_default("NtfctnGnlInf")

	@NtfctnGnlInf.deleter
	def NtfctnGnlInf(self):
		del self._NtfctnGnlInf
		self._NtfctnGnlInf = None

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
	def PrvsNtfctnId(self):
		return self._PrvsNtfctnId

	@PrvsNtfctnId.setter
	def PrvsNtfctnId(self, value):
		self._PrvsNtfctnId = value if type(value) != base_types.auto else self.make_default("PrvsNtfctnId")

	@PrvsNtfctnId.deleter
	def PrvsNtfctnId(self):
		del self._PrvsNtfctnId
		self._PrvsNtfctnId = None

	@property
	def Pgntn(self):
		return self._Pgntn

	@Pgntn.setter
	def Pgntn(self, value):
		self._Pgntn = value if type(value) != base_types.auto else self.make_default("Pgntn")

	@Pgntn.deleter
	def Pgntn(self):
		del self._Pgntn
		self._Pgntn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CorpActnOptnDtls', type=CorporateActionOption235, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CorpActnDtls', type=CorporateAction83, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgtInf', type=CorporateActionAgent2, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NtfctnGnlInf', type=CorporateActionNotification12, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=CorporateActionNarrative2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionGeneralInformation172, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsNtfctnId', type=DocumentIdentification31, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pgntn', type=Pagination1, min=0, max=1, mutex_group=None, array=False),
	))

