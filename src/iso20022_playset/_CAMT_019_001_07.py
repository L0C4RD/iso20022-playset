# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ReturnBusinessDayInformationV07

class CAMT_019_001_07():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07"
		_docname = "camt.019.001.07"

		__slots__ = ["_RtrBizDayInf"]
		@property
		def RtrBizDayInf(self):
			return self._RtrBizDayInf

		@RtrBizDayInf.setter
		def RtrBizDayInf(self, value):
			self._RtrBizDayInf = value if value is not None else base_types.UninitialisedField(self, 'RtrBizDayInf', ReturnBusinessDayInformationV07, False)

		@RtrBizDayInf.deleter
		def RtrBizDayInf(self):
			del self._RtrBizDayInf
			self._RtrBizDayInf = base_types.UninitialisedField(self, 'RtrBizDayInf', ReturnBusinessDayInformationV07, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='RtrBizDayInf', type=ReturnBusinessDayInformationV07, min=1, max=1, mutex_group=None, array=False),
		))