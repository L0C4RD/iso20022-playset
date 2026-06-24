# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CollateralValueQueryV02 import CollateralValueQueryV02

class COLR_001_001_02():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:colr.001.001.02",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_CollValQry"]
		@property
		def CollValQry(self):
			return self._CollValQry

		@CollValQry.setter
		def CollValQry(self, value):
			self._CollValQry = value if type(value) != base_types.auto else self.make_default("CollValQry")

		@CollValQry.deleter
		def CollValQry(self):
			del self._CollValQry
			self._CollValQry = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CollValQry', type=CollateralValueQueryV02, min=1, max=1, mutex_group=None, array=False),
		))