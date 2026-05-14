# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ReportQueryRequestV02 import ReportQueryRequestV02

class ADMI_005_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_RptQryReq"]
		@property
		def RptQryReq(self):
			return self._RptQryReq

		@RptQryReq.setter
		def RptQryReq(self, value):
			self._RptQryReq = value if type(value) != base_types.auto else self.make_default("RptQryReq")

		@RptQryReq.deleter
		def RptQryReq(self):
			del self._RptQryReq
			self._RptQryReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RptQryReq', type=ReportQueryRequestV02, min=1, max=1, mutex_group=None, array=False),
		))