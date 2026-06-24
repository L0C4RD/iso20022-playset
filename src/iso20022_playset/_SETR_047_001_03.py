# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SubscriptionOrderConfirmationCancellationInstructionV03 import SubscriptionOrderConfirmationCancellationInstructionV03

class SETR_047_001_03():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:setr.047.001.03"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_SbcptOrdrConfCxlInstr"]
		@property
		def SbcptOrdrConfCxlInstr(self):
			return self._SbcptOrdrConfCxlInstr

		@SbcptOrdrConfCxlInstr.setter
		def SbcptOrdrConfCxlInstr(self, value):
			self._SbcptOrdrConfCxlInstr = value if type(value) != base_types.auto else self.make_default("SbcptOrdrConfCxlInstr")

		@SbcptOrdrConfCxlInstr.deleter
		def SbcptOrdrConfCxlInstr(self):
			del self._SbcptOrdrConfCxlInstr
			self._SbcptOrdrConfCxlInstr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SbcptOrdrConfCxlInstr', type=SubscriptionOrderConfirmationCancellationInstructionV03, min=1, max=1, mutex_group=None, array=False),
		))