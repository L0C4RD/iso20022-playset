# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesBalanceCustodyReport002V11

class SEMT_002_002_11():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:semt.002.002.11"
		_docname = "semt.002.002.11"

		__slots__ = ["_SctiesBalCtdyRpt"]
		@property
		def SctiesBalCtdyRpt(self):
			return self._SctiesBalCtdyRpt

		@SctiesBalCtdyRpt.setter
		def SctiesBalCtdyRpt(self, value):
			self._SctiesBalCtdyRpt = value if value is not None else base_types.UninitialisedField(self, 'SctiesBalCtdyRpt', SecuritiesBalanceCustodyReport002V11, False)

		@SctiesBalCtdyRpt.deleter
		def SctiesBalCtdyRpt(self):
			del self._SctiesBalCtdyRpt
			self._SctiesBalCtdyRpt = base_types.UninitialisedField(self, 'SctiesBalCtdyRpt', SecuritiesBalanceCustodyReport002V11, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesBalCtdyRpt', type=SecuritiesBalanceCustodyReport002V11, min=1, max=1, mutex_group=None, array=False),
		))