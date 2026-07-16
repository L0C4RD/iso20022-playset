# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import TripartyCollateralTransactionInstructionProcessingStatusAdviceV01

class COLR_020_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:colr.020.001.01"
		_docname = "colr.020.001.01"

		__slots__ = ["_TrptyCollTxInstrPrcgStsAdvc"]
		@property
		def TrptyCollTxInstrPrcgStsAdvc(self):
			return self._TrptyCollTxInstrPrcgStsAdvc

		@TrptyCollTxInstrPrcgStsAdvc.setter
		def TrptyCollTxInstrPrcgStsAdvc(self, value):
			self._TrptyCollTxInstrPrcgStsAdvc = value if value is not None else base_types.UninitialisedField(self, 'TrptyCollTxInstrPrcgStsAdvc', TripartyCollateralTransactionInstructionProcessingStatusAdviceV01, False)

		@TrptyCollTxInstrPrcgStsAdvc.deleter
		def TrptyCollTxInstrPrcgStsAdvc(self):
			del self._TrptyCollTxInstrPrcgStsAdvc
			self._TrptyCollTxInstrPrcgStsAdvc = base_types.UninitialisedField(self, 'TrptyCollTxInstrPrcgStsAdvc', TripartyCollateralTransactionInstructionProcessingStatusAdviceV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='TrptyCollTxInstrPrcgStsAdvc', type=TripartyCollateralTransactionInstructionProcessingStatusAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))