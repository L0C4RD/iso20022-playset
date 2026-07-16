# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import UndertakingAmendmentResponseNotificationV01

class TSRV_009_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsrv.009.001.01"
		_docname = "tsrv.009.001.01"

		__slots__ = ["_UdrtkgAmdmntRspnNtfctn"]
		@property
		def UdrtkgAmdmntRspnNtfctn(self):
			return self._UdrtkgAmdmntRspnNtfctn

		@UdrtkgAmdmntRspnNtfctn.setter
		def UdrtkgAmdmntRspnNtfctn(self, value):
			self._UdrtkgAmdmntRspnNtfctn = value if value is not None else base_types.UninitialisedField(self, 'UdrtkgAmdmntRspnNtfctn', UndertakingAmendmentResponseNotificationV01, False)

		@UdrtkgAmdmntRspnNtfctn.deleter
		def UdrtkgAmdmntRspnNtfctn(self):
			del self._UdrtkgAmdmntRspnNtfctn
			self._UdrtkgAmdmntRspnNtfctn = base_types.UninitialisedField(self, 'UdrtkgAmdmntRspnNtfctn', UndertakingAmendmentResponseNotificationV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='UdrtkgAmdmntRspnNtfctn', type=UndertakingAmendmentResponseNotificationV01, min=1, max=1, mutex_group=None, array=False),
		))