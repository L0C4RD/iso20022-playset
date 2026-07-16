# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import TripartyCollateralTransactionInstructionV01

class COLR_019_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:colr.019.001.01"
		_docname = "colr.019.001.01"

		__slots__ = ["_TrptyCollTxInstr"]
		@property
		def TrptyCollTxInstr(self):
			return self._TrptyCollTxInstr

		@TrptyCollTxInstr.setter
		def TrptyCollTxInstr(self, value):
			self._TrptyCollTxInstr = value if value is not None else base_types.UninitialisedField(self, 'TrptyCollTxInstr', TripartyCollateralTransactionInstructionV01, False)

		@TrptyCollTxInstr.deleter
		def TrptyCollTxInstr(self):
			del self._TrptyCollTxInstr
			self._TrptyCollTxInstr = base_types.UninitialisedField(self, 'TrptyCollTxInstr', TripartyCollateralTransactionInstructionV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='TrptyCollTxInstr', type=TripartyCollateralTransactionInstructionV01, min=1, max=1, mutex_group=None, array=False),
		))