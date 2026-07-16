# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BuyerProtectionInstructionAllegementRemovalAdviceV01

class SEEV_065_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:seev.065.001.01"
		_docname = "seev.065.001.01"

		__slots__ = ["_BuyrPrtcnInstrAllgmtRmvlAdvc"]
		@property
		def BuyrPrtcnInstrAllgmtRmvlAdvc(self):
			return self._BuyrPrtcnInstrAllgmtRmvlAdvc

		@BuyrPrtcnInstrAllgmtRmvlAdvc.setter
		def BuyrPrtcnInstrAllgmtRmvlAdvc(self, value):
			self._BuyrPrtcnInstrAllgmtRmvlAdvc = value if value is not None else base_types.UninitialisedField(self, 'BuyrPrtcnInstrAllgmtRmvlAdvc', BuyerProtectionInstructionAllegementRemovalAdviceV01, False)

		@BuyrPrtcnInstrAllgmtRmvlAdvc.deleter
		def BuyrPrtcnInstrAllgmtRmvlAdvc(self):
			del self._BuyrPrtcnInstrAllgmtRmvlAdvc
			self._BuyrPrtcnInstrAllgmtRmvlAdvc = base_types.UninitialisedField(self, 'BuyrPrtcnInstrAllgmtRmvlAdvc', BuyerProtectionInstructionAllegementRemovalAdviceV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='BuyrPrtcnInstrAllgmtRmvlAdvc', type=BuyerProtectionInstructionAllegementRemovalAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))