# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._OrderConfirmationStatusReportV02 import OrderConfirmationStatusReportV02

class SETR_057_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_OrdrConfStsRpt"]
		@property
		def OrdrConfStsRpt(self):
			return self._OrdrConfStsRpt

		@OrdrConfStsRpt.setter
		def OrdrConfStsRpt(self, value):
			self._OrdrConfStsRpt = value if type(value) != base_types.auto else self.make_default("OrdrConfStsRpt")

		@OrdrConfStsRpt.deleter
		def OrdrConfStsRpt(self):
			del self._OrdrConfStsRpt
			self._OrdrConfStsRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='OrdrConfStsRpt', type=OrderConfirmationStatusReportV02, min=1, max=1, mutex_group=None, array=False),
		))