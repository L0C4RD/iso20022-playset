# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ReversalOfTransferOutConfirmationV09 import ReversalOfTransferOutConfirmationV09

class SESE_004_001_09():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:sese.004.001.09"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_RvslOfTrfOutConf"]
		@property
		def RvslOfTrfOutConf(self):
			return self._RvslOfTrfOutConf

		@RvslOfTrfOutConf.setter
		def RvslOfTrfOutConf(self, value):
			self._RvslOfTrfOutConf = value if type(value) != base_types.auto else self.make_default("RvslOfTrfOutConf")

		@RvslOfTrfOutConf.deleter
		def RvslOfTrfOutConf(self):
			del self._RvslOfTrfOutConf
			self._RvslOfTrfOutConf = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RvslOfTrfOutConf', type=ReversalOfTransferOutConfirmationV09, min=1, max=1, mutex_group=None, array=False),
		))