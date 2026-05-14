# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._UndertakingAmendmentNotificationV01 import UndertakingAmendmentNotificationV01

class TSRV_007_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_UdrtkgAmdmntNtfctn"]
		@property
		def UdrtkgAmdmntNtfctn(self):
			return self._UdrtkgAmdmntNtfctn

		@UdrtkgAmdmntNtfctn.setter
		def UdrtkgAmdmntNtfctn(self, value):
			self._UdrtkgAmdmntNtfctn = value if type(value) != base_types.auto else self.make_default("UdrtkgAmdmntNtfctn")

		@UdrtkgAmdmntNtfctn.deleter
		def UdrtkgAmdmntNtfctn(self):
			del self._UdrtkgAmdmntNtfctn
			self._UdrtkgAmdmntNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='UdrtkgAmdmntNtfctn', type=UndertakingAmendmentNotificationV01, min=1, max=1, mutex_group=None, array=False),
		))