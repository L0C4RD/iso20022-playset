# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import HostToATMRequestV01

class CAAM_007_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:caam.007.001.01"
		_docname = "caam.007.001.01"

		__slots__ = ["_HstToATMReq"]
		@property
		def HstToATMReq(self):
			return self._HstToATMReq

		@HstToATMReq.setter
		def HstToATMReq(self, value):
			self._HstToATMReq = value if value is not None else base_types.UninitialisedField(self, 'HstToATMReq', HostToATMRequestV01, False)

		@HstToATMReq.deleter
		def HstToATMReq(self):
			del self._HstToATMReq
			self._HstToATMReq = base_types.UninitialisedField(self, 'HstToATMReq', HostToATMRequestV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='HstToATMReq', type=HostToATMRequestV01, min=1, max=1, mutex_group=None, array=False),
		))