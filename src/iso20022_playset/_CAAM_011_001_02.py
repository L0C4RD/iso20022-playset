# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMExceptionAdviceV02

class CAAM_011_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:caam.011.001.02"
		_docname = "caam.011.001.02"

		__slots__ = ["_ATMXcptnAdvc"]
		@property
		def ATMXcptnAdvc(self):
			return self._ATMXcptnAdvc

		@ATMXcptnAdvc.setter
		def ATMXcptnAdvc(self, value):
			self._ATMXcptnAdvc = value if value is not None else base_types.UninitialisedField(self, 'ATMXcptnAdvc', ATMExceptionAdviceV02, False)

		@ATMXcptnAdvc.deleter
		def ATMXcptnAdvc(self):
			del self._ATMXcptnAdvc
			self._ATMXcptnAdvc = base_types.UninitialisedField(self, 'ATMXcptnAdvc', ATMExceptionAdviceV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMXcptnAdvc', type=ATMExceptionAdviceV02, min=1, max=1, mutex_group=None, array=False),
		))