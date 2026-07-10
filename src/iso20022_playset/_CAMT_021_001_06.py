# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ReturnGeneralBusinessInformationV06 import ReturnGeneralBusinessInformationV06

class CAMT_021_001_06():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.021.001.06"
		_docname = "camt.021.001.06"

		__slots__ = ["_RtrGnlBizInf"]
		@property
		def RtrGnlBizInf(self):
			return self._RtrGnlBizInf

		@RtrGnlBizInf.setter
		def RtrGnlBizInf(self, value):
			self._RtrGnlBizInf = value if type(value) != base_types.auto else self.make_default("RtrGnlBizInf")

		@RtrGnlBizInf.deleter
		def RtrGnlBizInf(self):
			del self._RtrGnlBizInf
			self._RtrGnlBizInf = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RtrGnlBizInf', type=ReturnGeneralBusinessInformationV06, min=1, max=1, mutex_group=None, array=False),
		))