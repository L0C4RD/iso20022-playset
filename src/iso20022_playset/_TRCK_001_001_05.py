# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._PaymentStatusTrackerUpdateV05 import PaymentStatusTrackerUpdateV05

class TRCK_001_001_05():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:trck.001.001.05",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_PmtStsTrckrUpd"]
		@property
		def PmtStsTrckrUpd(self):
			return self._PmtStsTrckrUpd

		@PmtStsTrckrUpd.setter
		def PmtStsTrckrUpd(self, value):
			self._PmtStsTrckrUpd = value if type(value) != base_types.auto else self.make_default("PmtStsTrckrUpd")

		@PmtStsTrckrUpd.deleter
		def PmtStsTrckrUpd(self):
			del self._PmtStsTrckrUpd
			self._PmtStsTrckrUpd = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='PmtStsTrckrUpd', type=PaymentStatusTrackerUpdateV05, min=1, max=1, mutex_group=None, array=False),
		))