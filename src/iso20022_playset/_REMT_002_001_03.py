# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RemittanceLocationAdviceV03

class REMT_002_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:remt.002.001.03"
		_docname = "remt.002.001.03"

		__slots__ = ["_RmtLctnAdvc"]
		@property
		def RmtLctnAdvc(self):
			return self._RmtLctnAdvc

		@RmtLctnAdvc.setter
		def RmtLctnAdvc(self, value):
			self._RmtLctnAdvc = value if value is not None else base_types.UninitialisedField(self, 'RmtLctnAdvc', RemittanceLocationAdviceV03, False)

		@RmtLctnAdvc.deleter
		def RmtLctnAdvc(self):
			del self._RmtLctnAdvc
			self._RmtLctnAdvc = base_types.UninitialisedField(self, 'RmtLctnAdvc', RemittanceLocationAdviceV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='RmtLctnAdvc', type=RemittanceLocationAdviceV03, min=1, max=1, mutex_group=None, array=False),
		))