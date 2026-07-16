# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import TripartyCollateralUnilateralRemovalRequestV01

class REDA_074_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:reda.074.001.01"
		_docname = "reda.074.001.01"

		__slots__ = ["_TrptyCollUnltrlRmvlReq"]
		@property
		def TrptyCollUnltrlRmvlReq(self):
			return self._TrptyCollUnltrlRmvlReq

		@TrptyCollUnltrlRmvlReq.setter
		def TrptyCollUnltrlRmvlReq(self, value):
			self._TrptyCollUnltrlRmvlReq = value if value is not None else base_types.UninitialisedField(self, 'TrptyCollUnltrlRmvlReq', TripartyCollateralUnilateralRemovalRequestV01, False)

		@TrptyCollUnltrlRmvlReq.deleter
		def TrptyCollUnltrlRmvlReq(self):
			del self._TrptyCollUnltrlRmvlReq
			self._TrptyCollUnltrlRmvlReq = base_types.UninitialisedField(self, 'TrptyCollUnltrlRmvlReq', TripartyCollateralUnilateralRemovalRequestV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='TrptyCollUnltrlRmvlReq', type=TripartyCollateralUnilateralRemovalRequestV01, min=1, max=1, mutex_group=None, array=False),
		))