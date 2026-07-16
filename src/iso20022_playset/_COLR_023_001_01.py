# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import TripartyCollateralStatusAdviceV01

class COLR_023_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:colr.023.001.01"
		_docname = "colr.023.001.01"

		__slots__ = ["_TrptyCollStsAdvc"]
		@property
		def TrptyCollStsAdvc(self):
			return self._TrptyCollStsAdvc

		@TrptyCollStsAdvc.setter
		def TrptyCollStsAdvc(self, value):
			self._TrptyCollStsAdvc = value if value is not None else base_types.UninitialisedField(self, 'TrptyCollStsAdvc', TripartyCollateralStatusAdviceV01, False)

		@TrptyCollStsAdvc.deleter
		def TrptyCollStsAdvc(self):
			del self._TrptyCollStsAdvc
			self._TrptyCollStsAdvc = base_types.UninitialisedField(self, 'TrptyCollStsAdvc', TripartyCollateralStatusAdviceV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='TrptyCollStsAdvc', type=TripartyCollateralStatusAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))