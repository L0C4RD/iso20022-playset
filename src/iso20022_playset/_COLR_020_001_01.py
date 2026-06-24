# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._TripartyCollateralTransactionInstructionProcessingStatusAdviceV01 import TripartyCollateralTransactionInstructionProcessingStatusAdviceV01

class COLR_020_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:colr.020.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_TrptyCollTxInstrPrcgStsAdvc"]
		@property
		def TrptyCollTxInstrPrcgStsAdvc(self):
			return self._TrptyCollTxInstrPrcgStsAdvc

		@TrptyCollTxInstrPrcgStsAdvc.setter
		def TrptyCollTxInstrPrcgStsAdvc(self, value):
			self._TrptyCollTxInstrPrcgStsAdvc = value if type(value) != base_types.auto else self.make_default("TrptyCollTxInstrPrcgStsAdvc")

		@TrptyCollTxInstrPrcgStsAdvc.deleter
		def TrptyCollTxInstrPrcgStsAdvc(self):
			del self._TrptyCollTxInstrPrcgStsAdvc
			self._TrptyCollTxInstrPrcgStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='TrptyCollTxInstrPrcgStsAdvc', type=TripartyCollateralTransactionInstructionProcessingStatusAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))