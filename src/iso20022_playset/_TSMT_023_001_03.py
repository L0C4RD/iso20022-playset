# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._MisMatchRejectionNotificationV03 import MisMatchRejectionNotificationV03

class TSMT_023_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_MisMtchRjctnNtfctn"]
		@property
		def MisMtchRjctnNtfctn(self):
			return self._MisMtchRjctnNtfctn

		@MisMtchRjctnNtfctn.setter
		def MisMtchRjctnNtfctn(self, value):
			self._MisMtchRjctnNtfctn = value if type(value) != base_types.auto else self.make_default("MisMtchRjctnNtfctn")

		@MisMtchRjctnNtfctn.deleter
		def MisMtchRjctnNtfctn(self):
			del self._MisMtchRjctnNtfctn
			self._MisMtchRjctnNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='MisMtchRjctnNtfctn', type=MisMatchRejectionNotificationV03, min=1, max=1, mutex_group=None, array=False),
		))