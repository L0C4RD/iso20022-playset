# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMDeviceControlV04

class CAAM_002_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:caam.002.001.04"
		_docname = "caam.002.001.04"

		__slots__ = ["_ATMDvcCtrl"]
		@property
		def ATMDvcCtrl(self):
			return self._ATMDvcCtrl

		@ATMDvcCtrl.setter
		def ATMDvcCtrl(self, value):
			self._ATMDvcCtrl = value if value is not None else base_types.UninitialisedField(self, 'ATMDvcCtrl', ATMDeviceControlV04, False)

		@ATMDvcCtrl.deleter
		def ATMDvcCtrl(self):
			del self._ATMDvcCtrl
			self._ATMDvcCtrl = base_types.UninitialisedField(self, 'ATMDvcCtrl', ATMDeviceControlV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMDvcCtrl', type=ATMDeviceControlV04, min=1, max=1, mutex_group=None, array=False),
		))