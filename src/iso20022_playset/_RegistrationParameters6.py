# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateAndDateTime2Choice
from . import Max35Text
from . import SecuritiesCertificate4

class RegistrationParameters6(base_types._BaseFieldType):

	__slots__ = ["_CertNb", "_CertfctnDtTm", "_CertfctnId", "_RegarAcct"]
	@property
	def CertNb(self):
		return self._CertNb

	@CertNb.setter
	def CertNb(self, value):
		self._CertNb = value if value is not None else base_types.UninitialisedField(self, 'CertNb', SecuritiesCertificate4, True)

	@CertNb.deleter
	def CertNb(self):
		del self._CertNb
		self._CertNb = base_types.UninitialisedField(self, 'CertNb', SecuritiesCertificate4, True)

	@property
	def CertfctnDtTm(self):
		return self._CertfctnDtTm

	@CertfctnDtTm.setter
	def CertfctnDtTm(self, value):
		self._CertfctnDtTm = value if value is not None else base_types.UninitialisedField(self, 'CertfctnDtTm', DateAndDateTime2Choice, False)

	@CertfctnDtTm.deleter
	def CertfctnDtTm(self):
		del self._CertfctnDtTm
		self._CertfctnDtTm = base_types.UninitialisedField(self, 'CertfctnDtTm', DateAndDateTime2Choice, False)

	@property
	def CertfctnId(self):
		return self._CertfctnId

	@CertfctnId.setter
	def CertfctnId(self, value):
		self._CertfctnId = value if value is not None else base_types.UninitialisedField(self, 'CertfctnId', Max35Text, False)

	@CertfctnId.deleter
	def CertfctnId(self):
		del self._CertfctnId
		self._CertfctnId = base_types.UninitialisedField(self, 'CertfctnId', Max35Text, False)

	@property
	def RegarAcct(self):
		return self._RegarAcct

	@RegarAcct.setter
	def RegarAcct(self, value):
		self._RegarAcct = value if value is not None else base_types.UninitialisedField(self, 'RegarAcct', Max35Text, False)

	@RegarAcct.deleter
	def RegarAcct(self):
		del self._RegarAcct
		self._RegarAcct = base_types.UninitialisedField(self, 'RegarAcct', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CertNb', type=SecuritiesCertificate4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CertfctnDtTm', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertfctnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegarAcct', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))