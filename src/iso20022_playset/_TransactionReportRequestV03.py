# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MessageIdentification1
from . import ReportSpecification4

class TransactionReportRequestV03(base_types._BaseFieldType):

	__slots__ = ["_ReqId", "_RptSpcfctn"]
	@property
	def ReqId(self):
		return self._ReqId

	@ReqId.setter
	def ReqId(self, value):
		self._ReqId = value if value is not None else base_types.UninitialisedField(self, 'ReqId', MessageIdentification1, False)

	@ReqId.deleter
	def ReqId(self):
		del self._ReqId
		self._ReqId = base_types.UninitialisedField(self, 'ReqId', MessageIdentification1, False)

	@property
	def RptSpcfctn(self):
		return self._RptSpcfctn

	@RptSpcfctn.setter
	def RptSpcfctn(self, value):
		self._RptSpcfctn = value if value is not None else base_types.UninitialisedField(self, 'RptSpcfctn', ReportSpecification4, False)

	@RptSpcfctn.deleter
	def RptSpcfctn(self):
		del self._RptSpcfctn
		self._RptSpcfctn = base_types.UninitialisedField(self, 'RptSpcfctn', ReportSpecification4, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ReqId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptSpcfctn', type=ReportSpecification4, min=1, max=1, mutex_group=None, array=False),
	))