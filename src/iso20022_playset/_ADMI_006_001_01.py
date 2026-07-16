# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ResendRequestV01

class ADMI_006_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:admi.006.001.01"
		_docname = "admi.006.001.01"

		__slots__ = ["_RsndReq"]
		@property
		def RsndReq(self):
			return self._RsndReq

		@RsndReq.setter
		def RsndReq(self, value):
			self._RsndReq = value if value is not None else base_types.UninitialisedField(self, 'RsndReq', ResendRequestV01, False)

		@RsndReq.deleter
		def RsndReq(self):
			del self._RsndReq
			self._RsndReq = base_types.UninitialisedField(self, 'RsndReq', ResendRequestV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='RsndReq', type=ResendRequestV01, min=1, max=1, mutex_group=None, array=False),
		))