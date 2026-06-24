# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SubscriptionOrderConfirmationV05 import SubscriptionOrderConfirmationV05

class SETR_012_001_05():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:setr.012.001.05",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_SbcptOrdrConf"]
		@property
		def SbcptOrdrConf(self):
			return self._SbcptOrdrConf

		@SbcptOrdrConf.setter
		def SbcptOrdrConf(self, value):
			self._SbcptOrdrConf = value if type(value) != base_types.auto else self.make_default("SbcptOrdrConf")

		@SbcptOrdrConf.deleter
		def SbcptOrdrConf(self):
			del self._SbcptOrdrConf
			self._SbcptOrdrConf = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SbcptOrdrConf', type=SubscriptionOrderConfirmationV05, min=1, max=1, mutex_group=None, array=False),
		))