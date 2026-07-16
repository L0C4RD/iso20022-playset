# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RemittanceAdviceV07

class REMT_001_001_07():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:remt.001.001.07"
		_docname = "remt.001.001.07"

		__slots__ = ["_RmtAdvc"]
		@property
		def RmtAdvc(self):
			return self._RmtAdvc

		@RmtAdvc.setter
		def RmtAdvc(self, value):
			self._RmtAdvc = value if value is not None else base_types.UninitialisedField(self, 'RmtAdvc', RemittanceAdviceV07, False)

		@RmtAdvc.deleter
		def RmtAdvc(self):
			del self._RmtAdvc
			self._RmtAdvc = base_types.UninitialisedField(self, 'RmtAdvc', RemittanceAdviceV07, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='RmtAdvc', type=RemittanceAdviceV07, min=1, max=1, mutex_group=None, array=False),
		))