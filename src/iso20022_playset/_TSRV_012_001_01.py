# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._UndertakingTerminationNotificationV01 import UndertakingTerminationNotificationV01

class TSRV_012_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsrv.012.001.01"
		_docname = "tsrv.012.001.01"

		__slots__ = ["_UdrtkgTermntnNtfctn"]
		@property
		def UdrtkgTermntnNtfctn(self):
			return self._UdrtkgTermntnNtfctn

		@UdrtkgTermntnNtfctn.setter
		def UdrtkgTermntnNtfctn(self, value):
			self._UdrtkgTermntnNtfctn = value if type(value) != base_types.auto else self.make_default("UdrtkgTermntnNtfctn")

		@UdrtkgTermntnNtfctn.deleter
		def UdrtkgTermntnNtfctn(self):
			del self._UdrtkgTermntnNtfctn
			self._UdrtkgTermntnNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='UdrtkgTermntnNtfctn', type=UndertakingTerminationNotificationV01, min=1, max=1, mutex_group=None, array=False),
		))