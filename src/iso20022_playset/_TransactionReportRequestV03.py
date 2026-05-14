# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._MessageIdentification1 import MessageIdentification1
from ._ReportSpecification4 import ReportSpecification4

class TransactionReportRequestV03(base_types._BaseFieldType):

	__slots__ = ["_ReqId", "_RptSpcfctn"]
	@property
	def ReqId(self):
		return self._ReqId

	@ReqId.setter
	def ReqId(self, value):
		self._ReqId = value if type(value) != base_types.auto else self.make_default("ReqId")

	@ReqId.deleter
	def ReqId(self):
		del self._ReqId
		self._ReqId = None

	@property
	def RptSpcfctn(self):
		return self._RptSpcfctn

	@RptSpcfctn.setter
	def RptSpcfctn(self, value):
		self._RptSpcfctn = value if type(value) != base_types.auto else self.make_default("RptSpcfctn")

	@RptSpcfctn.deleter
	def RptSpcfctn(self):
		del self._RptSpcfctn
		self._RptSpcfctn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ReqId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptSpcfctn', type=ReportSpecification4, min=1, max=1, mutex_group=None, array=False),
	))