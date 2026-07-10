# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._TripartyCollateralAllegementNotificationV01 import TripartyCollateralAllegementNotificationV01

class COLR_021_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:colr.021.001.01"
		_docname = "colr.021.001.01"

		__slots__ = ["_TrptyCollAllgmtNtfctn"]
		@property
		def TrptyCollAllgmtNtfctn(self):
			return self._TrptyCollAllgmtNtfctn

		@TrptyCollAllgmtNtfctn.setter
		def TrptyCollAllgmtNtfctn(self, value):
			self._TrptyCollAllgmtNtfctn = value if type(value) != base_types.auto else self.make_default("TrptyCollAllgmtNtfctn")

		@TrptyCollAllgmtNtfctn.deleter
		def TrptyCollAllgmtNtfctn(self):
			del self._TrptyCollAllgmtNtfctn
			self._TrptyCollAllgmtNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='TrptyCollAllgmtNtfctn', type=TripartyCollateralAllegementNotificationV01, min=1, max=1, mutex_group=None, array=False),
		))