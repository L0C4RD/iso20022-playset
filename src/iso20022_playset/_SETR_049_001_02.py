# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SubscriptionBulkOrderConfirmationCancellationInstructionV02 import SubscriptionBulkOrderConfirmationCancellationInstructionV02

class SETR_049_001_02():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:setr.049.001.02"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_SbcptBlkOrdrConfCxlInstr"]
		@property
		def SbcptBlkOrdrConfCxlInstr(self):
			return self._SbcptBlkOrdrConfCxlInstr

		@SbcptBlkOrdrConfCxlInstr.setter
		def SbcptBlkOrdrConfCxlInstr(self, value):
			self._SbcptBlkOrdrConfCxlInstr = value if type(value) != base_types.auto else self.make_default("SbcptBlkOrdrConfCxlInstr")

		@SbcptBlkOrdrConfCxlInstr.deleter
		def SbcptBlkOrdrConfCxlInstr(self):
			del self._SbcptBlkOrdrConfCxlInstr
			self._SbcptBlkOrdrConfCxlInstr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SbcptBlkOrdrConfCxlInstr', type=SubscriptionBulkOrderConfirmationCancellationInstructionV02, min=1, max=1, mutex_group=None, array=False),
		))