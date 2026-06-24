# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CollateralDataStatusAdviceV01 import CollateralDataStatusAdviceV01

class REDA_028_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:reda.028.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_CollDataStsAdvc"]
		@property
		def CollDataStsAdvc(self):
			return self._CollDataStsAdvc

		@CollDataStsAdvc.setter
		def CollDataStsAdvc(self, value):
			self._CollDataStsAdvc = value if type(value) != base_types.auto else self.make_default("CollDataStsAdvc")

		@CollDataStsAdvc.deleter
		def CollDataStsAdvc(self):
			del self._CollDataStsAdvc
			self._CollDataStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CollDataStsAdvc', type=CollateralDataStatusAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))