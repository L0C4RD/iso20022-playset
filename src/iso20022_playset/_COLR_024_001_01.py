# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._TripartyCollateralAllegementNotificationCancellationAdviceV01 import TripartyCollateralAllegementNotificationCancellationAdviceV01

class COLR_024_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:colr.024.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_TrptyCollAllgmtNtfctnCxlAdvc"]
		@property
		def TrptyCollAllgmtNtfctnCxlAdvc(self):
			return self._TrptyCollAllgmtNtfctnCxlAdvc

		@TrptyCollAllgmtNtfctnCxlAdvc.setter
		def TrptyCollAllgmtNtfctnCxlAdvc(self, value):
			self._TrptyCollAllgmtNtfctnCxlAdvc = value if type(value) != base_types.auto else self.make_default("TrptyCollAllgmtNtfctnCxlAdvc")

		@TrptyCollAllgmtNtfctnCxlAdvc.deleter
		def TrptyCollAllgmtNtfctnCxlAdvc(self):
			del self._TrptyCollAllgmtNtfctnCxlAdvc
			self._TrptyCollAllgmtNtfctnCxlAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='TrptyCollAllgmtNtfctnCxlAdvc', type=TripartyCollateralAllegementNotificationCancellationAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))