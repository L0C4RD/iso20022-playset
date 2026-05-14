# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CurrencyControlSupportingDocumentDeliveryV04 import CurrencyControlSupportingDocumentDeliveryV04

class AUTH_025_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CcyCtrlSpprtgDocDlvry"]
		@property
		def CcyCtrlSpprtgDocDlvry(self):
			return self._CcyCtrlSpprtgDocDlvry

		@CcyCtrlSpprtgDocDlvry.setter
		def CcyCtrlSpprtgDocDlvry(self, value):
			self._CcyCtrlSpprtgDocDlvry = value if type(value) != base_types.auto else self.make_default("CcyCtrlSpprtgDocDlvry")

		@CcyCtrlSpprtgDocDlvry.deleter
		def CcyCtrlSpprtgDocDlvry(self):
			del self._CcyCtrlSpprtgDocDlvry
			self._CcyCtrlSpprtgDocDlvry = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CcyCtrlSpprtgDocDlvry', type=CurrencyControlSupportingDocumentDeliveryV04, min=1, max=1, mutex_group=None, array=False),
		))