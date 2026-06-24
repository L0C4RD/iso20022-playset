# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._TripartyCollateralTransactionInstructionV01 import TripartyCollateralTransactionInstructionV01

class COLR_019_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:colr.019.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_TrptyCollTxInstr"]
		@property
		def TrptyCollTxInstr(self):
			return self._TrptyCollTxInstr

		@TrptyCollTxInstr.setter
		def TrptyCollTxInstr(self, value):
			self._TrptyCollTxInstr = value if type(value) != base_types.auto else self.make_default("TrptyCollTxInstr")

		@TrptyCollTxInstr.deleter
		def TrptyCollTxInstr(self):
			del self._TrptyCollTxInstr
			self._TrptyCollTxInstr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='TrptyCollTxInstr', type=TripartyCollateralTransactionInstructionV01, min=1, max=1, mutex_group=None, array=False),
		))