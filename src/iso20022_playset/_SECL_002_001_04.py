# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._TradeLegNotificationCancellationV04 import TradeLegNotificationCancellationV04

class SECL_002_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:secl.002.001.04"
		_docname = "secl.002.001.04"

		__slots__ = ["_TradLegNtfctnCxl"]
		@property
		def TradLegNtfctnCxl(self):
			return self._TradLegNtfctnCxl

		@TradLegNtfctnCxl.setter
		def TradLegNtfctnCxl(self, value):
			self._TradLegNtfctnCxl = value if type(value) != base_types.auto else self.make_default("TradLegNtfctnCxl")

		@TradLegNtfctnCxl.deleter
		def TradLegNtfctnCxl(self):
			del self._TradLegNtfctnCxl
			self._TradLegNtfctnCxl = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='TradLegNtfctnCxl', type=TradeLegNotificationCancellationV04, min=1, max=1, mutex_group=None, array=False),
		))