# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GetBusinessDayInformationV05

class CAMT_018_001_05():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.018.001.05"
		_docname = "camt.018.001.05"

		__slots__ = ["_GetBizDayInf"]
		@property
		def GetBizDayInf(self):
			return self._GetBizDayInf

		@GetBizDayInf.setter
		def GetBizDayInf(self, value):
			self._GetBizDayInf = value if value is not None else base_types.UninitialisedField(self, 'GetBizDayInf', GetBusinessDayInformationV05, False)

		@GetBizDayInf.deleter
		def GetBizDayInf(self):
			del self._GetBizDayInf
			self._GetBizDayInf = base_types.UninitialisedField(self, 'GetBizDayInf', GetBusinessDayInformationV05, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='GetBizDayInf', type=GetBusinessDayInformationV05, min=1, max=1, mutex_group=None, array=False),
		))