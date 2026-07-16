# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import HostToATMAcknowledgementV01

class CAAM_008_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:caam.008.001.01"
		_docname = "caam.008.001.01"

		__slots__ = ["_HstToATMAck"]
		@property
		def HstToATMAck(self):
			return self._HstToATMAck

		@HstToATMAck.setter
		def HstToATMAck(self, value):
			self._HstToATMAck = value if value is not None else base_types.UninitialisedField(self, 'HstToATMAck', HostToATMAcknowledgementV01, False)

		@HstToATMAck.deleter
		def HstToATMAck(self):
			del self._HstToATMAck
			self._HstToATMAck = base_types.UninitialisedField(self, 'HstToATMAck', HostToATMAcknowledgementV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='HstToATMAck', type=HostToATMAcknowledgementV01, min=1, max=1, mutex_group=None, array=False),
		))