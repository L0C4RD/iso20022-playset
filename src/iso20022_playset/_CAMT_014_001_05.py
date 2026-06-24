# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ReturnMemberV05 import ReturnMemberV05

class CAMT_014_001_05():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:camt.014.001.05",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_RtrMmb"]
		@property
		def RtrMmb(self):
			return self._RtrMmb

		@RtrMmb.setter
		def RtrMmb(self, value):
			self._RtrMmb = value if type(value) != base_types.auto else self.make_default("RtrMmb")

		@RtrMmb.deleter
		def RtrMmb(self):
			del self._RtrMmb
			self._RtrMmb = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RtrMmb', type=ReturnMemberV05, min=1, max=1, mutex_group=None, array=False),
		))