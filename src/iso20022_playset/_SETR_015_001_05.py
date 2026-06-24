# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SwitchOrderConfirmationV05 import SwitchOrderConfirmationV05

class SETR_015_001_05():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:setr.015.001.05",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_SwtchOrdrConf"]
		@property
		def SwtchOrdrConf(self):
			return self._SwtchOrdrConf

		@SwtchOrdrConf.setter
		def SwtchOrdrConf(self, value):
			self._SwtchOrdrConf = value if type(value) != base_types.auto else self.make_default("SwtchOrdrConf")

		@SwtchOrdrConf.deleter
		def SwtchOrdrConf(self):
			del self._SwtchOrdrConf
			self._SwtchOrdrConf = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SwtchOrdrConf', type=SwitchOrderConfirmationV05, min=1, max=1, mutex_group=None, array=False),
		))