# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import TripartyCollateralAllegementNotificationV01

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
			self._TrptyCollAllgmtNtfctn = value if value is not None else base_types.UninitialisedField(self, 'TrptyCollAllgmtNtfctn', TripartyCollateralAllegementNotificationV01, False)

		@TrptyCollAllgmtNtfctn.deleter
		def TrptyCollAllgmtNtfctn(self):
			del self._TrptyCollAllgmtNtfctn
			self._TrptyCollAllgmtNtfctn = base_types.UninitialisedField(self, 'TrptyCollAllgmtNtfctn', TripartyCollateralAllegementNotificationV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='TrptyCollAllgmtNtfctn', type=TripartyCollateralAllegementNotificationV01, min=1, max=1, mutex_group=None, array=False),
		))