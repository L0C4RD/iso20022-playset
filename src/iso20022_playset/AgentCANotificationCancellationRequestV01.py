from . import base_types
import NotificationCancellation1
import CorporateActionNotificationAdvice1
import DocumentIdentification8
import CorporateActionInformation2

class AgentCANotificationCancellationRequestV01(base_types._BaseFieldType):

	__slots__ = ["_CorpActnGnlInf", "_CorpActnNtfctnDtls", "_NtfctnCxlTpAndLkg", "_Id"]
	@property
	def CorpActnGnlInf(self):
		return self._CorpActnGnlInf

	@CorpActnGnlInf.setter
	def CorpActnGnlInf(self, value):
		self._CorpActnGnlInf = value if type(value) != auto else self.make_default("CorpActnGnlInf")

	@CorpActnGnlInf.deleter
	def CorpActnGnlInf(self):
		del self._CorpActnGnlInf
		self._CorpActnGnlInf = None

	@property
	def CorpActnNtfctnDtls(self):
		return self._CorpActnNtfctnDtls

	@CorpActnNtfctnDtls.setter
	def CorpActnNtfctnDtls(self, value):
		self._CorpActnNtfctnDtls = value if type(value) != auto else self.make_default("CorpActnNtfctnDtls")

	@CorpActnNtfctnDtls.deleter
	def CorpActnNtfctnDtls(self):
		del self._CorpActnNtfctnDtls
		self._CorpActnNtfctnDtls = None

	@property
	def NtfctnCxlTpAndLkg(self):
		return self._NtfctnCxlTpAndLkg

	@NtfctnCxlTpAndLkg.setter
	def NtfctnCxlTpAndLkg(self, value):
		self._NtfctnCxlTpAndLkg = value if type(value) != auto else self.make_default("NtfctnCxlTpAndLkg")

	@NtfctnCxlTpAndLkg.deleter
	def NtfctnCxlTpAndLkg(self):
		del self._NtfctnCxlTpAndLkg
		self._NtfctnCxlTpAndLkg = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionInformation2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnNtfctnDtls', type=CorporateActionNotificationAdvice1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtfctnCxlTpAndLkg', type=NotificationCancellation1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=DocumentIdentification8, min=1, max=1, mutex_group=None, array=False),
	))

