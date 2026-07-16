# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ContractRegistrationConfirmationV04

class AUTH_019_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.019.001.04"
		_docname = "auth.019.001.04"

		__slots__ = ["_CtrctRegnConf"]
		@property
		def CtrctRegnConf(self):
			return self._CtrctRegnConf

		@CtrctRegnConf.setter
		def CtrctRegnConf(self, value):
			self._CtrctRegnConf = value if value is not None else base_types.UninitialisedField(self, 'CtrctRegnConf', ContractRegistrationConfirmationV04, False)

		@CtrctRegnConf.deleter
		def CtrctRegnConf(self):
			del self._CtrctRegnConf
			self._CtrctRegnConf = base_types.UninitialisedField(self, 'CtrctRegnConf', ContractRegistrationConfirmationV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='CtrctRegnConf', type=ContractRegistrationConfirmationV04, min=1, max=1, mutex_group=None, array=False),
		))