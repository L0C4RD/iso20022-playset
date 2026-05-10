from . import base_types
from .DateAndDateTime1Choice import DateAndDateTime1Choice
from .SecuritiesCertificate3 import SecuritiesCertificate3
from .Max35Text import Max35Text

class RegistrationParameters3(base_types._BaseFieldType):

	__slots__ = ["_CertfctnId", "_CertfctnDtTm", "_RegarAcct", "_CertNb"]
	@property
	def CertfctnId(self):
		return self._CertfctnId

	@CertfctnId.setter
	def CertfctnId(self, value):
		self._CertfctnId = value if type(value) != base_types.auto else self.make_default("CertfctnId")

	@CertfctnId.deleter
	def CertfctnId(self):
		del self._CertfctnId
		self._CertfctnId = None

	@property
	def CertfctnDtTm(self):
		return self._CertfctnDtTm

	@CertfctnDtTm.setter
	def CertfctnDtTm(self, value):
		self._CertfctnDtTm = value if type(value) != base_types.auto else self.make_default("CertfctnDtTm")

	@CertfctnDtTm.deleter
	def CertfctnDtTm(self):
		del self._CertfctnDtTm
		self._CertfctnDtTm = None

	@property
	def RegarAcct(self):
		return self._RegarAcct

	@RegarAcct.setter
	def RegarAcct(self, value):
		self._RegarAcct = value if type(value) != base_types.auto else self.make_default("RegarAcct")

	@RegarAcct.deleter
	def RegarAcct(self):
		del self._RegarAcct
		self._RegarAcct = None

	@property
	def CertNb(self):
		return self._CertNb

	@CertNb.setter
	def CertNb(self, value):
		self._CertNb = value if type(value) != base_types.auto else self.make_default("CertNb")

	@CertNb.deleter
	def CertNb(self):
		del self._CertNb
		self._CertNb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CertfctnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertfctnDtTm', type=DateAndDateTime1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegarAcct', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertNb', type=SecuritiesCertificate3, min=0, max=None, mutex_group=None, array=True),
	))

